"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import random
from tkinter import *
from tkinter.ttk import *


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_已关注的app = self.__tk_label_已关注的app(self)
        self.tk_text_输入app = self.__tk_text_输入app(self)
        self.tk_button_关注该app = self.__tk_button_关注该app(self)
        self.tk_button_取消关注该app = self.__tk_button_取消关注该app(self)
        self.tk_label_展示颗粒度选择 = self.__tk_label_展示颗粒度选择(self)
        self.tk_radio_button_年 = self.__tk_radio_button_年(self)
        self.tk_radio_button_月 = self.__tk_radio_button_月(self)
        self.tk_radio_button_周 = self.__tk_radio_button_周(self)
        self.tk_button_查询该app近况 = self.__tk_button_查询该app近况(self)

    def __win(self):
        self.title("用户界面")
        # 设置窗口大小、居中
        width = 600
        height = 400
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.resizable(width=False, height=False)

    def scrollbar_autohide(self, vbar, hbar, widget):
        """自动隐藏滚动条"""

        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)

        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)

        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())

    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')

    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')

    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def __tk_label_已关注的app(self, parent):
        label = Label(parent, text="已关注的app:", anchor="center", )
        label.place(x=100, y=60, width=90, height=30)
        return label

    def __tk_text_输入app(self, parent):
        text = Text(parent)
        text.place(x=100, y=120, width=150, height=30)
        return text

    def __tk_button_关注该app(self, parent):
        btn = Button(parent, text="关注该app", takefocus=False, )
        btn.place(x=320, y=90, width=83, height=30)
        return btn

    def __tk_button_取消关注该app(self, parent):
        btn = Button(parent, text="取消关注该app", takefocus=False, )
        btn.place(x=320, y=140, width=96, height=30)
        return btn

    def __tk_label_展示颗粒度选择(self, parent):
        label = Label(parent, text="展示颗粒度选择", anchor="center", )
        label.place(x=100, y=190, width=104, height=30)
        return label

    def __tk_radio_button_年(self, parent):
        rb = Radiobutton(parent, text="年", )
        rb.place(x=100, y=230, width=60, height=30)
        return rb

    def __tk_radio_button_月(self, parent):
        rb = Radiobutton(parent, text="月", )
        rb.place(x=100, y=260, width=60, height=30)
        return rb

    def __tk_radio_button_周(self, parent):
        rb = Radiobutton(parent, text="周", )
        rb.place(x=100, y=290, width=60, height=30)
        return rb

    def __tk_button_查询该app近况(self, parent):
        btn = Button(parent, text="查询该app近况", takefocus=False, )
        btn.place(x=320, y=240, width=100, height=40)
        return btn


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def __event_bind(self):
        self.tk_button_关注该app.bind('<Button-1>', self.ctl.s1)
        self.tk_button_取消关注该app.bind('<Button-1>', self.ctl.s2)
        self.tk_button_查询该app近况.bind('<Button-1>', self.ctl.s3)

    def __style_config(self):
        pass


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()
