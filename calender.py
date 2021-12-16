from tkinter import *
import calendar

def scale():
    win2=Tk()
    win2.config(background='white')
    win2.title('CALENDER')
    win2.geometry('700x600')
    fact_year=int(entry.get())
    cal_count=calendar.calendar(fact_year)
    cal_year=Label(win2,text=cal_count,font='Consolas 10 bold')
    cal_year.grid(row=5,column=1)
    win2.mainloop()

if __name__ == '__main__':
    win=Tk()
    win.config(background='white')
    win.geometry('250x350')
    win.title('CALENDER')

    label1=Label(win,text='CALENDER',bg='dark gray',font=('times',28,'bold'))
    label2=Label(win,text='enter year',bg='green',font='times')
    entry=Entry(win,width=20)
    btn1=Button(win,text='Show Calender',bg='red',command=scale)
    btn2=Button(win,text='Exit',bg='red',command=exit)

    label1.grid(row=0,column=1)
    label2.grid(row=1,column=1)
    entry.grid(row=2,column=1)
    btn1.grid(row=3,column=1)
    btn2.grid(row=4,column=1)
    win.mainloop()
    vidioesd

# use calender 