
# 📦 wordCompress

一个用于压缩 `.docx` Word 文件中嵌入图像体积的自动化工具包。通过解压 `.docx` 文件、分析 `media/` 目录中 `.tif` 和 `.png` 图像体积，执行有损/无损压缩，并恢复为 Word 文档，实现大幅减少 Word 文件体积，**适用于学位论文/技术文档场景的文件大小限制需求**。

---

## 🚀 功能亮点

- 📁 将 `.docx` 文件转换为可处理的 `.zip` 目录结构
- 📊 统计 `word/media/` 路径下各类图像体积和数量
- 📉 对 `.tif`、`.png` 图像执行压缩（默认无损、可配置）
- 🔄 支持自动图像重采样（缩放最大宽度）
- ✅ 原路径覆盖保存，无需修改 Word XML 引用
- 📦 自动重新打包为 `.docx`，一键还原文档结构

---

## 📂 项目结构

```
wordCompress/
├── fileTypeAnalysis.py      # 文件类型体积统计
├── tif_png_compress.py      # tif 和 png 压缩主脚本
├── docxRecover.py           # docx 文件结构还原压缩
├── example/                 # 示例文档解压目录（包含 word/media）
└── README.md                # 仓库说明文件
```

---

## 📦 使用指南

### 1️⃣ 将 `.docx` 转为 `.zip` 并解压

```bash
cp example.docx example.zip
unzip example.zip -d example/
```

### 2️⃣ 执行文件体积分析

```bash
python fileTypeAnalysis.py
```

### 3️⃣ 执行 `.tif` 和 `.png` 图像压缩（无损压缩）

```bash
python tif_png_compress.py
```

> ✅ 支持自动缩放图像宽度到 `max_width`，并覆盖原路径

### 4️⃣ 执行 Word 还原打包为 `.docx`

```bash
python docxRecover.py
```

---

## 📊 效果评估示例

| 文件类型 | 压缩前 | 压缩后 | 减少比例 |
|----------|--------|--------|-----------|
| `.tif`   | 31.44 MB | ~27.38 MB | ~12.9% |
| `.png`   | 25.84 MB | ~7.44 MB | ~71.05% |
| `.docx` 总体 | ~62.3 MB | ~38.4 MB | ✅ 达成减半目标 |

---

## 📎 依赖环境

- Python ≥ 3.6
- Pillow 图像处理库

```bash
pip install pillow
```

---

## 📌 应用场景

- 🎓 毕业论文、硕博学位文档体积超限
- 📝 科研/工程文档图像多、图片嵌入多
- 📤 邮件传输、系统上传有文件大小限制
- 🧼 清理冗余图像/压缩空间避免图像撑大文档

---

## 💡 TODOs

- [ ] 添加 `.wmf → .png` 批处理支持
- [ ] 添加命令行参数与日志记录
- [ ] 增加 GUI 操作界面

---

## ⭐ 开源地址

欢迎使用、改进与贡献本工具：

👉 [https://github.com/JOYUAGV/wordCompress](https://github.com/JOYUAGV/wordCompress)

欢迎 Star！🚀
