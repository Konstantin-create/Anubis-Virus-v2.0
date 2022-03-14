from tkinter import *
from tkvideo import tkvideo


class Interference:
    def __init__(self):
        pass

    def draw(self):
        self.root = Tk()
        self.root["bg"] = "#000"
        self.root.attributes("-topmost", True)
        self.root.attributes("-fullscreen", True)
        self.root.protocol('WM_DELETE_WINDOW', self.user_close)
        my_label = Label(self.root, bg="#000")
        my_label.pack(fill=BOTH)
        player = tkvideo("images/tv.mp4", my_label, loop=1, size=(1920, 1080))
        player.play()
        self.root.mainloop()

    def user_close(self):
        pass

    def close(self):
        self.root.destroy()
        sys.exit()