# output.py

import keyboard
import time

def simulate_input(gbk_output):
    """
    模拟按下键盘按键，按顺序输入每个字符的 GBK 编码
    """
    for decimal_value in gbk_output:
        try:
            # 处理 GBK 编码的字符
            if decimal_value < 256:
                # 对于单字节字符，直接解码
                char = bytes([decimal_value]).decode('gbk')
                keyboard.write(char)  # 模拟键盘输入字符
                time.sleep(0.1)  # 延迟以便于模拟输入
            else:
                # 对于多字节字符，需要进行双字节的处理
                byte1 = decimal_value >> 8  # 高字节
                byte2 = decimal_value & 0xFF  # 低字节
                char = bytes([byte1, byte2]).decode('gbk')  # 解码为 GBK 字符
                keyboard.write(char)  # 模拟键盘输入字符
                time.sleep(0.2)  # 延迟
        except (UnicodeDecodeError, ValueError) as e:
            print(f"Error decoding GBK value {decimal_value}: {e}")
