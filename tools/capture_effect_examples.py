"""Photograph effect changes in the player's real render, with no desktop input."""
import argparse
import json
from pathlib import Path
import time

from PIL import Image, ImageChops, ImageStat

from capture_guide import command


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=19465)
    parser.add_argument("--out", default="shots/ko")
    parser.add_argument("--studio-file", required=True, help="Saved studio JSON in this player's isolated capture profile")
    args = parser.parse_args()
    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    # The diagnostic state is a short summary with different field names.
    # Restore the full serialized settings from the isolated studio instead.
    saved = json.loads(Path(args.studio_file).read_text(encoding="utf-8-sig"))["Post"]
    base = {
        "Enabled": True, "Bloom": False, "ColorGrading": False,
        "Vignette": False, "Grain": False, "ChromaticAberration": False,
        "DepthOfField": False, "MotionBlur": False,
        "Beautify": {"Enabled": False}, "Hbao": {"Enabled": False},
    }
    examples = {
        "vignette": {"Vignette": True, "VignetteIntensity": 0.85, "VignetteSmoothness": 0.65},
        "color": {"ColorGrading": True, "Saturation": -60, "Contrast": 0, "PostExposure": 0, "Temperature": 0, "Tint": 0},
        "pixel": {"Beautify": {"Enabled": True, "Pixelate": True, "PixelateIntensity": 70, "DepthOfField": False, "Blur": False}},
        "bloom": {"Bloom": True, "BloomIntensity": 0.5, "BloomThreshold": 0.9, "BloomDiffusion": 5},
        "dof": {"DepthOfField": True, "DofAutoFocus": True, "DofAperture": 2.8, "DofFocalLength": 85},
    }
    records = []
    try:
        command(args.port, "panel hide")
        command(args.port, "studio-camera preview off")
        for name, edit in examples.items():
            pictures = []
            for state, change in (("off", {}), ("on", edit)):
                command(args.port, "studio post " + json.dumps(base))
                if change:
                    command(args.port, "studio post " + json.dumps(change))
                time.sleep(1.5)
                path = out / ("guide-example-" + name + "-" + state + ".png")
                command(args.port, "studio-camera save-window " + str(path))
                for _ in range(80):
                    try:
                        with Image.open(path) as source:
                            picture = source.convert("RGB").crop((420, 60, 1500, 1020))
                        picture.save(path)
                        pictures.append(picture)
                        break
                    except OSError:
                        time.sleep(0.1)
                print("saved", path.name, flush=True)
            difference = sum(ImageStat.Stat(ImageChops.difference(*pictures)).mean) / 3
            if difference < 0.5:
                raise RuntimeError("Effect has no visible change: " + name)
            records.append({"effect": name, "on": edit, "mean_pixel_difference": round(difference, 3)})
            print(name, "difference", difference, flush=True)
    finally:
        command(args.port, "studio post " + json.dumps(saved))
        command(args.port, "panel show")
    (out / "effect-examples.json").write_text(json.dumps(records, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
