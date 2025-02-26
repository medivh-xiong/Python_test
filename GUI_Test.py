from tkinter import *

window = Tk()
window.title("抢美团卷")
window.geometry("500x300")

def start():
    print("你点了一下按钮")

label = Label(window, text="请输入token:", font=("黑体", 20), relief="sunken")
label.pack()

button = Button(window, text="开始", command=start)
button.pack(anchor=SW)

window.mainloop()