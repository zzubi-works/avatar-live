"""Photograph each translated UI in an isolated, minimized development player.

Uses the player's own render channel, not desktop input or image translation.
The source profile and avatar assets are never modified.
"""
import argparse
import json
from pathlib import Path
import re
import shutil
import socket
import subprocess
import sys
import time

from capture_guide import capture, command, panel_state, run_plan


NEUTRAL_POST = {
    "Enabled": True, "Bloom": False, "ColorGrading": False,
    "Vignette": False, "Grain": False, "ChromaticAberration": False,
    "DepthOfField": False, "MotionBlur": False,
    "Beautify": {"Enabled": False}, "Hbao": {"Enabled": False},
}
WORDS = {
    "en": ("Settings", "Standard poses", "Sitting pose", "Pose", "Expression", "View", "Camera", "Light"),
    "ja": ("設定", "通常ポーズ", "座り姿勢", "ポーズ", "表情", "ビュー", "カメラ", "ライト"),
    "zh": ("设置", "普通动作", "坐姿", "姿态", "表情", "视图", "相机", "光源"),
}


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def write(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def prepare(source, target, lang):
    target.mkdir(parents=True, exist_ok=True)
    for name in ("avatars", "studios", "thumbnails"):
        shutil.copytree(source / name, target / name, dirs_exist_ok=True)
    settings = read(source / "settings.json")
    settings.update(Language=lang, UiScale=1.25)
    # A capture must never replace the executable when its player quits.
    settings["Updates"].update(AutoUpdate=False, InstallOnQuit=False)
    settings["Output"].update(Spout=False, Ndi=False, VirtualCamera=False)
    settings["Session"].update(Address="203.0.113.10:47700", Name="Guest", Port=47700,
                               JoinSecret="", HostSecret="", SendAvatar=False,
                               SendAvatarConsent=False)
    words = WORDS[lang]
    for p in (target / "avatars").glob("*.json"):
        profile = read(p)
        for i, pose in enumerate(profile.get("Posing", {}).get("Poses", [])):
            if pose.get("Builtin") == "sit" or pose.get("Id") == "builtin-sit":
                pose["Name"] = words[2]
            elif re.search("[가-힣]", pose.get("Name", "")):
                pose["Name"] = words[3] + " " + str(i)
        for i, expression in enumerate(profile.get("Expressions", {}).get("Custom", []), 1):
            expression["Name"] = words[4] + " " + str(i)
        for i, view in enumerate(profile.get("Camera", {}).get("Presets", []), 1):
            view["Name"] = words[5] + " " + str(i)
        for i, light in enumerate(profile.get("Lighting", {}).get("Lights", []), 1):
            light["Name"] = words[7] + " " + str(i)
        write(p, profile)
    for p in (target / "studios").glob("*.studio.json"):
        studio = read(p)
        for i, camera in enumerate(studio.get("Cameras", []), 1):
            camera["Name"] = words[6] + " " + str(i)
        for i, light in enumerate(studio.get("Lights", []), 1):
            light["Name"] = words[7] + " " + str(i)
        write(p, studio)
    for i, view in enumerate(settings.get("Camera", {}).get("Presets", []), 1):
        view["Name"] = words[5] + " " + str(i)
    write(target / "settings.json", settings)
    poses = target / words[1]
    poses.mkdir(exist_ok=True)
    for source_clip in (source / "일반 동작" / "서 있는 자세").glob("*.anim"):
        shutil.copy2(source_clip, poses / source_clip.name)
    if len(list(poses.glob("*.anim"))) != 3:
        raise RuntimeError("Expected the three reviewed standing-motion clips")
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
    target = source / "localized" / lang
    settings, poses = prepare(source, target, lang)
    root = Path(__file__).resolve().parent.parent
    out = root / "shots" / ("zh-Hans" if lang == "zh" else lang)
    out.mkdir(parents=True, exist_ok=True)
    only = set(args.only.split(",")) if args.only else None
    want = lambda name: only is None or name in only
    port = args.port
    cmd = lambda text: command(port, text)
    sys.path.insert(0, str(Path(args.worktree).resolve() / "tools"))
    from osf_synth import Control

    si = subprocess.STARTUPINFO()
    si.dwFlags = subprocess.STARTF_USESHOWWINDOW
    si.wShowWindow = 7  # SW_SHOWMINNOACTIVE: no foreground activation.
    exe = Path(args.player).resolve() if args.player else Path(args.worktree).resolve() / ".local/builds/v45/AvatarLive.exe"
    player = subprocess.Popen([
        str(exe), "-adrAvatarBundle", settings["Launcher"]["Recent"][0]["Path"],
        "-adrControlPort", str(port), "-adrSettings", str(target / "settings.json"),
        "-adrFeatures", "all", "-screen-fullscreen", "0", "-screen-width", "1920",
        "-screen-height", "1080", "-adrUiMonitorHeight", "1080", "-adrNoRelaunch",
        "-logFile", str(target / "capture-player.log"),
    ], startupinfo=si)
    print(lang, "capture PID", player.pid, flush=True)
    records = []

    def snap(name, crop):
        if not want(name):
            return
        time.sleep(0.9)
        size = capture(port, out / (name + ".png"), crop)
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
            run_plan(port, path, out)
            records.extend(read(out / "capture-manifest.json"))
        cmd("studio post " + json.dumps(NEUTRAL_POST))
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
        snap("guide-avatar-library", [85, 0, 980, 800])
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

        if want("guide-launcher") or want("guide-launcher-start"):
            cmd("choose-avatar")
            cmd('settings {"UiScale":1.0}')
            cmd("launcher webcam off")
            cmd("launcher mic off")
            time.sleep(2)
            snap("guide-launcher", None)
            snap("guide-launcher-start", [1135, 100, 1870, 1070])
        manifest = out / "localized-capture-manifest.json"
        if only and manifest.exists():
            previous = {item["name"]: item for item in read(manifest)}
            previous.update({item["name"]: item for item in records})
            write(manifest, list(previous.values()))
        else:
            write(manifest, records)
        print(lang, "completed", len(records), "photos", flush=True)
    finally:
        try:
            cmd("quit")
            player.wait(timeout=15)
        except Exception:
            player.terminate()  # Only this script's own capture process.


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", required=True)
    parser.add_argument("--worktree", required=True)
    parser.add_argument("--player", help="Optional frozen development-player executable")
    parser.add_argument("--languages", nargs="+", choices=list(WORDS), default=list(WORDS))
    parser.add_argument("--port", type=int, default=19465)
    parser.add_argument("--only", help="Comma-separated capture names for a targeted retake")
    args = parser.parse_args()
    for lang in args.languages:
        take_language(args, lang)


if __name__ == "__main__":
    main()
