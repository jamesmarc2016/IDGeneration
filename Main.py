#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 导入tkinter包，为其定义别名tk
import Tkinter as tk
import ttk
import ProCitGen as pc

class Application(tk.Frame):
    # Application构造函数，master为窗口的父控件
    def __init__(self, master=None):
        # 初始化Application的Frame部分
        tk.Frame.__init__(self, master)
        # 显示窗口，并使用grid布局
        self.grid()
        # 创建控件
        self.createWidgets()

        # 创建控件
    def createWidgets(self):
        self.prov = tk.Label(self,text = "省：")
        self.city = tk.Label(self, text="市：")
        self.xian = tk.Label(self, text="县/区：")
        self.year = tk.Label(self, text="出生-年：")
        self.mou = tk.Label(self, text="出生-月：")
        self.day = tk.Label(self, text="出生-日：")
        self.gendar = tk.Label(self, text="性别：")

        provStr = tk.StringVar()
        cityStr = tk.StringVar()
        xianStr = tk.StringVar()
        yearStr = tk.StringVar()
        mouStr = tk.StringVar()
        dayStr = tk.StringVar()
        gendarStr = tk.StringVar()

        self.provCom = ttk.Combobox(self, width=12, state='readonly',textvariable=provStr)
        provList = pc.getProv()
        self.provCom['values'] = provList
        self.provCom.current(0)  # 选择第一个
        self.provCom.bind("<<ComboboxSelected>>", self.show_city)

        self.cityCom = ttk.Combobox(self, width=12, state='readonly',textvariable=cityStr)
        self.cityCom['values'] = ['-请选择-']
        self.cityCom.current(0)  # 选择第一个
        self.cityCom.bind("<<ComboboxSelected>>", self.show_xian)

        self.xianCom = ttk.Combobox(self, width=12, state='readonly',textvariable=xianStr)
        self.xianCom['values'] = ['-请选择-']
        self.xianCom.current(0)  # 选择第一个

        self.yearCom = ttk.Combobox(self, width=12, state='readonly',textvariable=yearStr)
        self.yearCom['values'] = pc.getYear()
        self.yearCom.current(0)  # 选择第一个

        self.mouCom = ttk.Combobox(self, width=12, state='readonly',textvariable=mouStr)
        self.mouCom['values'] = pc.getMou()
        self.mouCom.current(0)  # 选择第一个

        self.dayCom = ttk.Combobox(self, width=12, state='readonly',textvariable=dayStr)
        self.dayCom['values'] = pc.getDay()
        self.dayCom.current(0)  # 选择第一个

        self.gendarCom = ttk.Combobox(self, width=12, state='readonly',textvariable=gendarStr)
        self.gendarCom['values'] = ['男','女']
        self.gendarCom.current(0)  # 选择第一个

        self.startBut = tk.Button(self,text='开始生成',width=15,height=1)
        self.startBut.bind("<Button-1>",self.startGen)

        self.texts = tk.Text(self,width=59,font=("Symbol", 14))

        self.prov.grid(row=0, column=0)
        self.city.grid(row=0, column=2)
        self.xian.grid(row=0, column=4)
        self.year.grid(row=1, column=0)
        self.mou.grid(row=1, column=2)
        self.day.grid(row=1, column=4)
        self.gendar.grid(row=2, column=0)

        self.provCom.grid(row=0, column=1)
        self.cityCom.grid(row=0, column=3)
        self.xianCom.grid(row=0, column=5)
        self.yearCom.grid(row=1, column=1)
        self.mouCom.grid(row=1, column=3)
        self.dayCom.grid(row=1, column=5)
        self.gendarCom.grid(row=2, column=1)

        self.startBut.grid(row=3, column=0)
        self.texts.grid(row=4, column=0,columnspan=9)

    def show_city(self,event):
        prov = self.provCom.get()
        self.cityCom['values'] = pc.getCity(prov)

    def show_xian(self,event):
        prov = self.provCom.get()
        city = self.cityCom.get()
        self.xianCom['values'] = pc.getXian(city)

    def startGen(self,event):
        xian = self.xianCom.get()
        year = self.yearCom.get()
        mou = self.mouCom.get()
        day = self.dayCom.get()
        gendar = self.gendarCom.get()
        IdLists = pc.getIdLists(xian,year,mou,day,gendar)

        self.texts.delete(1.0, tk.END)
        i = 0
        for id in IdLists:
            self.texts.insert(tk.END, id + '\n')

# 创建一个Application对象app
app = Application()
# 设置窗口标题
app.master.title = 'IDGEN'
app.master.geometry('600x500')
# 主循环开始
app.mainloop()