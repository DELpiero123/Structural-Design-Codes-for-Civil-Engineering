import tkinter as tk
from tkinter import messagebox
from math import sqrt


def calculate():
    try:
        M = float(entry_M.get()) * 1000000.0  # 转换为MNm  
        if M < 0:
            a_ = -1.0 * M / (a1 * fc * b * h0 * h0)
        else:
            a_ = M / (a1 * fc * bf * h0 * h0)
        ξ = 1.0 - sqrt(1.0 - 2.0 * a_)
        if M < 0:
            As = ξ * b * h0 * a1 * fc / fy
        else:
            As = ξ * bf * h0 * a1 * fc / fy

            # 创建一个新的Toplevel窗口来显示结果
        result_window = tk.Toplevel(root)
        result_window.title("计算结果")
        result_window.geometry("300x150")

        # 使用Text控件来显示可复制的结果  
        result_text = tk.Text(result_window, height=5, wrap=tk.WORD)
        result_text.insert(tk.END, f"as={a_:.6f}\nξ={ξ:.6f}\nAs={As:.6f}")
        result_text.config(state='disabled')  # 禁用编辑，只显示结果  
        result_text.pack(padx=10, pady=10)

    except ValueError:
        messagebox.showerror("输入错误", "请输入有效的弯矩设计值")

    # 定义全局变量


a1 = 1.0
h0 = 460.0
fc = 14.3
ft = 1.43
fy = 360.0
fyv = 360.0
b = 200
bf = 1160

# 创建主窗口  
root = tk.Tk()
root.title("次梁弯矩设计值计算器")
root.geometry("400x200")

# 创建输入框和标签  
label_M = tk.Label(root, text="次梁弯矩设计值M(kNm):")
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
