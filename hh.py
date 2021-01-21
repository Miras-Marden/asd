from tkinter import *
import os
from subprocess import call

def open_file():
    os.system('missad.py')
def open_file1():
    os.system('main.py.py')

root = Tk()

btn = Button(root, text='tic tac toe', command=open_file)
btn1 = Button(root, text='tennis', command=open_file1)
btn.pack()
btn1.pack()

def main_menu():
    root = Menu()
    root.mainloop()

root.mainloop()