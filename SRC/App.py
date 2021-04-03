#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
if sys.version_info[0] == 2:
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    from tkinter import *
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('自动化程序集合')
        self.master.geometry('1369x804')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.Command8Var = StringVar(value='Command5')
        self.style.configure('TCommand8.TButton', font=('宋体',9))
        self.Command8 = Button(self.top, text='Command5', textvariable=self.Command8Var, command=self.Command8_Cmd, style='TCommand8.TButton')
        self.Command8.setText = lambda x: self.Command8Var.set(x)
        self.Command8.text = lambda : self.Command8Var.get()
        self.Command8.place(relx=0.941, rely=0.03, relwidth=0.03, relheight=0.051)

        self.Command7Var = StringVar(value='Command5')
        self.style.configure('TCommand7.TButton', font=('宋体',9))
        self.Command7 = Button(self.top, text='Command5', textvariable=self.Command7Var, command=self.Command7_Cmd, style='TCommand7.TButton')
        self.Command7.setText = lambda x: self.Command7Var.set(x)
        self.Command7.text = lambda : self.Command7Var.get()
        self.Command7.place(relx=0.906, rely=0.03, relwidth=0.03, relheight=0.051)

        self.Command6Var = StringVar(value='Command5')
        self.style.configure('TCommand6.TButton', font=('宋体',9))
        self.Command6 = Button(self.top, text='Command5', textvariable=self.Command6Var, command=self.Command6_Cmd, style='TCommand6.TButton')
        self.Command6.setText = lambda x: self.Command6Var.set(x)
        self.Command6.text = lambda : self.Command6Var.get()
        self.Command6.place(relx=0.871, rely=0.03, relwidth=0.03, relheight=0.051)

        self.Command5Var = StringVar(value='Command5')
        self.style.configure('TCommand5.TButton', font=('宋体',9))
        self.Command5 = Button(self.top, text='Command5', textvariable=self.Command5Var, command=self.Command5_Cmd, style='TCommand5.TButton')
        self.Command5.setText = lambda x: self.Command5Var.set(x)
        self.Command5.text = lambda : self.Command5Var.get()
        self.Command5.place(relx=0.836, rely=0.03, relwidth=0.03, relheight=0.051)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.top, textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.setText = lambda x: self.Text1Var.set(x)
        self.Text1.text = lambda : self.Text1Var.get()
        self.Text1.place(relx=0.596, rely=0.945, relwidth=0.398, relheight=0.041)

        self.Command4Var = StringVar(value='Command4')
        self.style.configure('TCommand4.TButton', font=('宋体',9))
        self.Command4 = Button(self.top, text='Command4', textvariable=self.Command4Var, command=self.Command4_Cmd, style='TCommand4.TButton')
        self.Command4.setText = lambda x: self.Command4Var.set(x)
        self.Command4.text = lambda : self.Command4Var.get()
        self.Command4.place(relx=0.503, rely=0.945, relwidth=0.088, relheight=0.041)

        self.style.configure('TInfoFrame.TLabelframe', font=('宋体',9))
        self.style.configure('TInfoFrame.TLabelframe.Label', font=('宋体',9))
        self.InfoFrame = LabelFrame(self.top, text='Info', style='TInfoFrame.TLabelframe')
        self.InfoFrame.place(relx=0.596, rely=0.1, relwidth=0.398, relheight=0.827)

        self.style.configure('TTaskFrame.TLabelframe', font=('宋体',9))
        self.style.configure('TTaskFrame.TLabelframe.Label', font=('宋体',9))
        self.TaskFrame = LabelFrame(self.top, text='TaskList', style='TTaskFrame.TLabelframe')
        self.TaskFrame.place(relx=0.216, rely=0.109, relwidth=0.375, relheight=0.817)

        self.style.configure('TControlPannelFrame.TLabelframe', font=('宋体',9))
        self.style.configure('TControlPannelFrame.TLabelframe.Label', font=('宋体',9))
        self.ControlPannelFrame = LabelFrame(self.top, text='Control', style='TControlPannelFrame.TLabelframe')
        self.ControlPannelFrame.place(relx=0.012, rely=0.259, relwidth=0.194, relheight=0.668)

        self.style.configure('TAPP.TLabelframe', font=('宋体',9))
        self.style.configure('TAPP.TLabelframe.Label', font=('宋体',9))
        self.APP = LabelFrame(self.top, text='GITHUB TASK', style='TAPP.TLabelframe')
        self.APP.place(relx=0.012, rely=0.01, relwidth=0.194, relheight=0.24)

        self.LogFrameVar = StringVar(value='')
        self.LogFrameFont = Font(font=('宋体',9))
        self.LogFrame = Listbox(self.InfoFrame, listvariable=self.LogFrameVar, font=self.LogFrameFont)
        self.LogFrame.place(relx=0.029, rely=0.036, relwidth=0.941, relheight=0.944)

        self.Command10Var = StringVar(value='Command1')
        self.style.configure('TCommand10.TButton', font=('宋体',9))
        self.Command10 = Button(self.ControlPannelFrame, text='Command1', textvariable=self.Command10Var, command=self.Command10_Cmd, style='TCommand10.TButton')
        self.Command10.setText = lambda x: self.Command10Var.set(x)
        self.Command10.text = lambda : self.Command10Var.get()
        self.Command10.place(relx=0.06, rely=0.194, relwidth=0.819, relheight=0.061)

        self.Command9Var = StringVar(value='Command1')
        self.style.configure('TCommand9.TButton', font=('宋体',9))
        self.Command9 = Button(self.ControlPannelFrame, text='Command1', textvariable=self.Command9Var, command=self.Command9_Cmd, style='TCommand9.TButton')
        self.Command9.setText = lambda x: self.Command9Var.set(x)
        self.Command9.text = lambda : self.Command9Var.get()
        self.Command9.place(relx=0.06, rely=0.119, relwidth=0.819, relheight=0.061)

        self.Command3Var = StringVar(value='Command1')
        self.style.configure('TCommand3.TButton', font=('宋体',9))
        self.Command3 = Button(self.ControlPannelFrame, text='Command1', textvariable=self.Command3Var, command=self.Command3_Cmd, style='TCommand3.TButton')
        self.Command3.setText = lambda x: self.Command3Var.set(x)
        self.Command3.text = lambda : self.Command3Var.get()
        self.Command3.place(relx=0.06, rely=0.045, relwidth=0.819, relheight=0.061)

        self.TaskListVar = StringVar(value='')
        self.TaskListFont = Font(font=('宋体',9))
        self.TaskList = Listbox(self.TaskFrame, listvariable=self.TaskListVar, font=self.TaskListFont)
        self.TaskList.place(relx=0.031, rely=0.037, relwidth=0.938, relheight=0.773)

        self.Text3Var = StringVar(value='Text2')
        self.Text3 = Entry(self.APP, textvariable=self.Text3Var, font=('宋体',9))
        self.Text3.setText = lambda x: self.Text3Var.set(x)
        self.Text3.text = lambda : self.Text3Var.get()
        self.Text3.place(relx=0.211, rely=0.332, relwidth=0.668, relheight=0.13)

        self.Text2Var = StringVar(value='Text2')
        self.Text2 = Entry(self.APP, textvariable=self.Text2Var, font=('宋体',9))
        self.Text2.setText = lambda x: self.Text2Var.set(x)
        self.Text2.text = lambda : self.Text2Var.get()
        self.Text2.place(relx=0.211, rely=0.166, relwidth=0.668, relheight=0.13)

        self.Command2Var = StringVar(value='Command1')
        self.style.configure('TCommand2.TButton', font=('宋体',9))
        self.Command2 = Button(self.APP, text='Command1', textvariable=self.Command2Var, command=self.Command2_Cmd, style='TCommand2.TButton')
        self.Command2.setText = lambda x: self.Command2Var.set(x)
        self.Command2.text = lambda : self.Command2Var.get()
        self.Command2.place(relx=0.543, rely=0.746, relwidth=0.366, relheight=0.171)

        self.Command1Var = StringVar(value='Command1')
        self.style.configure('TCommand1.TButton', font=('宋体',9))
        self.Command1 = Button(self.APP, text='Command1', textvariable=self.Command1Var, command=self.Command1_Cmd, style='TCommand1.TButton')
        self.Command1.setText = lambda x: self.Command1Var.set(x)
        self.Command1.text = lambda : self.Command1Var.get()
        self.Command1.place(relx=0.06, rely=0.746, relwidth=0.366, relheight=0.171)

        self.Label2Var = StringVar(value='Label1')
        self.style.configure('TLabel2.TLabel', anchor='w', font=('宋体',9))
        self.Label2 = Label(self.APP, text='Label1', textvariable=self.Label2Var, style='TLabel2.TLabel')
        self.Label2.setText = lambda x: self.Label2Var.set(x)
        self.Label2.text = lambda : self.Label2Var.get()
        self.Label2.place(relx=0.03, rely=0.332, relwidth=0.155, relheight=0.13)

        self.Label1Var = StringVar(value='Label1')
        self.style.configure('TLabel1.TLabel', anchor='w', font=('宋体',9))
        self.Label1 = Label(self.APP, text='Label1', textvariable=self.Label1Var, style='TLabel1.TLabel')
        self.Label1.setText = lambda x: self.Label1Var.set(x)
        self.Label1.text = lambda : self.Label1Var.get()
        self.Label1.place(relx=0.03, rely=0.166, relwidth=0.155, relheight=0.13)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command8_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command7_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command6_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command5_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command4_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command10_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command9_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command3_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command2_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()

