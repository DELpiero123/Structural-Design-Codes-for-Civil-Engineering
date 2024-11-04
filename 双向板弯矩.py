# 此代码已经上传到我的GitHub个人空间，老师若想查看请联系我
# 作者：刘博 土木21-2 202110606014
import tkinter as tk
from tkinter import messagebox

def calculate_moments():
    try:
        m1 = float(entry_m1.get())
        m2 = float(entry_m2.get())
        mj1 = float(entry_mj1.get())
        mj2 = float(entry_mj2.get())
        l01 = float(entry_l01.get())

        M1 = (m1 + 0.2 * m2) * 7.374 * l01 * l01 + (mj1 + 0.2 * mj2) * 0.51 * l01 * l01
        M2 = (m2 + 0.2 * m1) * 7.374 * l01 * l01 + (mj2 + 0.2 * mj1) * 0.51 * l01 * l01

        result_label.config(text=f"M1: {M1}\nM2: {M2}")
    except ValueError:
        messagebox.showerror("输入错误", "请输入有效的数字！")

def on_button_click():
    if messagebox.askyesno("确认退出", "确定要退出吗？"):
        root.destroy()

# 创建主窗口
root = tk.Tk()
root.title("力矩计算")

# 创建输入框和标签
label_m1 = tk.Label(root, text="m1:")
label_m1.grid(row=0, column=0)
entry_m1 = tk.Entry(root)
entry_m1.grid(row=0, column=1)

label_m2 = tk.Label(root, text="m2:")
label_m2.grid(row=1, column=0)
entry_m2 = tk.Entry(root)
entry_m2.grid(row=1, column=1)

label_mj1 = tk.Label(root, text="简支mj1:")
label_mj1.grid(row=2, column=0)
entry_mj1 = tk.Entry(root)
entry_mj1.grid(row=2, column=1)

label_mj2 = tk.Label(root, text="简支mj2:")
label_mj2.grid(row=3, column=0)
entry_mj2 = tk.Entry(root)
entry_mj2.grid(row=3, column=1)

label_l01 = tk.Label(root, text="l01:")
label_l01.grid(row=4, column=0)
entry_l01 = tk.Entry(root)
entry_l01.grid(row=4, column=1)

# 创建结果标签
result_label = tk.Label(root, text="", width=30, height=5)
result_label.grid(row=5, column=0, columnspan=2)

# 创建计算按钮
calculate_button = tk.Button(root, text="计算", command=calculate_moments)
calculate_button.grid(row=6, column=0)

# 创建退出按钮
exit_button = tk.Button(root, text="退出", command=on_button_click)
exit_button.grid(row=6, column=1)

# 运行主循环
root.mainloop()
