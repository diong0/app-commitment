import random
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import threading


from appstore.苹果 import fetch_comments
from huawei.huawei import scrape_app_comments
from googleplay.googleplay import scrape_google_play_reviews

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
        self.admin_win = None  # 添加对管理员窗口的引用

    # 主界面
    def login(self, event):
        username = self.win.get_username()
        password = self.win.get_password()
        identity = self.win.get_identity()
        # 假设验证成功
        if username and password:
            if identity == 1:
                messagebox.showinfo('提示', message="用户登录成功")
                print(f"登录信息: 账号={username}, 密码={password}, 身份=用户")
                self.show_main_app()
            elif identity == 2:
                messagebox.showinfo('提示', message="管理员登录成功")
                print(f"登录信息: 账号={username}, 密码={password}, 身份=管理员")
                self.show_admin_app()
        else:
            messagebox.showerror('错误', message="登录失败")

    def register(self, event):
        username = self.win.get_username()
        password = self.win.get_password()
        identity = self.win.get_identity()
        # 假设注册成功
        if username and password:
            messagebox.showinfo('提示', message="注册成功")
            print(f"注册信息: 账号={username}, 密码={password}, 身份={'用户' if identity == 1 else '管理员'}")
            self.show_main_app()
        else:
            messagebox.showerror('错误', message="注册失败")

    def show_main_app(self):  # 主界面到用户界面
        self.win.withdraw()  # 隐藏当前窗口
        main_app = MainApp(self.win)
        main_app.mainloop()

    def show_admin_app(self):  # 主界面到管理员界面
        self.win.withdraw()  # 隐藏当前窗口
        admin_app = AdminApp(self.win, self)
        admin_app.mainloop()

    # 用户界面
    def s1(self, event):
        print("关注该app按钮被点击")

    def s2(self, event):
        print("取消关注该app按钮被点击")

    def s3(self, event):
        print("查询该app近况按钮被点击")

    # 管理员界面
    def 获取评论(self, event):
        print("获取最新评论按钮被点击")
        # 创建并启动线程
        threading.Thread(target=self.fetch_comments).start()

    def fetch_comments(self):
        comment = []
        comment.append(scrape_app_comments(appname="抖音"))
        comment.append(scrape_google_play_reviews(appname="抖音"))
        comment.append(fetch_comments(appname="抖音"))
        print(comment)
        # 更新UI时需要使用 `after` 方法确保线程安全
        self.win.after(0, self.update_ui_with_comments, comment)

    def update_ui_with_comments(self, comment):
        # 在这里更新UI，确保在主线程中执行
        print(comment)
        messagebox.showinfo('提示', message="最新评论获取成功")

    def 用户查询(self, event): # 进入用户情况界面
        print("设置该用户情况按钮被点击")
        admin_search = UserChange(self.admin_win, self)  # 传入管理员窗口引用
        admin_search.mainloop()

    def 评论查询(self, event):  # 进入评论查询
        print("管理员评论查询按钮被点击")
        # if self.admin_win:
        #    self.admin_win.withdraw()  # 确保admin_win被正确初始化后再调用withdraw
        admin_search = Search(self.admin_win, self)  # 传入管理员窗口引用
        admin_search.mainloop()

    def logout(self, event=None):
        # 关闭当前用户界面窗口
        self.win.destroy()
        # 重新创建一个新的登录/注册界面
        self.win = Win(self)
        self.win.mainloop()

    # 评论查询界面
    def 显示分词(self, event):
        print("显示分词按钮被点击")

    def 增加分词(self, event):
        print("增加分词按钮被点击")

    def 删除分词(self, event):
        print("删除分词按钮被点击")

    def 退出查询(self, event):
        print("退出查询按钮被点击")
        event.widget.master.destroy()  # 关闭查询窗口
        if self.admin_win:
            self.admin_win.deiconify()  # 重新显示管理员窗口

    # 管理员修改用户界面
    def 修改按钮(self, event):
        print("修改按钮被点击")
        event.widget.master.destroy()  # 关闭查询窗口
        if self.admin_win:
            self.admin_win.deiconify()  # 重新显示管理员窗口

    def 不修改按钮(self, event):
        print("不修改按钮被点击")
        event.widget.master.destroy()  # 关闭查询窗口
        if self.admin_win:
            self.admin_win.deiconify()  # 重新显示管理员窗口


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
        self.tk_button_查询具体评论 = self.__tk_button_查询具体评论(self)
        self.tk_button_查询该app近况 = self.__tk_button_查询该app近况(self)
        self.tk_button_退出登录 = self.__tk_button_退出登录(self)
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

    def __tk_button_查询具体评论(self, parent):
        btn = Button(parent, text="查询具体评论", takefocus=False, )
        btn.place(x=320, y=220, width=100, height=30)
        return btn

    def __tk_button_查询该app近况(self, parent):
        btn = Button(parent, text="查询该app近况", takefocus=False, )
        btn.place(x=320, y=290, width=100, height=30)
        return btn

    def __tk_button_退出登录(self, parent):
        btn = Button(parent, text="退出登录", takefocus=False, )
        btn.place(x=490, y=340, width=80, height=30)
        return btn

    def __event_bind(self):
        self.tk_button_关注该app.bind('<Button-1>', self.controller.s1)
        self.tk_button_取消关注该app.bind('<Button-1>', self.controller.s2)
        self.tk_button_查询具体评论.bind('<Button-1>', self.controller.评论查询)
        self.tk_button_查询该app近况.bind('<Button-1>', self.controller.s3)
        self.tk_button_退出登录.bind('<Button-1>', self.controller.logout)


