import tkinter as tk  # 导入 tkinter 库，用于创建图形用户界面
import keyboard  # 导入 keyboard 库，用于监听键盘事件
from gbk_to_decimal import gbk  # 导入自定义的 gbk 转换函数
from input_validator import validate_gbk_input  # 导入输入验证函数
import threading  # 导入 threading 库，用于启动新线程
from output import simulate_input  # 导入新添加的 output 模块

def on_submit(input_entry, output_text, error_label, event=None):
    """
    处理回车键按下后用户输入的提交操作
    """
    user_input = input_entry.get()  # 获取输入框的文本内容
    if not user_input.strip():  # 检查输入内容是否为空
        error_label.config(text="输入不能为空")  # 显示错误信息
        return  # 结束函数，避免进一步处理

    # 调用输入验证函数，检查是否符合 GBK 编码规范
    validation_error = validate_gbk_input(user_input)
    if validation_error:
        error_label.config(text=validation_error)  # 如果输入无效，显示错误信息
    else:
        error_label.config(text="")  # 清除错误提示
        output_text.configure(state=tk.NORMAL)  # 重新启用输出框，以便插入新的输出内容
        # 调用 GBK 转换函数，获取十进制编码
        gbk_output = gbk(user_input)

        # 将用户输入和转换后的 GBK 十进制值插入到输出框
        output_text.insert(tk.END, f"输入: {user_input}\nGBK10进制: {gbk_output}\n")
        output_text.configure(state=tk.DISABLED)  # 禁用输出框编辑功能
        # 自动滚动到最底部，确保显示最新的内容
        output_text.see(tk.END)
        input_entry.delete(0, tk.END)  # 清空输入框内容

        # 调用 output 模块，模拟按下 Alt 和 GBK 输出
        simulate_input(gbk_output)

def listen_for_enter_key(input_entry, output_text, error_label):
    """
    监听回车键事件，在按下回车时，获取输入框的内容并触发提交。
    """
    keyboard.add_hotkey('enter', lambda: on_submit(input_entry, output_text, error_label))  # 将回车键与 on_submit 函数绑定
    keyboard.wait()  # 阻塞主线程，直到程序退出

def show_output_and_input():
    # 创建主窗口，并显示免责声明
    disclaimer = ("本软件仅供用户自行使用，作者不对使用本软件可能导致的任何后果承担法律责任\n"
                  "用户应充分知晓并理解，使用本软件可能面临的风险，例如2025年2月22日发生的黎明杀机中文插件EAC误封事件\n"
                  "用户使用本软件的行为，视为已完全理解并接受上述风险\n"
                  "作者:Yoru \n"
                  "本软件遵循GNU通用公共许可证（GPL）协议开源\n"
                  "本软件GitHub地址:https://github.com/Yoruuuuuusama/DBD_CN_INPUT\n"
                  "使用教程:在软件中输入文字后，点击游戏内输入框并按回车键即可输入")

    root = tk.Tk()  # 创建 Tkinter 窗口实例
    root.title("中文插件")  # 设置窗口标题

    # 创建输出文本框，显示处理结果
    output_text = tk.Text(root, wrap=tk.WORD, height=15, width=50)
    output_text.pack(padx=10, pady=10)  # 添加到窗口，并设置边距

    # 创建输入框，用户在此输入数据
    input_entry = tk.Entry(root, width=50)
    input_entry.insert(0, "")  # 默认提示文字为空
    input_entry.pack(padx=10, pady=5)  # 添加到窗口，并设置边距
    input_entry.focus_set()  # 设置输入框为焦点，使其可输入

    # 创建错误提示标签，用于显示输入错误信息
    error_label = tk.Label(root, fg="red")
    error_label.pack(pady=5)  # 添加到窗口，并设置垂直边距

    output_text.insert(tk.END, disclaimer)  # 将免责声明内容插入到输出文本框
    output_text.configure(state=tk.DISABLED)  # 禁用文本框的编辑功能，防止用户修改

    # 创建一个提交按钮，当点击时触发处理函数
    submit_button = tk.Button(root, text="提交", command=lambda: on_submit(input_entry, output_text, error_label))
    submit_button.pack(pady=5)  # 添加到窗口，并设置垂直边距

    # 创建一个关闭按钮，点击时关闭窗口
    close_button = tk.Button(root, text="关闭", command=root.destroy)
    close_button.pack(pady=10)  # 添加到窗口，并设置垂直边距

    # 启动新线程，开始监听回车键按下事件
    listener_thread = threading.Thread(target=listen_for_enter_key, args=(input_entry, output_text, error_label), daemon=True)
    listener_thread.start()  # 设置为守护线程，主程序退出时线程也会自动结束

    # 启动 Tkinter 主循环，显示窗口并等待用户操作
    root.mainloop()

# 主程序入口
if __name__ == "__main__":
    show_output_and_input()  # 调用主函数，启动程序
