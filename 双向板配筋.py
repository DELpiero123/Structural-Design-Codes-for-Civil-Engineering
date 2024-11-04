# 此代码已经上传到我的GitHub个人空间，老师若想查看请联系我
# 作者：刘博 土木21-2 202110606014
import tkinter as tk
from tkinter import simpledialog, StringVar


def calculate():
    # 初始值
    a1 = 1.0
    fc = 14.3
    fy = 270.0
    b = 1000.0

    # 用户输入
    M = float(simpledialog.askfloat("输入", "弯矩设计值(kN/m)：")) * 1000000.0
    h0 = float(simpledialog.askfloat("输入", "h0："))

    # 计算
    as_ = M / (a1 * fc * b * h0 * h0)
    YiPu = 1.0 - (1.0 - 2.0 * as_) ** 0.5
    As = YiPu * b * h0 * a1 * fc / fy

    # 显示结果
    result_var.set(f"as={as_:.4f}\nYiPu={YiPu:.4f}\nAs={As:.4f}")


# 创建主窗口
root = tk.Tk()
root.title("弯矩计算器")

# 创建用于显示结果的StringVar
result_var = StringVar()

# 创建输出结果的文本框
result_label = tk.Label(root, textvariable=result_var, height=5, wraplength=200)
result_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# 创建计算按钮
calculate_button = tk.Button(root, text="计算", command=calculate)
calculate_button.grid(row=1, column=1, padx=50, pady=10)

# （可选）添加一些说明或分隔
separator = tk.Label(root, text="-刘-博-制-作-", height=1)
separator.grid(row=2, column=0, columnspan=2, sticky='ew')

# 运行主循环
root.mainloop()