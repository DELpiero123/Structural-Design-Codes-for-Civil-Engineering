# 此代码已经上传到我的GitHub个人空间，老师若想查看请联系我
# 作者：刘博 土木21-2 202110606014
import tkinter as tk
from tkinter import messagebox
# 定义全局变量
a1 = 1.0
h0 = 60.0
fc = 14.3
fy = 270.0
b = 1000.0
def calculate():
    global a1, h0, fc, fy, b  # 声明全局变量
    try:
        M = float(entry_M.get()) * 1000000
        as_ = M / (a1 * fc * b * h0 * h0)
        ξ = 1.0 - (1.0 - 2.0 * as_) ** 0.5
        As = ξ * b * h0 * a1 * fc / fy
        messagebox.showinfo("结果", f"as={as_:.6f}\nξ={ξ:.6f}\nAs={As:.6f}")
    except ValueError:
        messagebox.showerror("错误", "请输入有效的弯矩设计值")
# 创建主窗口
root = tk.Tk()
root.title("弯矩计算器")
# 设置窗口大小
root.geometry("300x150")
# 创建输入框和标签
label_M = tk.Label(root, text="弯矩设计值(kN/m):")
label_M.pack(pady=5)
entry_M = tk.Entry(root)
entry_M.pack(pady=5)
# 创建计算按钮
button_calculate = tk.Button(root, text="计算", command=calculate)
button_calculate.pack(pady=5)
# 启动事件循环
root.mainloop()