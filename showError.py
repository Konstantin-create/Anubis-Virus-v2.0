from tkinter import *
import tkinter.messagebox as mb
from PIL import ImageTk


class Error0xC000021A:
    def __init__(self):
        try:
            self.root = Tk()
            self.root.attributes('-fullscreen', True)
            self.root.attributes('-topmost', True)
            self.root['bg'] = "#0000ae"
            self.image = ImageTk.PhotoImage(file="images//fatalError.png")
            self.errorText = Label(self.root, image=self.image, border=0)
            self.errorText.pack()
            self.root.bind("<Escape>", self.close)
            self.root.mainloop()
        except:
            self.root.destroy()

    def close(self, event):
        self.root.destroy()
        sys.exit()


def MbError(title, text):
    root = Tk()
    root.withdraw()
    mb.showerror(str(title), str(text))
    root.destroy()


def MbInfo(title, text):
    root = Tk()
    root.withdraw()
    mb.showinfo(str(title), str(text))
    root.destroy()


def MbQuestion(title, text):
    root = Tk()
    root.withdraw()
    if mb.askyesno(str(title), str(text)):
        root.destroy()
        return True
    else:
        root.destroy()
        return False
