import os
from tkinter import *
import tkinter.messagebox as messagebox



class Application(Frame):  # 从Frame派生出Application类，它是所有widget的父容器
    def __init__(self, master=None):  # master即是窗口管理器，用于管理窗口部件，如按钮标签等，顶级窗口master是None，即自己管理自己
        Frame.__init__(self, master)
        self.pack()  # 将widget加入到父容器中并实现布局
        self.createWidgets()
    def createWidgets(self):
        self.quitButton = Label(self, text='请输入wav语音路径：')  # 创建一个Quit按钮，实现点击即退出窗口
        self.quitButton.pack()
        self.input_wavPath = Entry(self,width=30)  # 创建一个输入框，以输入内容
        self.input_wavPath.pack()

        self.quitButton_txtPath = Label(self, text='请输入txt存储路径：')  # 创建一个Quit按钮，实现点击即退出窗口
        self.quitButton_txtPath.pack()
        self.input_txtPath = Entry(self,width=30)  # 创建一个输入框，以输入内容
        self.input_txtPath.pack()

        self.nameButton = Button(self, text='分帧', command=self.hello)  # 创建一个hello按钮，点击调用hello方法，实现输出
        self.nameButton2 = Button(self, text='识别', command=self.recog)  # 创建一个hello按钮，点击调用hello方法，实现输出
        self.nameButton.pack(side=LEFT)
        self.nameButton2.pack(side=RIGHT)

    def hello(self):
        wavPath = self.input_wavPath.get()  # 获取输入的内容
        command1 = "python WavFileCutWithArgv.py "+str(wavPath)
        os.system(command1)
        messagebox.showinfo('Message', 'succeed!') # 显示输出

    def recog(self):
        txtPath = self.input_txtPath.get()  # 获取输入的内容
        tempPath = os.path.dirname(__file__)
        tempPath = tempPath+'/MusicResult'
        command2 = "python test.py "+str(txtPath)+' '+str(tempPath)
        os.system(command2)
        messagebox.showinfo('Message', 'succeed!')  # 显示输出

# C:\Users\epic_cy\Desktop\1.txt
# E:\caoyong\开会\4.wav
# C:\Users\epic_cy\Desktop\WavCut-master\WavCut-master\MusicResult
app = Application()
app.master.title("语音转文本")  # 窗口标题
app.master.geometry("300x150")
app.mainloop()  # 主消息循环
