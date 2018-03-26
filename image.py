from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=1000, height=1000)
canvas.pack()

myimage = PhotoImage(file='C:\\Users\\Gabi\\Documents\\Programowanie\\Python\\cat.gif')
canvas.create_image(0, 0, anchor=NW, image=myimage)
