import os

# 定义要处理的文件夹路径
input_folder = 'image_without_encrypt'  # 替换为你的输入文件夹路径
# 定义输出文件夹路径
output_folder = 'image1'  # 还原后的文件保存路径

# 确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)

# 遍历输入文件夹中的所有文件
for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.lower().endswith('.png'):  # 只处理 PNG 文件
            modified_file_path = os.path.join(root, file)

            # 读取 PNG 文件并获取其 HEX 数据
            with open(modified_file_path, 'rb') as f:
                hex_data = f.read().hex()

            # 将 HEX 数据转换为字节数组
            byte_array = bytearray.fromhex(hex_data)

            # 恢复被删除的字节
            mid_index = len(byte_array) // 2
            if len(byte_array) % 2 == 0:  # 偶数个字节
                byte_array.insert(mid_index - 1, 0x00)  # 插入一个字节
            else:  # 奇数个字节
                byte_array.insert(mid_index, 0x00)  # 插入一个字节

            # 恢复交换的字节
            if len(byte_array) >= 3:  # 确保字节数组至少有三个字节
                byte_array[1], byte_array[2] = byte_array[2], byte_array[1]  # 交换第二和第三个字节

            # 定义输出文件的相对路径
            relative_path = os.path.relpath(root, input_folder)
            output_path = os.path.join(output_folder, relative_path)

            # 确保输出子文件夹存在
            os.makedirs(output_path, exist_ok=True)

            # 定义还原后的文件路径
            restored_file_path = os.path.join(output_path, 'restored_' + file)

            # 将还原后的字节数组写回到文件
            with open(restored_file_path, 'wb') as restored_file:
                restored_file.write(byte_array)

            print(f"还原后的文件已保存到: {restored_file_path}")
