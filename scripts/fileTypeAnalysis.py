import os

# 设置要统计的文件夹路径
target_dir = r"./example/word/media"

# 要统计的扩展名（不区分大小写）
exts_to_track = [".tiff", ".tif", ".wmf", ".png", ".jpeg", ".jpg"]

# 存储结果的字典
file_stats = {ext: {"count": 0, "total_size": 0} for ext in exts_to_track}

# 遍历所有文件
for root, dirs, files in os.walk(target_dir):
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in file_stats:
            full_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(full_path)
                file_stats[ext]["count"] += 1
                file_stats[ext]["total_size"] += file_size
            except Exception as e:
                print(f"Error reading {file}: {e}")

# 输出统计结果
print(f"\n📊 文件类型统计结果（单位：MB）：\n{'-'*40}")
for ext, stats in file_stats.items():
    size_mb = stats["total_size"] / (1024 * 1024)
    print(f"{ext:<6} → 数量: {stats['count']:>4}，总大小: {size_mb:.2f} MB")