class AdminApp(Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.__win()
        self.tk_button_获取最新评论 = self.__tk_button_获取最新评论(self)
        self.tk_button_设置该用户情况 = self.__tk_button_设置该用户情况(self)
        self.tk_button_评论查询 = self.__tk_button_评论查询(self)
        self.tk_input_app名 = self.__tk_input_app名(self)
        self.tk_label_输入app = self.__tk_label_输入app(self)
        self.tk_list_box_用户账户 = self.__tk_list_box_用户账户(self)
        self.tk_button_返回登录 = self.__tk_button_返回登录(self)
        self.__event_bind()

    def __win(self):
        self.title("管理员界面")
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

    def __tk_button_获取最新评论(self, parent):
        btn = Button(parent, text="获取最新评论", takefocus=False, )
        btn.place(x=240, y=100, width=90, height=30)
        return btn

    def __tk_button_设置该用户情况(self, parent):
        btn = Button(parent, text="设置该用户情况", takefocus=False, )
        btn.place(x=240, y=200, width=100, height=30)
        return btn

    def __tk_button_评论查询(self, parent):
        btn = Button(parent, text="评论查询", takefocus=False, )
        btn.place(x=440, y=100, width=60, height=30)
        return btn

    def __tk_input_app名(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=130, y=100, width=90, height=30)
        return ipt

    def __tk_label_输入app(self, parent):
        label = Label(parent, text="输入app", anchor="center", )
        label.place(x=60, y=100, width=50, height=30)
        return label

    def __tk_list_box_用户账户(self, parent):
        lb = Listbox(parent)
        lb.insert(END, "用户账户")
        lb.place(x=60, y=200, width=150, height=100)
        self.create_bar(parent, lb, True, True, 60, 200, 150, 100, 600, 400)
        return lb

    def __tk_button_返回登录(self, parent):
        btn = Button(parent, text="返回登录", takefocus=False, )
        btn.place(x=500, y=340, width=60, height=30)
        return btn

    def __event_bind(self):
        self.tk_button_获取最新评论.bind('<Button-1>', self.controller.获取评论)
        self.tk_button_设置该用户情况.bind('<Button-1>', self.controller.用户查询)
        self.tk_button_评论查询.bind('<Button-1>', self.controller.评论查询)
        self.tk_button_返回登录.bind('<Button-1>', self.controller.logout)


class Search(Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.admin_window = parent  # 保存管理员窗口引用
        self.__win()
        self.tk_label_输入查询时间 = self.__tk_label_输入查询时间(self)
        self.tk_select_box_选择年 = self.__tk_select_box_选择年(self)
        self.tk_label_标签年 = self.__tk_label_标签年(self)
        self.tk_select_box_选择月 = self.__tk_select_box_选择月(self)
        self.tk_label_标签月 = self.__tk_label_标签月(self)
        self.tk_select_box_选择日 = self.__tk_select_box_选择日(self)
        self.tk_label_标签日 = self.__tk_label_标签日(self)
        self.tk_label_选择应用商店 = self.__tk_label_选择应用商店(self)
        self.tk_select_box_应用商店 = self.__tk_select_box_应用商店(self)
        self.tk_label_输入app名 = self.__tk_label_输入app名(self)
        self.tk_input_app名 = self.__tk_input_app名(self)
        self.tk_label_选择查询评分 = self.__tk_label_选择查询评分(self)
        self.tk_select_box_评分 = self.__tk_select_box_评分(self)
        self.tk_label_选择评论内容 = self.__tk_label_选择评论内容(self)
        self.tk_list_box_评论内容 = self.__tk_list_box_评论内容(self)
        self.tk_label_选择评论分词 = self.__tk_label_选择评论分词(self)
        self.tk_list_box_评论分词 = self.__tk_list_box_评论分词(self)
        self.tk_button_显示分词 = self.__tk_button_显示分词(self)
        self.tk_button_执行查询 = self.__tk_button_执行查询(self)
        self.tk_label_输入要增加的分词 = self.__tk_label_输入要增加的分词(self)
        self.tk_input_输入分词 = self.__tk_input_输入分词(self)
        self.tk_button_增加分词 = self.__tk_button_增加分词(self)
        self.tk_button_删除分词 = self.__tk_button_删除分词(self)
        self.tk_button_退出查询 = self.__tk_button_退出查询(self)
        self.__event_bind()

    def __win(self):
        self.title("评论查询")
        width = 600
        height = 400
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def scrollbar_autohide(self, vbar, hbar, widget):
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

    def __tk_label_输入查询时间(self, parent):
        label = Label(parent, text="输入查询时间", anchor="center")
        label.place(x=40, y=40, width=80, height=30)
        return label

    def __tk_select_box_选择年(self, parent):
        cb = Combobox(parent, state="readonly")
        cb['values'] = ("2024", "2023", "2022", "2021", "2020")
        cb.place(x=15, y=80, width=50, height=30)
        return cb

    def __tk_label_标签年(self, parent):
        label = Label(parent, text="年", anchor="center")
        label.place(x=68, y=80, width=20, height=30)
        return label

    def __tk_select_box_选择月(self, parent):
        cb = Combobox(parent, state="readonly")
        cb['values'] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
        cb.place(x=93, y=80, width=40, height=30)
        return cb

    def __tk_label_标签月(self, parent):
        label = Label(parent, text="月", anchor="center")
        label.place(x=135, y=80, width=20, height=30)
        return label

    def __tk_select_box_选择日(self, parent):
        cb = Combobox(parent, state="readonly")
        cb['values'] = (
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
            "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
        cb.place(x=158, y=80, width=40, height=30)
        return cb

    def __tk_label_标签日(self, parent):
        label = Label(parent, text="日", anchor="center")
        label.place(x=200, y=80, width=20, height=30)
        return label

    def __tk_label_选择应用商店(self, parent):
        label = Label(parent, text="选择应用商店", anchor="center")
        label.place(x=240, y=40, width=80, height=30)
        return label

    def __tk_select_box_应用商店(self, parent):
        cb = Combobox(parent, state="readonly")
        cb['values'] = ("华为", "苹果", "google")
        cb.place(x=240, y=80, width=150, height=30)
        return cb

    def __tk_label_输入app名(self, parent):
        label = Label(parent, text="输入app名", anchor="center")
        label.place(x=420, y=40, width=80, height=30)
        return label

    def __tk_input_app名(self, parent):
        ipt = Entry(parent)
        ipt.place(x=420, y=80, width=150, height=30)
        return ipt

    def __tk_label_选择查询评分(self, parent):
        label = Label(parent, text="选择查询评分", anchor="center")
        label.place(x=40, y=140, width=80, height=30)
        return label

    def __tk_select_box_评分(self, parent):
        cb = Combobox(parent, state="readonly")
        cb['values'] = ("5", "4", "3", "2", "1")
        cb.place(x=40, y=180, width=150, height=30)
        return cb

    def __tk_label_选择评论内容(self, parent):
        label = Label(parent, text="选择评论内容", anchor="center")
        label.place(x=240, y=140, width=80, height=30)
        return label

    def __tk_list_box_评论内容(self, parent):
        lb = Listbox(parent)
        lb.insert(END, "评论内容")
        lb.place(x=240, y=180, width=150, height=100)
        self.create_bar(parent, lb, True, True, 240, 180, 150, 100, 600, 400)
        return lb

    def __tk_label_选择评论分词(self, parent):
        label = Label(parent, text="选择评论分词", anchor="center")
        label.place(x=420, y=140, width=80, height=30)
        return label

    def __tk_list_box_评论分词(self, parent):
        lb = Listbox(parent)
        lb.insert(END, "评论分词")
        lb.place(x=420, y=180, width=150, height=100)
        self.create_bar(parent, lb, True, True, 420, 180, 150, 100, 600, 400)
        return lb

    def __tk_button_显示分词(self, parent):
        btn = Button(parent, text="显示分词", takefocus=False)
        btn.place(x=510, y=140, width=60, height=30)
        return btn

    def __tk_button_执行查询(self, parent):
        btn = Button(parent, text="查询!", takefocus=False)
        btn.place(x=40, y=260, width=120, height=80)
        return btn

    def __tk_label_输入要增加的分词(self, parent):
        label = Label(parent, text="输入要增加的分词", anchor="center")
        label.place(x=240, y=280, width=100, height=30)
        return label

    def __tk_input_输入分词(self, parent):
        ipt = Entry(parent)
        ipt.place(x=240, y=320, width=150, height=30)
        return ipt

    def __tk_button_增加分词(self, parent):
        btn = Button(parent, text="增加分词", takefocus=False)
        btn.place(x=420, y=320, width=60, height=30)
        return btn

    def __tk_button_删除分词(self, parent):
        btn = Button(parent, text="删除分词", takefocus=False)
        btn.place(x=510, y=320, width=60, height=30)
        return btn

    def __tk_button_退出查询(self, parent):
        btn = Button(parent, text="退出查询", takefocus=False)
        btn.place(x=510, y=20, width=60, height=30)
        return btn

    def __event_bind(self):
        self.tk_button_显示分词.bind('<Button-1>', self.controller.显示分词)
        self.tk_button_增加分词.bind('<Button-1>', self.controller.增加分词)
        self.tk_button_删除分词.bind('<Button-1>', self.controller.删除分词)
        self.tk_button_退出查询.bind('<Button-1>', self.controller.退出查询)

class UserChange(Toplevel):
    def __init__(self, parent, controller):
        super().__init__()
        self.__win()
        self.controller = controller
        self.admin_window = parent  # 保存管理员窗口引用
        self.tk_label_修改前账号 = self.__tk_label_修改前账号(self)
        self.tk_label_修改前密码 = self.__tk_label_修改前密码(self)
        self.tk_label_修改前关注app = self.__tk_label_修改前关注app(self)
        self.tk_label_修改为 = self.__tk_label_修改为(self)
        self.tk_text_修改后账号 = self.__tk_text_修改后账号(self)
        self.tk_text_修改后密码 = self.__tk_text_修改后密码(self)
        self.tk_text_修改后关注app = self.__tk_text_修改后关注app(self)
        self.tk_button_修改按钮 = self.__tk_button_修改按钮(self)
        self.tk_button_不修改按钮 = self.__tk_button_不修改按钮(self)
        self.__event_bind()
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

    def __event_bind(self):
        self.tk_button_修改按钮.bind('<Button-1>', self.controller.修改按钮)
        self.tk_button_不修改按钮.bind('<Button-1>', self.controller.不修改按钮)


if __name__ == "__main__":
    controller = Controller()
    win = Win(controller)
    win.mainloop()

"""
分词,分词解析,,
用户界面
查询关注的app最近100条评论
近况:分词图,评论数趋势图,评论评分饼图
管理员界面
获取(爬虫)最新评论
查询用户情况,设置用户密码、关注的APP
按时间、内容、地区、分数等搜索条件，查询相应的评论详情
"""
