import subprocess
from pathlib import Path


def main():
    base_dir = Path(".")
    yaml_file = base_dir / "lily58_keymap.yaml"
    svg_file = base_dir / "IMG/lily58.svg"
    svg_file.parent.mkdir(parents=True, exist_ok=True)

    # parse -> YAML
    parse_cmd = f'keymap parse -c 10 -z ./config/lily58.keymap > "{yaml_file}"'
    subprocess.run(parse_cmd, shell=True, check=True)

    # draw -> SVG
    draw_cmd = f'keymap draw "{yaml_file}" > "{svg_file}"'
    subprocess.run(draw_cmd, shell=True, check=True)

    print(f"✅ 已生成 SVG: {svg_file}")


if __name__ == "__main__":
    main()
