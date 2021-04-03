#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
from git import Repo
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

        self.Command8Var = StringVar(value='|||')
        self.style.configure('TCommand8.TButton', font=('宋体',9))
        self.Command8 = Button(self.top, text='|||', textvariable=self.Command8Var, command=self.Command8_Cmd, style='TCommand8.TButton')
        self.Command8.setText = lambda x: self.Command8Var.set(x)
        self.Command8.text = lambda : self.Command8Var.get()
        self.Command8.place(relx=0.941, rely=0.03, relwidth=0.03, relheight=0.051)

        self.Command7Var = StringVar(value='-')
        self.style.configure('TCommand7.TButton', font=('宋体',9))
        self.Command7 = Button(self.top, text='-', textvariable=self.Command7Var, command=self.Command7_Cmd, style='TCommand7.TButton')
        self.Command7.setText = lambda x: self.Command7Var.set(x)
        self.Command7.text = lambda : self.Command7Var.get()
        self.Command7.place(relx=0.906, rely=0.03, relwidth=0.03, relheight=0.051)

        self.Command6Var = StringVar(value='O')
        self.style.configure('TCommand6.TButton', font=('宋体',9))
        self.Command6 = Button(self.top, text='O', textvariable=self.Command6Var, command=self.Command6_Cmd, style='TCommand6.TButton')
        self.Command6.setText = lambda x: self.Command6Var.set(x)
        self.Command6.text = lambda : self.Command6Var.get()
        self.Command6.place(relx=0.871, rely=0.03, relwidth=0.03, relheight=0.051)

        self.Command5Var = StringVar(value='X')
        self.style.configure('TCommand5.TButton', font=('宋体',9))
        self.Command5 = Button(self.top, text='X', textvariable=self.Command5Var, command=self.Command5_Cmd, style='TCommand5.TButton')
        self.Command5.setText = lambda x: self.Command5Var.set(x)
        self.Command5.text = lambda : self.Command5Var.get()
        self.Command5.place(relx=0.836, rely=0.03, relwidth=0.03, relheight=0.051)

        self.CommandTextVar = StringVar(value='')
        self.CommandText = Entry(self.top, textvariable=self.CommandTextVar, font=('宋体',9))
        self.CommandText.setText = lambda x: self.CommandTextVar.set(x)
        self.CommandText.text = lambda : self.CommandTextVar.get()
        self.CommandText.place(relx=0.596, rely=0.945, relwidth=0.398, relheight=0.041)

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

        self.style.configure('TUserFrame.TLabelframe', font=('宋体',9))
        self.style.configure('TUserFrame.TLabelframe.Label', font=('宋体',9))
        self.UserFrame = LabelFrame(self.top, text='User', style='TUserFrame.TLabelframe')
        self.UserFrame.place(relx=0.012, rely=0.01, relwidth=0.194, relheight=0.24)

        self.LogListVar = StringVar(value='')
        self.LogListFont = Font(font=('宋体',9))
        self.LogList = Listbox(self.InfoFrame, listvariable=self.LogListVar, font=self.LogListFont)
        self.LogList.place(relx=0.029, rely=0.036, relwidth=0.941, relheight=0.944)

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
        self.Text3 = Entry(self.UserFrame, textvariable=self.Text3Var, font=('宋体',9))
        self.Text3.setText = lambda x: self.Text3Var.set(x)
        self.Text3.text = lambda : self.Text3Var.get()
        self.Text3.place(relx=0.211, rely=0.332, relwidth=0.668, relheight=0.13)

        self.Text2Var = StringVar(value='Text2')
        self.Text2 = Entry(self.UserFrame, textvariable=self.Text2Var, font=('宋体',9))
        self.Text2.setText = lambda x: self.Text2Var.set(x)
        self.Text2.text = lambda : self.Text2Var.get()
        self.Text2.place(relx=0.211, rely=0.166, relwidth=0.668, relheight=0.13)

        self.Command2Var = StringVar(value='Command1')
        self.style.configure('TCommand2.TButton', font=('宋体',9))
        self.Command2 = Button(self.UserFrame, text='Command1', textvariable=self.Command2Var, command=self.Command2_Cmd, style='TCommand2.TButton')
        self.Command2.setText = lambda x: self.Command2Var.set(x)
        self.Command2.text = lambda : self.Command2Var.get()
        self.Command2.place(relx=0.543, rely=0.746, relwidth=0.366, relheight=0.171)

        self.Command1Var = StringVar(value='Command1')
        self.style.configure('TCommand1.TButton', font=('宋体',9))
        self.Command1 = Button(self.UserFrame, text='Command1', textvariable=self.Command1Var, command=self.Command1_Cmd, style='TCommand1.TButton')
        self.Command1.setText = lambda x: self.Command1Var.set(x)
        self.Command1.text = lambda : self.Command1Var.get()
        self.Command1.place(relx=0.06, rely=0.746, relwidth=0.366, relheight=0.171)

        self.Label2Var = StringVar(value='Label1')
        self.style.configure('TLabel2.TLabel', anchor='w', font=('宋体',9))
        self.Label2 = Label(self.UserFrame, text='Label1', textvariable=self.Label2Var, style='TLabel2.TLabel')
        self.Label2.setText = lambda x: self.Label2Var.set(x)
        self.Label2.text = lambda : self.Label2Var.get()
        self.Label2.place(relx=0.03, rely=0.332, relwidth=0.155, relheight=0.13)

        self.Label1Var = StringVar(value='Label1')
        self.style.configure('TLabel1.TLabel', anchor='w', font=('宋体',9))
        self.Label1 = Label(self.UserFrame, text='Label1', textvariable=self.Label1Var, style='TLabel1.TLabel')
        self.Label1.setText = lambda x: self.Label1Var.set(x)
        self.Label1.text = lambda : self.Label1Var.get()
        self.Label1.place(relx=0.03, rely=0.166, relwidth=0.155, relheight=0.13)




