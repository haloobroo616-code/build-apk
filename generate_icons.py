"""
Generate app icons (ic_launcher.png & ic_launcher_round.png) untuk semua density
dari satu file sumber icon.png di root repo.
"""
import os
from PIL import Image

SOURCE_ICON = "icon.png"
RES_DIR = "android/app/src/main/res"

DENSITIES = {
    "mipmap-mdpi": 48,
    "mipmap-hdpi": 72,
    "mipmap-xhdpi": 96,
    "mipmap-xxhdpi": 144,
    "mipmap-xxxhdpi": 192,
}

def main():
    if not os.path.exists(SOURCE_ICON):
        print(f"⚠️  {SOURCE_ICON} tidak ditemukan, skip generate icon.")
        return

    img = Image.open(SOURCE_ICON).convert("RGBA")

    for folder, size in DENSITIES.items():
        out_dir = os.path.join(RES_DIR, folder)
        os.makedirs(out_dir, exist_ok=True)
        resized = img.resize((size, size), Image.LANCZOS)
        resized.save(os.path.join(out_dir, "ic_launcher.png"))
        resized.save(os.path.join(out_dir, "ic_launcher_round.png"))
        print(f"✅ Generated {folder} ({size}x{size})")

if __name__ == "__main__":
    main()
