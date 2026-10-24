"""Photograph each translated UI in an isolated, minimized development player.

Uses the player's own render channel, not desktop input or image translation.
The source profile and avatar assets are never modified.
"""
import argparse
import ctypes
from ctypes import wintypes
import json
from pathlib import Path
import re
import shutil
import socket
import sys
import time

from PIL import Image, ImageFilter

from capture_guide import capture, command, panel_state, run_plan


NEUTRAL_POST = {
    "Enabled": True, "Bloom": False, "ColorGrading": False,
    "Vignette": False, "Grain": False, "ChromaticAberration": False,
    "DepthOfField": False, "MotionBlur": False,
    "Beautify": {"Enabled": False}, "Hbao": {"Enabled": False},
}
WORDS = {
    "ko": ("설정", "일반 동작", "앉은 자세", "자세", "표정", "뷰", "카메라", "라이트"),
    "en": ("Settings", "Standard poses", "Sitting pose", "Pose", "Expression", "View", "Camera", "Light"),
    "ja": ("設定", "通常ポーズ", "座り姿勢", "ポーズ", "表情", "ビュー", "カメラ", "ライト"),
    "zh": ("设置", "普通动作", "坐姿", "姿态", "表情", "视图", "相机", "光源"),
}


class Window:
    """The capture player's window, shown off the desktop without activation, and clicks posted to it. The process is per-monitor
    DPI aware so that posted coordinates are the player's own client pixels (the display may be scaled)."""

    class Placement(ctypes.Structure):
        _fields_ = [("length", wintypes.UINT), ("flags", wintypes.UINT), ("showCmd", wintypes.UINT),
                    ("minimum", wintypes.POINT), ("maximum", wintypes.POINT), ("normal", wintypes.RECT)]

    def __init__(self, pid, cmd):
        self.user32 = ctypes.WinDLL("user32", use_last_error=True)
        self.user32.SetProcessDpiAwarenessContext(ctypes.c_void_p(-4))
        self.user32.PostMessageW.argtypes = [wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM]
        self.cmd = cmd
        found = []
        def each(hwnd, _):
            owner = wintypes.DWORD()
            self.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(owner))
            if owner.value == pid and self.user32.IsWindowVisible(hwnd):
                found.append(hwnd)
            return True
        self.user32.EnumWindows(ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)(each), 0)
        if not found:
            raise RuntimeError("No window of the capture player")
        self.hwnd = found[0]

    def show_offscreen(self):
        """Restored from minimized without activation, far left of every monitor: the player draws and takes posted input."""
        placement = self.Placement()
        placement.length = ctypes.sizeof(placement)
        self.user32.GetWindowPlacement(self.hwnd, ctypes.byref(placement))
        rect = placement.normal
        width, height = rect.right - rect.left, rect.bottom - rect.top
        rect.left, rect.top, rect.right, rect.bottom = -6000, 100, -6000 + width, 100 + height
        placement.showCmd = 4  # SW_SHOWNOACTIVATE
        self.user32.SetWindowPlacement(self.hwnd, ctypes.byref(placement))
        time.sleep(1.0)

    def post(self, message, keys, x, y):
        self.user32.PostMessageW(self.hwnd, message, keys, (int(y) << 16) | (int(x) & 0xFFFF))

    def click(self, x, y):
        self.cmd("input on")
        self.post(0x200, 0, x, y)
        time.sleep(0.08)
        self.post(0x201, 1, x, y)
        time.sleep(0.08)
        self.post(0x202, 0, x, y)
        time.sleep(0.25)
        # Off every control: no hover tip stays in the photograph.
        self.post(0x200, 0, 1300, 1070)
        time.sleep(0.1)
        self.cmd("input off")


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def write(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


# Profile parts a capture never takes from the user's settings: logins, tokens, channels, linked Discord
# channels, the user's own graphs and rules. The capture starts from the app's defaults for them.
PRIVATE_SETTINGS = ("Twitch", "Chzzk", "Soop", "Discord", "Graphs", "Broadcast", "DonationBox", "Share")  # Share: the PC's game and window list
# The user's current studio ("Main 3": grey background, screen light off) and one more scene for the scene list. Copies only;
# the capture studio leaves out its room and background picture; its exposure stays the user's.
CAPTURE_STUDIO = "studio-fb96c3efe0d9"
SCENES = (CAPTURE_STUDIO, "studio-c03f89839740")
# The only avatars a capture may show (the user's list): Main, Loop Neko, 아이리 Straight Flush, Kaguya_Mayo_뉴.
ALLOWED_AVATARS = ("av-2f53db2d8cbf6641", "av-aa2e9b1d963cf11a", "av-86cf4df20bbafb84", "av-3c8c42cfb1b66883")
# Example 간편 설정 items for the broadcast chapters (names in each language; the reward title is what a viewer would redeem).
SAMPLE_RULES = {
    "ko": ("팔로우하면 던지기", "큰 후원에 물 뿌리기", "디스코드 반응으로 던지기", "채널 포인트로 조명", "조명 바꾸기"),
    "en": ("Throw on a follow", "Splash on a big donation", "Throw on Discord reactions", "Lights on channel points", "Change the lights"),
    "ja": ("フォローで投げる", "大きな支援で水をかける", "Discordのリアクションで投げる", "チャンネルポイントで照明", "照明を変える"),
    "zh": ("关注时投掷", "大额打赏时泼水", "Discord 反应时投掷", "频道点数切换灯光", "换个灯光"),
}
SAMPLE_GRAPH = {"ko": "후원 1만 원 이상이면 물 뿌리기", "en": "Splash on donations of 10,000 won or more",
                "ja": "1万ウォン以上の支援で水をかける", "zh": "打赏满 1 万韩元时泼水"}
# The default lighting preset's face spot light: the lighting example changes its colour for a while.
SAMPLE_LIGHT = "d2cb09e0c559"  # Spot Light in Main's own lighting preset (user:7fee108b6ee9)
TRIGGERS = ("OnRedeem", "OnChat", "OnFollow", "OnSubscribe", "OnBits", "OnChzzkChat", "OnChzzkDonation", "OnChzzkSubscribe",
            "OnSoopChat", "OnSoopBalloon", "OnSoopSubscribe", "OnDiscordReaction", "OnDiscordGame")


def sample_rules(template, lang):
    """Four 간편 설정 items made from one of the user's own items (its object list, liquid and light values), with
    made-up triggers; no login, channel or viewer of the user's is in them. The app makes their graphs when it starts."""
    names = SAMPLE_RULES[lang]
    def rule(index, kind, **fields):
        item = json.loads(json.dumps(template))
        item.update({key: False for key in TRIGGERS})
        item.update(Id="sample%026d" % index, Enabled=True, Name=names[index], ActionKind=kind, GraphSignature="",
                    EditedInAdvanced=False, RewardTitle="", ChatContains="", DiscordReaction="", Cooldown=3.0)
        item.update(fields)
        return item
    return [
        rule(0, 2, OnFollow=True),
        rule(1, 3, OnChzzkDonation=True, ChzzkDonationMin=10000, OnBits=True, BitsMin=1000, OnSoopBalloon=True, SoopBalloonMin=100),
        rule(2, 2, OnDiscordReaction=True),
        rule(3, 5, OnRedeem=True, RewardTitle=names[4],
             Lighting=dict(template["Lighting"], Kind=1, Light=SAMPLE_LIGHT, SetColor=True, ColorR=1.0, ColorG=0.62, ColorB=0.75, Seconds=5.0)),
    ]


def sample_graph(lang):
    """A small hand-laid graph for the node editor chapter: a CHZZK donation of 10,000 won or more pours liquid. Switched off, so
    it never runs; the graphs the app makes from 간편 설정 items overlap their nodes and do not read as an example."""
    ids = ["5a3e0000-0000-4000-8000-00000000000%d" % i for i in range(4)]  # the app reads node ids as GUIDs
    node = lambda i, type_id, title, x, y, inputs=None: (ids[i], {
        "id": ids[i], "typeId": type_id, "name": title, "version": 0,
        "dataInputs": {key: {"value": json.dumps(value)} for key, value in (inputs or {}).items()}, "x": str(x), "y": str(y)})
    link = lambda a, out, b, into: {"outputNode": ids[a], "inputNode": ids[b], "outputPort": out, "inputPort": into}
    return json.dumps({
        "id": "5a3e0000-0000-4000-8000-0000000000aa", "enabled": False, "name": SAMPLE_GRAPH[lang],
        # The editor opens with the graph's origin in the middle of its canvas: the nodes sit left and up of it to be all in view.
        "nodes": dict([node(0, "OnChzzkDonation", "ON_CHZZK_DONATION", -690, -350),
                       node(1, "IntegerGreaterThanOrEqual", "INTEGER_GREATER_THAN_OR_EQUAL", -400, -10, {"B": 10000}),
                       node(2, "IfBranch", "IF_BRANCH", -130, -350),
                       node(3, "LaunchLiquid", "LAUNCH_LIQUID", 160, -350)]),
        "dataConnections": [link(0, "Amount", 1, "A"), link(1, "Result", 2, "Condition")],
        "flowConnections": [link(0, "Exit", 2, "Enter"), link(2, "IfTrue", 3, "Enter")],
        "properties": {"variables": []},
    }, ensure_ascii=False)


def prepare(source, target, lang):
    """An isolated copy of the user's profile for one language; the user's own files are only read."""
    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True)
    # The avatars keep their own lights (Main: the user's preset user:7fee108b6ee9), as the user sees them.
    shutil.copy2(source / "lighting-presets.json", target / "lighting-presets.json")
    for name in ("thumbnails", "poses", "content-packs"):
        if (source / name).is_dir():
            shutil.copytree(source / name, target / name)
    (target / "avatars").mkdir()
    for avatar in ALLOWED_AVATARS:
        shutil.copy2(source / "avatars" / (avatar + ".json"), target / "avatars")
    (target / "studios").mkdir()
    for scene in SCENES:
        studio = read(source / "studios" / (scene + ".studio.json"))
        studio["Background"]["ImagePath"] = ""
        for slot in studio["Slots"]:
            if slot.get("DefaultAvatarId") not in ALLOWED_AVATARS:
                slot.update(DefaultAvatarId=ALLOWED_AVATARS[0], DefaultAvatarName="Main", DefaultAvatarFile="")
        if scene == CAPTURE_STUDIO:
            studio["Room"].update(Pack="", Id="", Pieces=[], HiddenParts=[])
            studio["Background"]["Mode"] = 0
            studio["ScreenLight"]["Enabled"] = False
        else:
            # Its picture shows the Main avatar in this studio; the capture studio's own picture showed another avatar.
            shutil.copy2(source / "studios" / (scene + ".thumb.jpg"), target / "studios")
        write(target / "studios" / (scene + ".studio.json"), studio)
    # The signed room-pack list and its pictures: the DLC rooms show as they do on this PC.
    if (source / "cache/room-packs").is_dir():
        shutil.copytree(source / "cache/room-packs", target / "cache/room-packs", ignore=shutil.ignore_patterns("downloads"))
    settings = read(source / "settings.json")
    template = next(iter(settings.get("Twitch", {}).get("Rules", [])), None)
    for key in PRIVATE_SETTINGS:
        settings.pop(key, None)
    if template is None:
        raise RuntimeError("The profile has no 간편 설정 item to model the examples on")
    settings["Twitch"] = {"Enabled": False, "Rules": sample_rules(template, lang)}
    settings["Graphs"] = [sample_graph(lang)]
    settings.update(Language=lang, UiScale=1.25, LastAvatarId=ALLOWED_AVATARS[0])
    recent, seen = [], set()
    for item in settings["Launcher"]["Recent"]:
        if item["Id"] in ALLOWED_AVATARS and item["Id"] not in seen:
            seen.add(item["Id"])
            recent.append(item)
    settings["Launcher"]["Recent"] = recent
    # No camera picture or voice of the user in a capture: the avatar stands in its idle pose.
    settings["General"].update(StartWebcam=False, StartMicrophone=False)
    # A capture must never replace the executable when its player quits.
    settings["Updates"].update(AutoUpdate=False, InstallOnQuit=False)
    settings["Output"].update(Spout=False, Ndi=False, VirtualCamera=False)
    settings["Session"].update(Address="203.0.113.10:47700", Name="Guest", Port=47700,
                               JoinSecret="", HostSecret="", SendAvatar=False,
                               SendAvatarConsent=False)
    settings["CurrentStudioId"] = CAPTURE_STUDIO
    words = WORDS[lang]
    translate = lang != "ko"
    for p in (target / "avatars").glob("*.json"):
        profile = read(p)
        if translate:
            for i, pose in enumerate(profile.get("Posing", {}).get("Poses", [])):
                if pose.get("Builtin") == "sit" or pose.get("Id") == "builtin-sit":
                    pose["Name"] = words[2]
                elif re.search("[가-힣]", pose.get("Name", "")):
                    pose["Name"] = words[3] + " " + str(i)
            for i, expression in enumerate(profile.get("Expressions", {}).get("Custom", []), 1):
                expression["Name"] = words[4] + " " + str(i)
            for i, view in enumerate(profile.get("Camera", {}).get("Presets", []), 1):
                view["Name"] = words[5] + " " + str(i)
        write(p, profile)
    for p in (target / "studios").glob("*.studio.json"):
        studio = read(p)
        if translate:
            for i, camera in enumerate(studio.get("Cameras", []), 1):
                camera["Name"] = words[6] + " " + str(i)
            for i, light in enumerate(studio.get("Lights", []), 1):
                light["Name"] = words[7] + " " + str(i)
        write(p, studio)
    if translate:
        for i, view in enumerate(settings.get("Camera", {}).get("Presets", []), 1):
            view["Name"] = words[5] + " " + str(i)
    write(target / "settings.json", settings)
    # The pose library shows the user's own motion clips, in a folder named in the capture's language.
    poses = target / words[1]
    poses.mkdir(exist_ok=True)
    for source_clip in (source / "clips").glob("*.anim"):
        shutil.copy2(source_clip, poses / source_clip.name)
    if not any(poses.glob("*.anim")):
        raise RuntimeError("No motion clips to show in the pose library")
    return settings, poses


