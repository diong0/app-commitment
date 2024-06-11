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
        self.tk_label_修改前账号 = self.__tk_label_修改前账号(self)
        self.tk_label_修改前密码 = self.__tk_label_修改前密码(self)
        self.tk_label_修改前关注app = self.__tk_label_修改前关注app(self)
        self.tk_label_修改为 = self.__tk_label_修改为(self)
        self.tk_text_修改后账号 = self.__tk_text_修改后账号(self)
        self.tk_text_修改后密码 = self.__tk_text_修改后密码(self)
        self.tk_text_修改后关注app = self.__tk_text_修改后关注app(self)
        self.tk_button_修改按钮 = self.__tk_button_修改按钮(self)
        self.tk_button_不修改按钮 = self.__tk_button_不修改按钮(self)
    def __win(self):
        self.title("用户情况")
        # 设置窗口大小、居中
        width = 600
        height = 400
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.resizable(width=False, height=False)

    def scrollbar_autohide(self,vbar, hbar, widget):
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

    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_label_修改前账号(self,parent):
        label = Label(parent,text="账号:",anchor="center", )
        label.place(x=70, y=100, width=50, height=30)
        return label
    def __tk_label_修改前密码(self,parent):
        label = Label(parent,text="密码:",anchor="center", )
        label.place(x=220, y=100, width=50, height=30)
        return label
    def __tk_label_修改前关注app(self,parent):
        label = Label(parent,text="关注的app:",anchor="center", )
        label.place(x=375, y=100, width=70, height=30)
        return label
    def __tk_label_修改为(self,parent):
        label = Label(parent,text="修改为",anchor="center", )
        label.place(x=70, y=152, width=50, height=30)
        return label
    def __tk_text_修改后账号(self,parent):
        text = Text(parent)
        text.place(x=80, y=200, width=100, height=30)
        return text
    def __tk_text_修改后密码(self,parent):
        text = Text(parent)
        text.place(x=230, y=200, width=100, height=30)
        return text
    def __tk_text_修改后关注app(self,parent):
        text = Text(parent)
        text.place(x=380, y=200, width=100, height=30)
        return text
    def __tk_button_修改按钮(self,parent):
        btn = Button(parent, text="修改", takefocus=False,)
        btn.place(x=200, y=320, width=50, height=30)
        return btn
    def __tk_button_不修改按钮(self,parent):
        btn = Button(parent, text="不修改", takefocus=False,)
        btn.place(x=349, y=320, width=50, height=30)
        return btn
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_button_修改按钮.bind('<Button-1>',self.ctl.修改按钮)
        self.tk_button_不修改按钮.bind('<Button-1>',self.ctl.不修改按钮)
        pass
    def __style_config(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()