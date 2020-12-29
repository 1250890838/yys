import pyautogui
import win32gui
import win32con
import threading
import tkinter as tk
import time
lock=0
#定义窗口，里面还有各种按钮
class Window():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("阴阳师")
        btn_start = tk.Button(master=self.window, text="准备开始", command=init, width=20, bg='red')
        btn_start.grid(row=0, column=0)
        btn_huntu = tk.Button(master=self.window, text="组队魂土", command=huntu_th, width=20, bg='blue')
        btn_huntu.grid(row=0, column=1)
        number_juexin=tk.Entry()
        number_juexin.grid(row=1,column=1)
        btn_juexin = tk.Button(master=self.window, text="单人觉醒右边层数", command=lambda:juexin_th(number_juexin),width=20, bg='yellow')
        btn_juexin.grid(row=1, column=0)
        btn_hunshi=tk.Button(master=self.window,text='单人御魂',command=hunshi_th,width=20,bg='pink')
        btn_hunshi.grid(row=2,column=0)
        btn_juexin = tk.Button(master=self.window, text="退出", command=exit, width=20, bg='purple')
        btn_juexin.grid(row=2, column=1)
        btn_juexin = tk.Button(master=self.window, text="停止/继续", command=stop, width=20, bg='white')
        btn_juexin.grid(row=3, column=0)
        lbl_note = tk.Label(master=self.window, text='烦烦烦烦烦烦烦烦烦')
        lbl_note.grid(row=3, column=1)
    def run(self):
        self.window.mainloop()

#调整窗口大小，这样才能识别图片来点击
def init():
    handle=win32gui.FindWindow(None,"阴阳师-网易游戏")
    win32gui.SetWindowPos(handle, None, 0, 0, 821, 500, win32con.SWP_SHOWWINDOW)

#魂十按钮对应的函数，用来启动线程执行--魂十
def hunshi_th():
    thread=threading.Thread(target=hunshi,daemon=True)
    thread.start()

#魂十线程执行的函数
def hunshi():
    while True:
        click_begin_hunshi()
        click_over_hunshi()

#点击魂十的挑战按钮
def click_begin_hunshi():
    while True:
        if lock==1:
            exit(0)
        try:
            x,y=pyautogui.locateCenterOnScreen("../images/begin_hun.png")
            pyautogui.click(x,y)
            return
        except:
            time.sleep(0.1)

#点击魂十的结束按钮
def click_over_hunshi():
    while True:
        if lock == 1:
            exit(0)
        try:
            x, y = pyautogui.locateCenterOnScreen("../images/over_hun1.png")
            pyautogui.click(x,y)
            for i in range(15):
                time.sleep(0.1)
                pyautogui.doubleClick(x,y)
            return
        except:
            time.sleep(0.1)

#觉醒按钮的函数，用来启动觉醒线程
def juexin_th(number):
    thread=threading.Thread(target=juexin,daemon=True,args=(number,))
    thread.start()

#觉醒线程执行的函数
def juexin(number):
    if number.get() == '1':
        number="../images/over_jue1.png"
    elif number.get() == '2':
        number="../images/over_jue2.png"
    elif number.get() == '3':
        number = "../images/over_jue3.png"
    elif number.get() == '4':
        number = "../images/over_jue4.png"
    elif number.get() == '5':
        number = "../images/over_jue5.png"
    elif number.get() == '6':
        number = "../images/over_jue6.png"
    elif number.get() == '7':
        number = "../images/over_jue7.png"
    elif number.get() == '8':
        number = "../images/over_jue8.png"
    elif number.get() == '9':
        number = "../images/over_jue9.png"
    elif number.get() == '10':
        number = "../images/over_jue10.png"
    else:
        exit(0)
    while True:
        click_begin_jue()
        click_over_jue(number)

#点击觉醒挑战按钮
def click_begin_jue():
    while True:
        if lock==1:
            exit(0)
        try:
            x,y=pyautogui.locateCenterOnScreen("../images/begin_jue.png")
            pyautogui.click(x,y)
            return
        except:
            print(time.time())
            time.sleep(0.05)

#点击觉醒结束按钮
def click_over_jue(number):
    while True:
        if lock==1:
            exit(0)
        try:
            x, y = pyautogui.locateCenterOnScreen(number)
            pyautogui.click(x,y)
            for i in range(15):
                time.sleep(0.1)
                pyautogui.doubleClick(x,y)
            return
        except:
            time.sleep(0.1)

#魂土按钮对应的函数，用来启动线程执行--魂土
def huntu_th():
    thread=threading.Thread(target=huntu, daemon=True)
    thread.start()

#----
def huntu():
    while True:
        click_begin_huntu()
        click_over_huntu()

def click_begin_huntu():
    while True:
        if lock==1:
            exit(0)
        try:
            x, y = pyautogui.locateCenterOnScreen("../images/begin_huntu.png")
            pyautogui.click(x, y)
            return
        except:
            time.sleep(0.04)

def click_over_huntu():
    while True:
        if lock==1:
            exit(0)
        try:
            x,y=pyautogui.locateCenterOnScreen("../images/over_huntu.png")
            pyautogui.click(x,y)
            for i in range(16):
                time.sleep(0.2)
                pyautogui.doubleClick(x,y)
            return
        except:
            time.sleep(0.1)






