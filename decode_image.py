import os
import shutil

def modify_png_header(file_path):
    # 定义新的 PNG 文件头
    new_header = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
    
    # 读取原始文件
    with open(file_path, "rb") as f:
        data = f.read()
    
    # 修改文件头
    modified_data = new_header + data[8:]  # 保留原数据，从第 9 个字节开始

    return modified_data

def process_directory(src_dir, dest_dir):
    # 遍历源目录
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.lower().endswith('.png'):
                src_file_path = os.path.join(root, file)
                
                # 修改 PNG 文件头
                modified_data = modify_png_header(src_file_path)
                
                # 计算目标文件路径
                relative_path = os.path.relpath(root, src_dir)
                dest_folder = os.path.join(dest_dir, relative_path)
                
                # 创建目标文件夹（如果不存在）
                os.makedirs(dest_folder, exist_ok=True)

                # 保存修改后的文件
                dest_file_path = os.path.join(dest_folder, file)
                with open(dest_file_path, "wb") as f:
                    f.write(modified_data)

                print(f"Processed: {src_file_path} -> {dest_file_path}")

# 使用示例
source_directory = r"./image"  # 替换为源文件夹路径
destination_directory = r"./decode_image"  # 替换为目标文件夹路径

process_directory(source_directory, destination_directory)
