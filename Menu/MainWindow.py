from tkinter import *
import RecordWindow as rw
import ReadWin as readW


class mainWindow(Frame):
    def __init__(self, master):
        super(mainWindow, self).__init__(master)
        self.grid()
        self.create_widgets()

        self._Rwin = None
        self._ReadWin = None

    def callRecordWindow(self):
        if self._Rwin is not None:
            return
        self._Rwin = rw.RecordWindow(self)

    def callReadWindow(self):
        if self._ReadWin is not None:
            return
        self._ReadWin = readW.ReadWindow(self)

    def close(self):
        self._Rwin.destroy()
        self._ReadWin.destroy()

    def closeAll(self):
        exit()

    def create_widgets(self):
        # Button has a command in order to save data
        self.callRW = Button(self, text="Сделать запись", command=self.callRecordWindow)
        self.callRW.grid(column=0, row=0)

        self.callRW = Button(self, text="Найти запись", command=self.callReadWindow)
        self.callRW.grid(column=0, row=1)

        self.callRW = Button(self, text="Закрыть все окна", command=self.closeAll)
        self.callRW.grid(column=0, row=2)


def main():
    root = Tk()
    root.title("Main Window")
    root.geometry("200x100")
    app = mainWindow(root)
    root.mainloop()  # Для работы окна


main()
