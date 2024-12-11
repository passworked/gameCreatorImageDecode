import os

# 定义要处理的文件夹路径
folder_path = 'discrypt_image'  # 替换为你的文件夹路径

# 遍历文件夹中的所有文件
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.lower().endswith('.png') and file.startswith('modified_'):  # 只处理以 modified_ 开头的 PNG 文件
            # 生成新的文件名，去掉 modified_ 前缀
            new_file_name = file[len('modified_'):]  # 去掉前缀
            # 生成完整的旧文件路径和新文件路径
            old_file_path = os.path.join(root, file)
            new_file_path = os.path.join(root, new_file_name)

            # 重命名文件
            os.rename(old_file_path, new_file_path)
            print(f"重命名: {old_file_path} -> {new_file_path}")
