from tkinter import *

def cambia():
    global textp
    textp["text"] = "uwu"

window = Tk()

textp = Label(window,text = "holi")


textp.pack()



boton = Button(window,text = "cambia", command=cambia)
boton.pack()



window.mainloop()


