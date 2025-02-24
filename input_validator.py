def validate_gbk_input(user_input):
    """
    验证用户输入是否符合GBK编码范围。
    如果输入包含不在GBK编码范围内的字符，返回错误信息。
    如果输入合法，返回 None。
    """
    invalid_characters = []  # 用于存储不在GBK编码范围内的字符

    # 遍历用户输入的每个字符
    for character in user_input:
        try:
            character.encode("gbk")  # 尝试将字符编码为GBK
        except UnicodeEncodeError:  # 如果编码失败，捕获异常
            invalid_characters.append(character)  # 将无效字符添加到列表

    # 检查是否发现无效字符
    if invalid_characters:
        return f"以下字符不在GBK编码范围内，请重新输入：\n{''.join(invalid_characters)}"
    else:
        return None  # 输入合法
