import random
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_lx8or2ne = self.__tk_label_lx8or2ne(self)
        self.tk_label_lx8p3vie = self.__tk_label_lx8p3vie(self)
        self.tk_input_lx8p3406 = self.__tk_input_lx8p3406(self)
        self.tk_label_lx8p4ht2 = self.__tk_label_lx8p4ht2(self)
        self.tk_input_lx8p6a91 = self.__tk_input_lx8p6a91(self)
        self.tk_label_lx8p9f6z = self.__tk_label_lx8p9f6z(self)
        self.identities = IntVar()  # 创建一个IntVar变量来保存单选按钮的状态 身份1用户2管理员
        self.tk_radio_button_lx8pbcbn = self.__tk_radio_button_lx8pbcbn(self)
        self.tk_radio_button_lx8pecky = self.__tk_radio_button_lx8pecky(self)
        self.tk_button_lx8oosjo = self.__tk_button_lx8oosjo(self)
        self.tk_button_lx8p7ka9 = self.__tk_button_lx8p7ka9(self)

    def __win(self):
        self.title("app评论分析系统")
        # 设置窗口大小、居中
        width = 600
        height = 500
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

    def __tk_label_lx8or2ne(self, parent):
        label = Label(parent, text="登录与注册", anchor="center", )
        label.place(x=200, y=70, width=214, height=30)
        return label

    def __tk_label_lx8p3vie(self, parent):
        label = Label(parent, text="账号", anchor="center", )
        label.place(x=140, y=150, width=50, height=30)
        return label

    def __tk_input_lx8p3406(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=240, y=150, width=200, height=30)
        return ipt

    def __tk_label_lx8p4ht2(self, parent):
        label = Label(parent, text="密码", anchor="center", )
        label.place(x=140, y=210, width=50, height=30)
        return label

    def __tk_input_lx8p6a91(self, parent):
        ipt = Entry(parent, show="*")  # 密码输入框显示为星号
        ipt.place(x=240, y=210, width=200, height=30)
        return ipt

    def __tk_label_lx8p9f6z(self, parent):
        label = Label(parent, text="身份", anchor="center", )
        label.place(x=140, y=270, width=50, height=30)
        return label

    def __tk_radio_button_lx8pbcbn(self, parent):
        rb = Radiobutton(parent, text="用户", variable=self.identities, value=1)
        rb.place(x=240, y=270, width=80, height=30)
        return rb

    def __tk_radio_button_lx8pecky(self, parent):
        rb = Radiobutton(parent, text="管理员", variable=self.identities, value=2)
        rb.place(x=360, y=270, width=80, height=30)
        return rb

    def __tk_button_lx8oosjo(self, parent):
        btn = Button(parent, text="登录", takefocus=False, )
        btn.place(x=190, y=380, width=50, height=30)
        return btn

    def __tk_button_lx8p7ka9(self, parent):
        btn = Button(parent, text="注册", takefocus=False, )
        btn.place(x=365, y=380, width=50, height=30)
        return btn

    def get_username(self):
        return self.tk_input_lx8p3406.get()

    def get_password(self):
        return self.tk_input_lx8p6a91.get()

    def get_identity(self):
        return self.identities.get()


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def __event_bind(self):
        self.tk_button_lx8oosjo.bind('<Button-1>', self.ctl.login)
        self.tk_button_lx8p7ka9.bind('<Button-1>', self.ctl.register)

    def __style_config(self):
        pass


class Controller:
    def init(self, win):
        self.win = win

    def login(self, event):
        messagebox.showinfo('提示', message="登录成功")
        username = self.win.get_username()
        password = self.win.get_password()
        identity = self.win.get_identity()
        # 假设验证成功
        if username and password:
            print(f"登录信息: 账号={username}, 密码={password}, 身份={'用户' if identity == 1 else '管理员'}")
            self.show_main_app()
        else:
            print("登录失败")

    def register(self, event):
        messagebox.showinfo('提示', message="注册成功")
        username = self.win.get_username()
        password = self.win.get_password()
        identity = self.win.get_identity()
        # 假设注册成功
        if username and password:
            print(f"注册信息: 账号={username}, 密码={password}, 身份={'用户' if identity == 1 else '管理员'}")
            self.show_main_app()
        else:
            print("注册失败")

    def show_main_app(self):
        self.win.withdraw()  # 隐藏当前窗口
        main_app = MainApp(self.win)
        main_app.mainloop()

    def s1(self, event):
        print("关注该app按钮被点击")

    def s2(self, event):
        print("取消关注该app按钮被点击")

    def s3(self, event):
        print("查询该app近况按钮被点击")


class MainApp(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = controller
        self.__win()
        self.tk_label_已关注的app = self.__tk_label_已关注的app(self)
        self.tk_text_输入app = self.__tk_text_输入app(self)
        self.tk_button_关注该app = self.__tk_button_关注该app(self)
        self.tk_button_取消关注该app = self.__tk_button_取消关注该app(self)
        self.tk_label_展示颗粒度选择 = self.__tk_label_展示颗粒度选择(self)
        self.particle_size = IntVar()  # 设置颗粒度1年2月3周
        self.tk_radio_button_年 = self.__tk_radio_button_年(self)
        self.tk_radio_button_月 = self.__tk_radio_button_月(self)
        self.tk_radio_button_周 = self.__tk_radio_button_周(self)
        self.tk_button_查询该app近况 = self.__tk_button_查询该app近况(self)
        self.__event_bind()


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
        rb = Radiobutton(parent, text="年", variable=self.particle_size, value=1)
        rb.place(x=100, y=230, width=60, height=30)
        return rb

    def __tk_radio_button_月(self, parent):
        rb = Radiobutton(parent, text="月", variable=self.particle_size, value=2)
        rb.place(x=100, y=260, width=60, height=30)
        return rb

    def __tk_radio_button_周(self, parent):
        rb = Radiobutton(parent, text="周", variable=self.particle_size, value=3)
        rb.place(x=100, y=290, width=60, height=30)
        return rb

    def __tk_button_查询该app近况(self, parent):
        btn = Button(parent, text="查询该app近况", takefocus=False, )
        btn.place(x=320, y=240, width=100, height=40)
        return btn

    def __event_bind(self):
        self.tk_button_关注该app.bind('<Button-1>', self.controller.s1)
        self.tk_button_取消关注该app.bind('<Button-1>', self.controller.s2)
        self.tk_button_查询该app近况.bind('<Button-1>', self.controller.s3)


if __name__ == "__main__":
    controller = Controller()
    win = Win(controller)
    win.mainloop()
