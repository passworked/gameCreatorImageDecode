import os

# 定义要处理的文件夹路径
input_folder = 'decode_image'  # 替换为你的输入文件夹路径
# 定义输出文件夹路径
output_folder = 'dddecode_image'

# 确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)

# 遍历输入文件夹中的所有文件
for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.lower().endswith('.png'):  # 只处理 PNG 文件
            png_file_path = os.path.join(root, file)

            # 读取 PNG 文件并获取其 HEX 数据
            with open(png_file_path, 'rb') as f:
                hex_data = f.read().hex()

            # 将 HEX 数据转换为字节数组
            byte_array = bytearray.fromhex(hex_data)

            # 清除位于 1/2 地址的一个 HEX 字节
            if len(byte_array) > 1:
                if len(byte_array) % 2 == 0:  # 偶数个字节
                    del byte_array[len(byte_array) // 2 - 1]  # 删除索引加 1 的字节
                else:  # 奇数个字节
                    del byte_array[len(byte_array) // 2]  # 删除该字节

            # 定义输出文件的相对路径
            relative_path = os.path.relpath(root, input_folder)
            output_path = os.path.join(output_folder, relative_path)

            # 确保输出子文件夹存在
            os.makedirs(output_path, exist_ok=True)

            # 定义修改后的文件路径
            modified_file_path = os.path.join(output_path, 'modified_' + file)

            # 将修改后的字节数组写回到文件
            with open(modified_file_path, 'wb') as modified_file:
                modified_file.write(byte_array)

            print(f"修改后的文件已保存到: {modified_file_path}")
