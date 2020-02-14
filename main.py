import os
from tkinter import Tk, Menu, Label, Button
from tkinter.filedialog import askopenfilenames
from tkinter.messagebox import showinfo

from make_love_you_img import gen_love_you_img

IMGPATH = ''

class GUI(object):

    def __init__(self, window):
        self.window = window
        self.window.title('表白神器')
        self.window.geometry('300x200')
        menubar = Menu(self.window)

        # 定义空菜单
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='帮助', command=self.helpme)
        filemenu.add_separator()

        # 显示
        self.l = Label(window, text='')
        self.l.pack(padx=5, pady=10)  # 固定窗口位置

        # 选择图片
        btn1 = Button(window, text='选择图片', width=15, height=2, command=self.get_img)
        btn1.pack()

        # 生成图片
        self.send_btn = Button(window, text='生成表白图片', width=15, height=2, command=self.gen_img)
        self.send_btn.pack()

    def helpme(self):
        showerror('帮助', '请关注「懒编程」公众号，联系作者二两')

    def get_img(self):
        global IMGPATH
        # 选择文件
        filenames = askopenfilenames(filetypes=(("jpeg img", "*.jpeg"), ("jpg img", "*.jpg"), ("png img", "*.png")))
        if len(filenames) > 0:
            fnlist = [fn for fn in filenames]
            fnstr = '\n'.join(fnlist)
            self.l.config(text=fnstr)
            IMGPATH = fnlist
        else:
            self.l.config(text='目前没有选择任何图片文件')

    def gen_img(self):
        global IMGPATH
        respathlist = []
        for imgpath in IMGPATH:
            filepath,tempfilename = os.path.split(imgpath)
            filename,extension = os.path.splitext(tempfilename)
            savepath =  f'{filename}_gen{extension}'
            gen_love_you_img(imgpath, savepath)
            respathlist.append(savepath)
        respath = ' '.join(respathlist)
        showinfo('完成生成', f'表白图片已生成，路径为：{respath}')

if __name__ == '__main__':
    # 创建窗口
    window = Tk()
    GUI(window)
    # 显示窗口 必须在所有控件后
    window.mainloop()
