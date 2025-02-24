def gbk(user_input=""):
    # 创建一个空列表，存储每个字符的 GBK 编码的十进制表示
    user_input_list = []

    # 遍历用户输入的每个字符
    for character in user_input:
        #  将当前字符编码为 GBK 格式的字节序列,并转换为十六进制字符串
        hex_gbk_encoded = character.encode("gbk")
        hex_gbk_encoded = hex_gbk_encoded.hex()

        # 将十六进制字符串转换为十进制整数
        decimal_gbk_encoded = int(hex_gbk_encoded, 16)

        # 将用户输入储存到列表
        user_input_list.append(decimal_gbk_encoded)

    # 去除掉列表中值为 10 的元素
    while 10 in user_input_list:
        user_input_list.remove(10)

    return user_input_list
