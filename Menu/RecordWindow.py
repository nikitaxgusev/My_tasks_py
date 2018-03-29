from tkinter import *
import tkinter as tk
import csv

class RecordWindow(tk.Toplevel):
    """Application class is for a task, which represents
    some capibalities to fill gaps and record information in a file"""

    def __init__(self, master):
        super(RecordWindow, self).__init__(master)
        self.grid()
        self.listData = []
        self.create_widgets()
        self.cleanGaps()
        self.title("Recording")
        self.geometry('400x370+30+30')
        self.protocol('WM_DELETE_WINDOW', master.close)


    def close(self):
        self.destroy()

    def create_widgets(self):
        """Create widgets for a main window"""
        self.numc = 0
        with open('hello.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',')  # good point by @paco
            for row in reader:
                for field in row:
                    if str(field) == 'c':
                        self.numc += 1

        listInput = ['Фамилия:', 'Имя:', 'Отчество:', 'Пол:', 'Почта:', 'Номер:', 'Количество просмотров:']
        s=1
        for el in listInput:

            self.lblExam4 = Label(self, text=str(el))
            self.lblExam4.grid(column=0, row=s)
            s+=2

        self.StatusR = Label(self, text="Cтатус записи:")
        self.StatusR.grid(column=1, row=0)

        self.StatusR = Label(self, text="Ваш ID:"+str(self.numc))
        self.StatusR.grid(column=0, row=0)



        self.entrySurName = Entry(self)
        self.entrySurName.grid(column=0, row=2)



        self.entryName = Entry(self)
        self.entryName.grid(column=0, row=4)



        self.entrySecName = Entry(self)
        self.entrySecName.grid(column=0, row=6)

        self.v = StringVar()
        self.rSexBtnM = Radiobutton(self, text="M", value="М", var=self.v)
        self.rSexBtnM.grid(column=0, sticky=W, row=7)

        self.rSexBtnM = Radiobutton(self, text="Ж", value="Ж",var=self.v)
        self.rSexBtnM.grid(column=0, sticky=E, row=7)



        self.entrySubject = Entry(self)
        self.entrySubject.grid(column=0, row=10)



        self.entryExam = Entry(self)
        self.entryExam.grid(column=0, row=12)


        self.entryDirection = Entry(self)
        self.entryDirection.grid(column=0, row=14)

        # Button has a command in order to save data

        self.btnSave = Button(self, text="Записать", state=NORMAL, command=self.saveData,height = 1, width = 18)
        self.btnSave.grid(column=0, row=17)

        self.cleanGapsBtn = Button(self, text="Очистить поля", command=self.cleanGaps,height = 1, width = 18)
        self.cleanGapsBtn.grid(row=16, column=0)


        self.callRW = Button(self, text="Закрыть", command=self.close,height = 1, width = 18)
        self.callRW.grid(column=0, row=18)



    def saveData(self):

        self.listData.append(str(self.numc))
        if len(self.entrySurName.get()) != 0:
            self.SurName = self.entrySurName.get()
            self.listData.append(self.SurName)

            if len(self.entryName.get()) != 0:
                self.Name = self.entryName.get()
                self.listData.append(self.Name)

                if len(self.entrySecName.get()) != 0:
                    self.SecName = self.entrySecName.get()
                    self.listData.append(self.SecName)

                    value = self.v.get()

                    if 'Ж' == value:
                        self.listData.append('Жен')
                    if 'М' == value:
                        self.listData.append('Муж')

                    if len(self.entrySubject.get()) != 0:
                        self.Subject = self.entrySubject.get()
                        self.listData.append(self.Subject)

                        if len(self.entryExam.get()) != 0:
                            self.Exam = self.entryExam.get()
                            self.listData.append(self.Exam)

                            if len(self.entryDirection.get()) != 0:
                                self.Direction = self.entryDirection.get()
                                self.listData.append(self.Direction)




                                if ''!=value:


                                    fileSaveData=open('hello.csv','a')
                                    num = 0
                                    for i in self.listData:
                                        fileSaveData.write(i+'\n')
                                        num += 1
                                    fileSaveData.write('c')
                                    fileSaveData.write('\n\n')
                                    self.cleanGaps()



                                    self.messW = Label(self, text="Ваша запись была учтена.")
                                    self.messW.grid(column=2, row=0)
                                    self.numc+=1
                                    self.StatusR = Label(self, text="Ваш ID:" + str(self.numc))
                                    self.StatusR.grid(column=0, row=0)


                                else:
                                    self.messWarning()

                            else:
                                self.messWarning()
                    else:
                        self.messWarning()
                else:
                    self.messWarning()
            else:
                self.messWarning()
        else:
            self.messWarning()


    def cleanGaps(self):
        """cleanGaps() is for cleaning filling gaps"""
        self.listData.clear()
        self.entryName.delete(0, END)
        self.entrySurName.delete(0, END)
        self.entrySecName.delete(0, END)
        self.entrySubject.delete(0, END)
        self.entryExam.delete(0, END)
        self.entryDirection.delete(0, END)

    def messWarning(self):
        self.messW = Label(self, text="Заполните все поля!")
        self.messW.grid(column=2, row=0)

        self.cleanGaps()

def main():
    root = Tk()
    app = RecordWindow(root)
    root.mainloop()  # Для работы окна




