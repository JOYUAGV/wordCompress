import zipfile
import os

def zip_dir_to_docx(src_dir, output_docx):
    with zipfile.ZipFile(output_docx, 'w', zipfile.ZIP_DEFLATED) as docx_zip:
        for foldername, subfolders, filenames in os.walk(src_dir):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                arcname = os.path.relpath(file_path, src_dir)
                docx_zip.write(file_path, arcname)
    print(f"[✓] 成功打包为 {output_docx}")

# 修改路径为你自己的
zip_dir_to_docx(
    src_dir=r"./example/",      # 该目录必须是包含 [Content_Types].xml 的目录
    output_docx= r"./example-comp.docx"
)