def take_language(args, lang):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as probe:
        probe.settimeout(0.3)
        probe.sendto(b"ping", ("127.0.0.1", args.port))
        try:
            probe.recv(1024)
        except (socket.timeout, ConnectionResetError):
            pass
        else:
            raise RuntimeError("Capture port already belongs to a running player")
    source = Path(args.profile).resolve()
    root = Path(__file__).resolve().parent.parent
    target = root / ".local" / "capture" / lang
    settings, poses = prepare(source, target, lang)
    own_post = read(target / "studios" / (CAPTURE_STUDIO + ".studio.json"))["Post"]  # before the player saves the studio
    out = root / "shots" / ("zh-Hans" if lang == "zh" else lang)
    out.mkdir(parents=True, exist_ok=True)
    only = set(args.only.split(",")) if args.only else None
    # --resume: a photograph already taken in this run is not taken again (shots/ holds only this refresh's PNGs).
    want = lambda name: (only is None or name in only) and not (args.resume and (out / (name + ".png")).exists())
    port = args.port
    cmd = lambda text: command(port, text)
    sys.path.insert(0, str(Path(args.worktree).resolve() / "tools"))
    sys.path.insert(0, str(Path(args.nofocus).resolve()))
    from osf_synth import Control
    from nofocus import launch

    # Shown without activation; if the player still takes the foreground, the user's window gets it back.
    player = launch([
        str(Path(args.player).resolve()), "-adrAvatarBundle", args.bundle,
        "-adrControlPort", str(port), "-adrSettings", str(target / "settings.json"),
        "-adrFeatures", "all", "-screen-fullscreen", "0", "-screen-width", "1920",
        "-screen-height", "1080", "-adrUiMonitorHeight", "1080", "-adrNoRelaunch",
        "-logFile", str(target / "capture-player.log"),
    ], log=lambda text: print(lang, text, flush=True))
    print(lang, "capture PID", player.pid, flush=True)
    records, missed = [], []

    def snap(name, crop, blur=None):
        if not want(name):
            return
        time.sleep(0.9)
        size = capture(port, out / (name + ".png"), crop)
        if blur:
            # Something no photograph may show (a folder path holds the Windows user name), in the saved picture's pixels.
            with Image.open(out / (name + ".png")) as source:
                image = source.copy()
            image.paste(image.crop(blur).filter(ImageFilter.GaussianBlur(9)), blur[:2])
            image.save(out / (name + ".png"))
        records.append({"name": name, "language": lang, "crop": crop, "size": size})
        print(lang, "saved", name, size, flush=True)

    def open_page(page):
        for text in ("panel menu close", "panel popover none", "panel show", "panel open", "panel " + page, "panel scroll 0"):
            cmd(text)
        for key, value in panel_state(port)["folds"].items():
            if value > 0.9:
                cmd("panel fold " + key)

    def focus(key):
        time.sleep(0.8)
        state = panel_state(port)
        rect = state["sectionHeaders"].get(key) or state["foldArrows"].get(key)
        if isinstance(rect, dict):
            rect = rect["row"]
        if rect is None:
            raise RuntimeError("No visible section " + key)
        cmd("panel scroll " + str(max(0, (rect[1] - 145) / state["scale"] + state["scroll"])))
        time.sleep(0.8)

    try:
        Control(port).wait_ready(timeout=75)
        cmd("window minimize")
        open_page("Settings")
        title = panel_state(port)["pageTitle"]
        if title != WORDS[lang][0]:
            raise RuntimeError("Wrong UI language: " + title)
        cmd("studio-camera preview off")
        cmd("studio post " + json.dumps(NEUTRAL_POST))
        open_page("AvatarMenu")
        # Open ordinary expression toggles, never the root with its adult submenu.
        for _ in range(4):
            tiles = panel_state(port)["tiles"]
            if any(tile["name"] == "eyes star" for tile in tiles):
                break
            cmd("panel tile 0")
            time.sleep(0.4)
        else:
            raise RuntimeError("Could not open the reviewed expression submenu")

        plan = read(Path(__file__).with_name("guide_capture_plan.json"))
        plan = [shot for shot in plan if want(shot["name"])]
        if plan:
            path = target / "capture-plan.json"
            write(path, plan)
            try:
                run_plan(port, path, out)
            except RuntimeError as error:
                missed.append(str(error))
            records.extend(read(out / "capture-manifest.json"))
        # Shots with the avatar keep the studio's own post-processing (the look the user sees).
        cmd("studio post " + json.dumps(own_post))
        open_page("AvatarMenu")
        time.sleep(0.8)
        card = panel_state(port)["sectionCards"]["menu.tiles"]
        snap("guide-avatar-menu", [98, 65, 648, round(card[1] + card[3] + 10)])
        cmd("panel unfold menu.poses")
        cmd("panel unfold menu.myexpr")
        snap("guide-main", [0, 0, 1420, 1080])
        focus("menu.poses")
        state = panel_state(port)
        a, b = state["sectionCards"]["menu.poses"], state["sectionCards"]["menu.myexpr"]
        snap("guide-menu-poses", [98, round(a[1]-8), 648, round(min(1045, b[1]+b[3]+8))])
        cmd("panel scroll 0")
        cmd("panel tilemenu 1")
        snap("guide-menu-context", [0, 0, 650, 520])
        cmd("panel menu close")
        cmd("panel popover avatar")
        snap("guide-avatar-library", [85, 0, 980, 800], blur=(155, 138, 565, 170))
        cmd("panel popover none")
        cmd("panel popover camera")
        time.sleep(0.8)
        x, y, w, h = panel_state(port)["popoverRect"]
        snap("guide-camera-toolbar", [round(x-10), round(y-10), round(x+w+10), round(min(1080, y+h+10))])

        open_page("Scene")
        cmd("panel unfold scene.posing")
        cmd("panel unfold pose.tracking.builtin-sit")
        focus("scene.posing")
        snap("guide-pose-tracking", [98, 140, 648, 750])
        cmd("panel fold pose.tracking.builtin-sit")
        cmd("panel pose library folder " + str(poses))
        cmd("panel pose library search")
        cmd("panel pose library show")
        time.sleep(1.6)
        focus("pose.library")
        state = panel_state(port)
        row = state["foldArrows"]["pose.library"]["row"]
        box = state["foldBoxes"]["pose.library"]
        snap("guide-pose-library", [115, round(max(138, row[1]-8)), 615,
                                    round(min(1045, box[1]+box[3]+10))])

        open_page("Motion")
        cmd("facecal begin")
        snap("guide-face-calibration", [662, 261, 1257, 819])
        cmd("facecal cancel")

        # These photographs contain no UI or language. Preserve the reviewed render.
        for path in (root / "shots/ko").glob("guide-example-*.png"):
            if want(path.stem):
                shutil.copy2(path, out / path.name)
                records.append({"name": path.stem, "language": "none", "source": "reviewed UI-free Main render"})

        # 간편 설정 items opened in place: the trigger of one, the action settings of three.
        rule = lambda index: "settings.twitch.rule.sample%026d" % index
        def rule_shot(name, index, where):
            if not want(name):
                return
            open_page("interact")
            cmd("panel unfold bc.rules")
            cmd("panel unfold " + rule(index))
            time.sleep(0.8)
            state = panel_state(port)
            if where == "top":
                top = state["switchRows"][rule(index)]["row"][1] - 240  # below the page's tabs, which stay at the top
            elif where == "bottom":
                box = state["foldBoxes"][rule(index)]
                top = box[1] + box[3] - 1000
            else:
                top = state["foldArrows"][rule(index) + "." + where]["row"][1] - 420
            cmd("panel scroll %d" % (state["scroll"] + top))
            snap(name, [90, 140, 640, 1045])
        rule_shot("guide-rule-trigger", 3, "top")
        rule_shot("guide-rule-throw", 0, "throw.props")
        rule_shot("guide-rule-liquid", 1, "bottom")
        rule_shot("guide-rule-light", 3, "bottom")

        if any(want(name) for name in ("guide-simple-setup", "guide-simple-setup-connect", "guide-node-editor", "guide-node-editor-lists")):
            window = Window(player.pid, cmd)
            window.show_offscreen()
            open_page("interact")
            cmd("panel unfold bc.rules")
            time.sleep(0.8)
            state = panel_state(port)
            x, y, w, h = state["sectionCards"]["bc.nodes"]
            window.click(470, y + h / 2)
            time.sleep(2.5)
            # The graph list and the node list closed: the example graph alone on the canvas.
            window.click(58, 104)
            window.click(1862, 104)
            snap("guide-node-editor", [30, 30, 1890, 1050])
            window.click(58, 104)
            window.click(1862, 104)
            snap("guide-node-editor-lists", [30, 30, 1890, 1050])
            window.click(1860, 55)
            time.sleep(1.0)
            open_page("interact")
            cmd("panel unfold bc.rules")
            time.sleep(0.8)
            chip = panel_state(port)["linkChips"]["bc.rules.chip"]["rect"]
            window.click(chip[0] + chip[2] / 2, chip[1] + chip[3] / 2)
            time.sleep(1.0)
            state = panel_state(port)
            card, below = state["sectionCards"]["bc.rules"], state["switchRows"][rule(0)]["row"]
            snap("guide-simple-setup", [90, round(card[1] - 10), 640, round(below[1] - 6)])
            # 다음: the second step asks for the chosen platform's login (nothing is sent until its button is pressed).
            window.click(520, below[1] - 34)
            time.sleep(1.0)
            state = panel_state(port)
            card, below = state["sectionCards"]["bc.rules"], state["switchRows"][rule(0)]["row"]
            snap("guide-simple-setup-connect", [90, round(card[1] - 10), 640, round(below[1] - 6)])
            cmd("window minimize")

        if want("guide-launcher") or want("guide-launcher-start"):
            cmd("choose-avatar")
            cmd('settings {"UiScale":1.0}')
            cmd("launcher webcam off")
            cmd("launcher mic off")
            time.sleep(2)
            snap("guide-launcher", None)
            snap("guide-launcher-start", [1135, 100, 1870, 1070])
        manifest = out / "localized-capture-manifest.json"
        if (only or args.resume) and manifest.exists():
            previous = {item["name"]: item for item in read(manifest)}
            previous.update({item["name"]: item for item in records})
            write(manifest, list(previous.values()))
        else:
            write(manifest, records)
        print(lang, "completed", len(records), "photos", flush=True)
        if missed:
            raise RuntimeError(lang + ": " + "; ".join(missed))
    finally:
        try:
            cmd("quit")
            player.wait(timeout=15)
        except Exception:
            player.terminate()  # Only this script's own capture process.


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", default=str(Path.home() / "AppData/LocalLow/Curious Bobby Co/Avatar Live"),
                        help="The user's profile folder (only read; each language gets its own copy under .local/capture)")
    parser.add_argument("--bundle", required=True, help="The reviewed avatar's bundle")
    parser.add_argument("--worktree", required=True, help="Runtime worktree whose tools/osf_synth.py talks to the player")
    parser.add_argument("--nofocus", required=True, help="Folder of nofocus.py, which starts the player without taking focus")
    parser.add_argument("--player", required=True, help="Frozen development-player executable")
    parser.add_argument("--languages", nargs="+", choices=list(WORDS), default=list(WORDS))
    parser.add_argument("--port", type=int, default=19465)
    parser.add_argument("--only", help="Comma-separated capture names for a targeted retake")
    parser.add_argument("--resume", action="store_true", help="Skip photographs whose PNG already exists")
    parser.add_argument("--attempts", type=int, default=6, help="Start the player again this many times if it goes away")
    args = parser.parse_args()
    for lang in args.languages:
        resume = args.resume
        for attempt in range(1, args.attempts + 1):
            try:
                take_language(args, lang)
                break
            except (OSError, TimeoutError) as error:
                # The player went away (another program ended it, or it stopped answering): start again, keeping
                # the photographs already taken.
                print(lang, "attempt", attempt, "lost the player:", error, flush=True)
                args.resume = True
                if attempt == args.attempts:
                    raise
        args.resume = resume


if __name__ == "__main__":
    main()
