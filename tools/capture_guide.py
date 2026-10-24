"""Capture real UI through a development player's local control channel.

The player renders its own PNG, including its actual open menus, without
moving the desktop pointer or activating its window. Retail builds omit this
channel. Run only against an isolated copy of the chosen user's studio.
"""
import argparse
import json
from pathlib import Path
import socket
import time

from PIL import Image, ImageFilter


def command(port, text):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(("127.0.0.1", 0))
        sock.settimeout(25)
        sock.sendto(text.encode("utf-8"), ("127.0.0.1", port))
        reply = sock.recv(65535).decode("utf-8")
    if not reply.startswith("ok"):
        raise RuntimeError(reply)
    return reply


def capture(port, path, crop=None):
    path = Path(path).resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    command(port, "notices read-all")
    time.sleep(0.2)
    # The player writes asynchronously; an older image must not pass as the new capture.
    path.unlink(missing_ok=True)
    command(port, "screenshot " + str(path))
    for _ in range(120):
        try:
            with Image.open(path) as source:
                image = source.copy()
            if crop:
                image = image.crop(crop)
                image.save(path)
            return image.size
        except (OSError, ValueError):
            time.sleep(0.1)
    raise RuntimeError("Player did not finish writing " + str(path))


def panel_state(port):
    return json.loads(command(port, "panel state")[len("ok panel "):])


def run_plan(port, plan_path, out):
    plan = json.loads(Path(plan_path).read_text(encoding="utf-8-sig"))
    records, failed = [], []
    for shot in plan:
        try:
            records.append(take_shot(port, shot, out))
        except RuntimeError as error:
            # One section the UI no longer draws must not stop the other photographs; the run still fails at the end.
            failed.append(shot["name"])
            print("FAILED", shot["name"], error, flush=True)
    (Path(out) / "capture-manifest.json").write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    if failed:
        raise RuntimeError("Not captured: " + ", ".join(failed))


def take_shot(port, shot, out):
    command(port, "panel menu close")
    command(port, "panel show")
    command(port, "panel open")
    if shot.get("page"):
        command(port, "panel " + shot["page"])
    command(port, "panel popover none")
    command(port, "panel scroll 0")
    if shot.get("reset", True):
        for key, value in panel_state(port)["folds"].items():
            if value > 0.9:
                command(port, "panel fold " + key)
    for text in shot.get("commands", []):
        command(port, text)
    for key in shot.get("open", []):
        command(port, "panel unfold " + key)
    time.sleep(0.8)
    state = panel_state(port)
    focus = shot.get("focus")
    if focus:
        rect = state["sectionHeaders"].get(focus) or state["foldArrows"].get(focus) or state["foldBoxes"].get(focus)
        if isinstance(rect, dict):
            rect = rect["row"]
        if rect is None:
            raise RuntimeError("UI section not drawn: " + focus)
        command(port, "panel scroll " + str(max(0, (rect[1] - 140) / state["scale"] + state["scroll"])))
    elif "scroll" in shot:
        command(port, "panel scroll " + str(shot["scroll"]))
    for text in shot.get("after", []):
        command(port, text)
    time.sleep(0.8)
    state = panel_state(port)
    if "crop" in shot:
        crop = shot["crop"]
    elif shot.get("full"):
        crop = None
    else:
        x, y, width, height = state["drawerRect"]
        crop = [round(x), 62, round(x + width), round(min(height, shot.get("bottom", 1045)))]
        if focus and not shot.get("panel"):
            rect = state["sectionCards"].get(focus)
            if rect:
                crop[1] = round(max(140, rect[1] - 10))
                crop[3] = round(min(1045, rect[1] + rect[3] + 12))
            else:
                row = state["foldArrows"].get(focus, {}).get("row")
                box = state["foldBoxes"].get(focus)
                if row and box:
                    crop[1] = round(max(140, row[1] - 8))
                    crop[3] = round(min(1045, box[1] + box[3] + 12))
    path = Path(out) / (shot["name"] + ".png")
    size = capture(port, path, crop)
    if shot.get("blurLastRow"):
        # A value no photograph may show (this PC's own network address): the last row of that box, from its value on.
        box = state["foldBoxes"][shot["blurLastRow"]]
        top, left = (crop[1], crop[0]) if crop else (0, 0)
        area = (round(box[0] + box[2] * 0.45 - left), round(box[1] + box[3] - 64 - top), round(box[0] + box[2] - left), round(box[1] + box[3] - 4 - top))
        with Image.open(path) as source:
            image = source.copy()
        image.paste(image.crop(area).filter(ImageFilter.GaussianBlur(9)), area[:2])
        image.save(path)
    print("saved", shot["name"], size, flush=True)
    return {**shot, "size": size, "crop": crop, "pageDrawn": state["pageTitle"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=19465)
    parser.add_argument("--command", action="append", default=[])
    parser.add_argument("--output")
    parser.add_argument("--plan")
    parser.add_argument("--out", default="shots/ko")
    parser.add_argument("--crop", type=int, nargs=4, metavar=("LEFT", "TOP", "RIGHT", "BOTTOM"))
    args = parser.parse_args()
    if args.plan:
        run_plan(args.port, args.plan, args.out)
        return
    for text in args.command:
        print(command(args.port, text))
    if args.output:
        time.sleep(0.65)
        print(json.dumps({"path": str(Path(args.output).resolve()), "size": capture(args.port, args.output, args.crop)}))


if __name__ == "__main__":
    main()