class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self.initData()

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


    def handler_adaptor(self, fun,  **kwds):
        return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)

    def handler(self, event, name, item, option, item_type, data, log):
        self.Log("UI交互:控件["+name+"]类型["+item_type+"]操作["+
              option+"]数据["+str(data)+"]提示信息["+str(log)+"]")
        print("UI交互:控件["+name+"]类型["+item_type+"]操作["+
              option+"]数据["+str(data)+"]提示信息["+str(log)+"]")


    def initData(self):
        self.app_dir=os.path.dirname(os.path.realpath(sys.argv[0]))
        self.Log("App Run at:%s"%self.app_dir)
         

    def Log(self,info):
        # if self.LoggerLevel<1999:
        #     return
        _info = str(info)
        # if len(info) > 110:
        #     _info = str(info)[0:50]+"..."+str(info)[len(info)-50:len(info)]
        self.LogList.insert(END, " "+str(_info))
        self.LogList.itemconfig(END, bg="#C3C3C3")
        self.LogList.see(END)
        # self.Log2File(info,None)
        pass

    def LogSuccessful(self, info, event=None):
        # if self.LoggerLevel<9:
        #     return
        _info = str(info)
        # if len(info) > 110:
        #     _info = str(info)[0:50]+"..."+str(info)[len(info)-50:len(info)]
        self.LogList.insert(END, str(_info))
        self.LogList.itemconfig(END, bg="#00FF00")
        self.LogList.itemconfig(END, fg="#000000")
        self.LogList.see(END)

    def LogWarning(self, info, event=None):
        # if self.LoggerLevel<199:
        #     return
        _info = str(info)
        # if len(info) > 110:
            # _info = str(info)[0:50]+"..."+str(info)[len(info)-50:len(info)]
        self.LogList.insert(END, "   "+str(_info))
        self.LogList.itemconfig(END, bg="#FFFF00")
        self.LogList.itemconfig(END, fg="#000000")
        self.LogList.see(END)
        # self.Log2File(info,None)

    def LogError(self, info, event=None):
        # if self.LoggerLevel<19:
        #     return
        _info = str(info)
        # if len(info) > 100:
        #     _info = str(info)[0:100]+"\n"+str(info)[len(info)-100:len(info)]
        #     if len(info) > 200:
        #         _info = str(info)[0:100]+"\n"+str(info)[100:200]+"\n"+str(info)[len(info)-200:len(info)]
        #         if len(info) > 300:
        #             _info = str(info)[0:100]+"\n"+str(info)[100:200]+"\n"+str(info)[200:300]+"\n"+str(info)[len(info)-300:len(info)] 
        self.LogList.insert(END, str(_info))
        self.LogList.itemconfig(END, bg="#FF0000")
        self.LogList.itemconfig(END, fg="#FFFFFF")
        self.LogList.see(END)
        # self.Log2File(info,None)
        pass

    def CheckPath(self, filename):
        try:
            print("  check file>>> %s "% filename)
            _file = filename
            if None == _file:
                print("   file>>> %s >>>None"% filename)
                return False
            if _file == "":
                print("   file>>> %s >>>Empty"% filename)
                return False
            if len(str(_file)) < 3:
                print("   file>>> %s >>>Not a File"% filename)
                return False
            if not os.path.exists(_file):
                print("   file>>> %s >>>Not Exists"% filename)
                return False
            if os.path.isfile(filename):
                print("   file>>> %s >>>Is File"% filename)
                return False
            print("   path>>> %s >>>Success"% filename)
            return True
        except Exception as e:
            print(e)
            return False

    def commit(self,gitPath):
        self.Log("Commit Request:%s"%str(gitPath))
        print("Commit Request:%s"%str(gitPath))
        repo = Repo(gitPath, search_parent_directories=True)
        self.Log("RepoStatus:%s"%self.repo.git.status())
        print("RepoStatus:%s"%self.repo.git.status())
        remote = repo.remote()
        origin = repo.remotes.origin
        index  = repo.index
        changedFiles = [ item.a_path for item in repo.index.diff(None) ]
        self.Log("ChangedFiles:%s"%changedFiles)
        untracked_files = repo.untracked_files
        self.Log("UntrackedFiles:%s"%untracked_files)
        index.add(changedFiles)
        print("add files 2 master : %s"%changedFiles)
        self.LogSuccessful("modify added file:%s"%changedFiles)
        index.add(untracked_files)
        print("add untracked_files 2 master : %s"%untracked_files)
        self.LogSuccessful("added new file:%s"%untracked_files)
        commit_msg=""
        if len(changedFiles)+len(untracked_files)>0:
            print("new commit:%s"%str(self.fileindex))
            commit_msg="a new version"
            if len(untracked_files)>0:
                commit_msg="new:%s,video current id:%s"%(str(untracked_files),str(self.fileindex))
            self.index.commit(commit_msg)
            self.LogSuccessful("commit:%s"%commit_msg)
        if "Your branch is ahead of" in self.repo.git.status():
            self.LogWarning("Push:%s"%self.repo.git.status())
            self.repo.remote().push()
        if "Your branch is up to date" in self.repo.git.status():
            self.LogSuccessful("Your branch is up to date!:%s"%self.repo.git.status())
        pass


    def getV2rayData(self):
        self.Log("Start to check V2ray Links:")
        defaulturl = "http://music.sonimei.cn/"
        defaultHeader = {
            'upgrade-insecure-requests': "1",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            'dnt': "1",
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'accept-encoding': "gzip, deflate",
            'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
            'cache-control': "no-cache"
            }
        ajaxheaders = {
            'upgrade-insecure-requests': "1",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            'dnt': "1",
            'accept-encoding': "gzip, deflate",
            'x-requested-with': "XMLHttpRequest",
            'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
            'cache-control': "no-cache",
            'accept': "application/json, text/javascript, */*; q=0.01",
            }



if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()

