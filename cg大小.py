import os
import csv

# 设置要读取的文件夹路径
folder_path = 'discrypt_image\事件\cg'  # 替换为您的文件夹路径

# 创建一个空列表来存储文件信息
file_data = []

# 遍历文件夹内的文件
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):  # 确保是文件而不是文件夹
        file_size_bytes = os.path.getsize(file_path)  # 获取文件大小（字节）
        file_size_kb = file_size_bytes / 1024  # 转换为 KB
        file_data.append([filename, f"{file_size_kb:.2f} KB"])  # 将文件名和大小添加到列表，保留两位小数

# 设置输出的 CSV 文件路径
output_csv_path = './cg大小.csv'  # 替换为您想保存的路径

# 写入 CSV 文件
with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['文件名', '文件大小 (KB)'])  # 写入表头
    csv_writer.writerows(file_data)  # 写入文件信息

print(f"CSV 文件已生成：{output_csv_path}")
