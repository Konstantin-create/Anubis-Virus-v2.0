import os
from tkinter import *
from PIL import ImageTk


class ShowImage:
    def __init__(self):
        pass

    def show(self):
        self.root = Tk()
        self.root['bg'] = "#000"
        self.root.attributes("-topmost", True)
        self.root.attributes("-fullscreen", True)
        self.image = ImageTk.PhotoImage(file="image.jpg")
        os.remove("image.jpg")
        self.imageLabel = Label(self.root, image=self.image)
        self.imageLabel.pack()
        self.root.bind("<Escape>", self.close)
        self.root.mainloop()

    def close(self, event):
        try:
            self.root.destroy()
            sys.exit()
        except:
            pass


class ShowWindow:
    def __init__(self):
        pass

    def draw(self, title, geometry, bg_color, fg_color, labelText):
        self.root = Tk()
        self.root.title(str(title))
        self.root.attributes("-topmost", True)
        self.root.geometry(str(geometry))
        self.root["bg"] = str(bg_color)
        Label(self.root, text=str(labelText), font=("Arial", 50), bg=bg_color, fg=fg_color).pack(anchor=CENTER)
        self.root.mainloop()

    def close(self):
        try:
            self.root.destroy()
            sys.exit()
        except:
            pass
