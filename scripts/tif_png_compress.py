from PIL import Image
import os

# 设置图像目录
media_dir = r"./example/word/media"
max_width = 1000  # 超过该宽度将自动缩放

# 遍历文件
for file in os.listdir(media_dir):
    ext = os.path.splitext(file)[1].lower()
    input_path = os.path.join(media_dir, file)

    # 处理 .tif / .tiff
    if ext in [".tif", ".tiff"]:
        try:
            with Image.open(input_path) as img:
                img = img.convert("RGB")
                if img.width > max_width:
                    scale = max_width / img.width
                    img = img.resize((int(img.width * scale), int(img.height * scale)), Image.ANTIALIAS)

                # 保存为原路径，使用 LZW 压缩（无损）
                img.save(input_path, format="TIFF", compression="tiff_lzw")
                print(f"[✓] Compressed TIF: {file}")
        except Exception as e:
            print(f"[✗] Failed to compress TIF {file}: {e}")

    # 处理 .png
    elif ext == ".png":
        try:
            with Image.open(input_path) as img:
                if img.mode not in ["RGB", "RGBA"]:
                    img = img.convert("RGBA")
                if img.width > max_width:
                    scale = max_width / img.width
                    img = img.resize((int(img.width * scale), int(img.height * scale)), Image.ANTIALIAS)

                # 覆盖保存，启用 PNG 压缩优化
                img.save(input_path, format="PNG", optimize=True)
                print(f"[✓] Compressed PNG: {file}")
        except Exception as e:
            print(f"[✗] Failed to compress PNG {file}: {e}")
