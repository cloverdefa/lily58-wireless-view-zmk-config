import subprocess
from pathlib import Path


def main():
    base_dir = Path(".")
    yaml_file = base_dir / "lily58_keymap.yaml"
    svg_file = base_dir / "IMG/lily58.svg"
    svg_file.parent.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        "keymap parse -c 10 -z ./config/lily58.keymap > lily58_keymap.yaml",
        shell=True,
        check=True,
    )
    subprocess.run(
        "keymap draw lily58_keymap.yaml > IMG/lily58.svg", shell=True, check=True
    )
    print(f"✅ 已生成 SVG: {svg_file}")


if __name__ == "__main__":
    main()
