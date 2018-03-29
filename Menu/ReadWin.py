from tkinter import *
import tkinter as tk
import csv

class ReadWindow(tk.Toplevel):
    """Application class is for a task, which represents
    some capibalities to fill gaps and record information in a file"""

    def __init__(self, master):
        super(ReadWindow, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.listDatafind=[]
        self.title("Reading")
        self.geometry('400x200+30+30')
        self.protocol('WM_DELETE_WINDOW', master.close)


    def close(self):
        self.destroy()

    def create_widgets(self):
        # Enter exam
        self.lblExam = Label(self, text="Ваш ID")
        self.lblExam.grid(column=0, row=0)

        self.entryID = Entry(self)
        self.entryID.grid(column=0, row=1)



        self.searchBtn=Button(self,text="Найти",command=self.findMan)
        self.searchBtn.grid(column=0, row=2)

        listInput=['Фамилия:','Имя:','Отчество:','Пол:','Почта:','Номер:','Количество просмотров:']
        s=0
        for el in listInput:

            self.lblExam4 = Label(self, text=str(el))
            self.lblExam4.grid(column=1, row=s)

            self.lblExam5 = Label(self, text=" N\A")
            self.lblExam5.grid(column=2, row=s)
            s+=1


    def findMan(self):

        idF=str(self.entryID.get())

        num = 0
        n = 0
        with open('hello.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',')  # good point by @paco
            for row in reader:
                for field in row:
                    if str(field) == idF:
                        for i in reader:
                            self.listDatafind.append(i)
                            str1 = ''.join(self.listDatafind[n])
                            self.lblExam9 = Label(self, text=str(str1))
                            self.lblExam9.grid(column=2, row=n)
                            n += 1
                            if 7 == n:
                                 break


def main():
    root = Tk()
    app = ReadWindow(root)
    root.mainloop()  # Для работы окна




