import os
import subprocess

inkscape_path = r"C:\Program Files\Inkscape\bin\inkscape.exe"
media_dir = r"./example/word/media"

for file in os.listdir(media_dir):
    if file.lower().endswith(".wmf"):
        input_path = os.path.join(media_dir, file)
        output_name = os.path.splitext(file)[0] + ".png"
        output_path = os.path.join(media_dir, output_name)

        try:
            subprocess.run([
                inkscape_path, input_path,
                "--export-type=png",
                f"--export-filename={output_path}"
            ], check=True)
            os.remove(input_path)  # 删除原 .wmf
            print(f"[✓] Converted and replaced: {file} → {output_name}")
        except subprocess.CalledProcessError as e:
            print(f"[✗] Failed to convert {file}: {e}")
