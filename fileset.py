#import module
from tkinter import *
import tkinter as tk
from tkinter import colorchooser 
import os,shutil
from tkinter.ttk import Combobox
from tkinter import messagebox as m_box

# use tkinter library 
win=Tk()
win.title("set files")
win.geometry('1100x800')

# crate folder function 
def createfolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# this fuction is used to file move in folder
def folder_move(folderName,files):      
    for f in files:
        shutil.move(f, f'{folderName}')

# main fuction this program
def getColor():
    # set bakground color for window 
    color = colorchooser.askcolor(title='') 
    print(color[1])
    win.configure(background=color[1])
    tk.Label(win,text="File set in folder",width=20,borderwidth=10,relief='solid', background=color[1],fg='white',font=('Arial',40)).grid(row=2,column=15,padx=20,pady=10)
    
    # massege 
    tk.Label(win,text="Select folder ",width=15, background=color[1],fg='white',font=('Arial',30)).grid(row=4,column=15,padx=20,pady=10)
    
    # create combobox for folder name 
    folder_var=StringVar()
    combo=Combobox(win,width=20,textvariable=folder_var,height=30,state='readonly',font=15)
    combo['value']=('medias','document','picture','others')
    combo.current(0)
    combo.grid(row=5,column=15,padx=0,pady=30)
    
    #create folder
    def var():
        if folder_var.get() == 'medias':
            createfolder('medias')      
        if folder_var.get() == 'document':
            createfolder('document')
        if folder_var.get() == 'picture':
            createfolder('picture')
        if folder_var.get() == 'others':
            createfolder('others') 
    tk.Button(text="Create folder",background='red',font=15,command=var).grid(row=15,column=15)
    
    # show folder list in message box
    files=os.listdir()
    files.remove('fileset.py')
    mas=Message(win,text=files,font='Arial 15')
    mas.grid(row=18,column=15,padx=0,pady=5)

    #file move for depended extetntion  
    # medias folder
    music=[".mp3",".mp4",".wav",".flv"]
    music_f=[file for file in files if os.path.splitext(file)[1].lower() in music]
    tk.Label(win,text=music,font='Arial 15').grid(row=20,column=10,pady=5,padx=0)
    
    #move file in medias folder
    def move_music():
        if os.path.exists(folder_var.get()):
            if folder_var.get() == 'medias':
                folder_move('medias',music_f)
            if folder_var.get() == 'document':
                folder_move('document',music_f)
            if folder_var.get() == 'picture':
                folder_move('picture',music_f)
            if folder_var.get() == 'others':
                folder_move('others',music_f)
        else:
            m_box.showerror('title','first not create folder for first position in combobox')
    tk.Button(text="move medias file",background='red',font=15,command=move_music).grid(row=22,column=10) 
     
    #file move for depended extetntion  
    #documetn folder  
    dox=[".txt",".docx",".doc",".pdf"]
    documet=[file for file in files if os.path.splitext(file)[1].lower() in dox]
    tk.Label(win,text=dox,font='Arial 15').grid(row=20,column=15,pady=5,padx=0)
    
    #move file in document folder
    def move_dox():
        if os.path.exists(folder_var.get()):
            if folder_var.get() == 'medias':
                folder_move('medias',documet)
            if folder_var.get() == 'document':
                folder_move('document',documet)
            if folder_var.get() == 'picture':
                folder_move('picture',documet)
            if folder_var.get() == 'others':
                folder_move('others',documet)
        else:
            m_box.showerror('title','first not create folder for first position in combobox')
    
    tk.Button(text="move documetn file",background='red',font=15,command=move_dox).grid(row=22,column=15) 
    
    #file move for depended extetntion  
    #picture folder
    img=[".png",".jpg",'.jpeg']
    img_m=[file for file in files if os.path.splitext(file)[1].lower() in img]
    tk.Label(win,text=img,font='Arial 15').grid(row=20,column=17,pady=5,padx=0)
    
    # move image file in picture folder 
    def move_img():
        if os.path.exists(folder_var.get()):
            if folder_var.get() == 'medias':
                folder_move('medias',img_m)
            if folder_var.get() == 'document':
                folder_move('document',img_m)
            if folder_var.get() == 'picture':
                folder_move('picture',img_m)
            if folder_var.get() == 'others':
                folder_move('others',img_m)
        else:
            m_box.showerror('title','first not create folder for first position in combobox')
    tk.Button(text="move imag file",background='red',font=15,command=move_img).grid(row=22,column=17) 
    
    #file move for depended extetntion  
    #others folder
    others=[]
    for file in files:
        ext=os.path.splitext(file)[1].lower()
        if (ext not in music) and (ext not in dox) and (ext not in img) and os.path.isfile(file):
            others.append(file) 
    tk.Label(win,text="others",font='Arial 15').grid(row=24,column=15,pady=5,padx=5)
    
    # move other file in others folder 
    def move_others():
        if os.path.exists(folder_var.get()):
            if folder_var.get() == 'medias':
                folder_move('medias',others)
            if folder_var.get() == 'document':
                folder_move('document',others)
            if folder_var.get() == 'picture':
                folder_move('picture',others)
            if folder_var.get() == 'others':
                folder_move('others',others)
        else:
            m_box.showerror('title','first not create folder for first position in combobox')
    tk.Button(text="move other file",background='red',font=15,command=move_others).grid(row=25,column=15,pady=5,padx=10) 
    
tk.Button(text='Select Color', command=getColor,width=15,height=1,bg='red',fg='blue',font=50).grid(row=0,column=10)

win.mainloop()