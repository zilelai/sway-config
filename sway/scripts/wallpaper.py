#!/usr/bin/env python3
import sys
import subprocess

wallpapers = {
    "1": "/home/zilelai/Downloads/wallpaper1.webp",
    "2": "/home/zilelai/Downloads/wallpaper2.jpeg",
}

def main():
    if len(sys.argv) < 2:
        print("Usage: set_wallpaper.py <number>")
        sys.exit(1)

    key = sys.argv[1]

    if key in wallpapers:
        path = wallpapers[key]
        subprocess.run(["pkill", "swaybg"])
        subprocess.Popen(["swaybg", "-i", path, "-m", "fill"])
    else:
        print(f"No wallpaper mapped for '{key}'")
        sys.exit(1)

if __name__ == "__main__":
    main()
