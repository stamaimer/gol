# -*- coding: utf-8 -*-

from Tkinter import *


class GameOfLife(Frame):

    def __init__(self, parent):

        Frame.__init__(self, parent)

        self.parent = parent

        self.choice = IntVar()

        self.initUI()

    def next_callback(self):

        tmp_frame = Frame(self)
        tmp_frame.pack(fill=BOTH, expand=True)

        label = Label(tmp_frame, text=str(self.choice.get()))
        label.pack()

    def initUI(self):

        self.parent.title("Game of Life")

        self.pack(fill=BOTH, expand=True)

        top_frame = Frame(self)
        top_frame.pack(fill=BOTH, expand=True)

        Radiobutton(top_frame, text=u"文件", variable=self.choice, value=1).pack(side="left")
        Radiobutton(top_frame, text=u"随机", variable=self.choice, value=2).pack(side="left")
        Radiobutton(top_frame, text=u"点击", variable=self.choice, value=3).pack(side="left")

        next_button = Button(top_frame, text=u"下一步", command=self.next_callback)
        next_button.pack(side="left")




def main():

    root = Tk()

    GameOfLife(root)

    root.mainloop()


if __name__ == '__main__':

    main()
