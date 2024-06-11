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
    def __win(self):
        self.title("管理员查询评论")
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
    def __tk_label_输入查询时间(self,parent):
        label = Label(parent,text="输入查询时间",anchor="center", )
        label.place(x=40, y=40, width=80, height=30)
        return label
    def __tk_select_box_选择年(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("2024","2","3","4","5","6","7","8","9","10","11","12")
        cb.place(x=15, y=80, width=50, height=30)
        return cb
    def __tk_label_标签年(self,parent):
        label = Label(parent,text="年",anchor="center", )
        label.place(x=68, y=80, width=20, height=30)
        return label
    def __tk_select_box_选择月(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("1","2","3","4","5","6","7","8","9","10","11","12")
        cb.place(x=93, y=80, width=40, height=30)
        return cb
    def __tk_label_标签月(self,parent):
        label = Label(parent,text="月",anchor="center", )
        label.place(x=135, y=80, width=20, height=30)
        return label
    def __tk_select_box_选择日(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("1","2","3","4","5","6","7","8","9","10","11","12")
        cb.place(x=158, y=80, width=40, height=30)
        return cb
    def __tk_label_标签日(self,parent):
        label = Label(parent,text="日",anchor="center", )
        label.place(x=200, y=80, width=20, height=30)
        return label
    def __tk_label_选择应用商店(self,parent):
        label = Label(parent,text="选择应用商店",anchor="center", )
        label.place(x=240, y=40, width=80, height=30)
        return label
    def __tk_select_box_应用商店(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("华为","苹果","google")
        cb.place(x=240, y=80, width=150, height=30)
        return cb
    def __tk_label_输入app名(self,parent):
        label = Label(parent,text="输入app名",anchor="center", )
        label.place(x=420, y=40, width=80, height=30)
        return label
    def __tk_input_app名(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=420, y=80, width=150, height=30)
        return ipt
    def __tk_label_选择查询评分(self,parent):
        label = Label(parent,text="选择查询评分",anchor="center", )
        label.place(x=40, y=140, width=80, height=30)
        return label
    def __tk_select_box_评分(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("5","4","3","2","1")
        cb.place(x=40, y=180, width=150, height=30)
        return cb
    def __tk_label_选择评论内容(self,parent):
        label = Label(parent,text="选择评论内容",anchor="center", )
        label.place(x=240, y=140, width=80, height=30)
        return label
    def __tk_list_box_评论内容(self,parent):
        lb = Listbox(parent)

        lb.insert(END, "评论内容")

        lb.place(x=240, y=180, width=150, height=100)
        self.create_bar(parent, lb, True, True,240, 180, 150,100,600,400)
        return lb
    def __tk_label_选择评论分词(self,parent):
        label = Label(parent,text="选择评论分词",anchor="center", )
        label.place(x=420, y=140, width=80, height=30)
        return label
    def __tk_list_box_评论分词(self,parent):
        lb = Listbox(parent)

        lb.insert(END, "评论分词")

        lb.place(x=420, y=180, width=150, height=100)
        self.create_bar(parent, lb, True, True,420, 180, 150,100,600,400)
        return lb
    def __tk_button_显示分词(self,parent):
        btn = Button(parent, text="显示分词", takefocus=False,)
        btn.place(x=510, y=140, width=60, height=30)
        return btn
    def __tk_button_执行查询(self,parent):
        btn = Button(parent, text="查询!", takefocus=False,)
        btn.place(x=40, y=260, width=120, height=80)
        return btn
    def __tk_label_输入要增加的分词(self,parent):
        label = Label(parent,text="输入要增加的分词",anchor="center", )
        label.place(x=240, y=280, width=100, height=30)
        return label
    def __tk_input_输入分词(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=240, y=320, width=150, height=30)
        return ipt
    def __tk_button_增加分词(self,parent):
        btn = Button(parent, text="增加分词", takefocus=False,)
        btn.place(x=420, y=320, width=60, height=30)
        return btn
    def __tk_button_删除分词(self,parent):
        btn = Button(parent, text="删除分词", takefocus=False,)
        btn.place(x=510, y=320, width=60, height=30)
        return btn
    def __tk_button_退出查询(self,parent):
        btn = Button(parent, text="退出查询", takefocus=False,)
        btn.place(x=530, y=20, width=50, height=30)
        return btn
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_button_显示分词.bind('<Button-1>',self.ctl.显示分词)
        self.tk_button_增加分词.bind('<Button-1>',self.ctl.增加分词)
        self.tk_button_删除分词.bind('<Button-1>',self.ctl.删除分词)
        self.tk_button_退出查询.bind('<Button-1>',self.ctl.退出查询)
        pass
    def __style_config(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()