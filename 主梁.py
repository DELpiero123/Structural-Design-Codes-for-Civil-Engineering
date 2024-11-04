import tkinter as tk
from tkinter import scrolledtext  # 使用scrolledtext而不是简单的Text，以便自动滚动
from math import sqrt

# 定义全局变量
a1 = 1.0
h0 = 546.0
fc = 14.3
fy = 360.0
b = 300.0
bf = 2300  # 注意：这里bf应该是整数或浮点数，确保类型一致性


def calculate():
    try:
        M = float(entry_M.get()) * 1000000.0  # 转换为MNm
        if M < 0:
            as_ = -1.0 * M / (a1 * fc * b * h0 * h0)
        else:
            as_ = M / (a1 * fc * bf * h0 * h0)

        γ = (1.0 + sqrt(1.0 - 2.0 * as_)) / 2 if 2.0 * as_ < 1.0 else 1.0  # 确保根号内非负
        As = M / (γ * fy * h0)

        # 创建一个新的Toplevel窗口来显示结果
        result_window = tk.Toplevel(root)
        result_window.title("计算结果")
        result_window.geometry("300x200")  # 可以根据需要调整大小

        # 使用scrolledtext控件来显示可复制的结果
        result_text = scrolledtext.ScrolledText(result_window, wrap=tk.WORD)
        result_text.insert(tk.END, f"as={as_:.6f}\nγ={γ:.6f}\nAs={As:.6f}")
        result_text.config(state='disabled')  # 禁用编辑，只显示结果
        result_text.pack(padx=10, pady=10)

    except ValueError:
        tk.messagebox.showerror("输入错误", "请输入有效的弯矩设计值")

    # 创建主窗口


root = tk.Tk()
root.title("主梁弯矩设计值计算器")

# 设置窗口大小
root.geometry("300x200")

# 创建输入框和标签
label_M = tk.Label(root, text="主梁弯矩设计值M(kNm):")
label_M.pack(pady=5)
entry_M = tk.Entry(root)
entry_M.pack(pady=5)

# 创建计算按钮
button_calculate = tk.Button(root, text="计算", command=calculate)
button_calculate.pack(pady=10)

# 创建退出按钮
button_exit = tk.Button(root, text="退出", command=root.quit)
button_exit.pack(pady=10)

# 启动事件循环
root.mainloop()