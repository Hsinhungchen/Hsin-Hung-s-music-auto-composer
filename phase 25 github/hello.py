# -*- coding: big5 -*-
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#import wx,string
import tkinter as tk
#from Tkinter import *
#import Tkinter as tk
import inception

pad_x = 180

window = tk.Tk()

window.title('Hsin\'s Music Composer')

window.geometry('500x220')

window.configure(background='black')

var = tk.StringVar()
mode = tk.IntVar()




l = tk.Label(window, fg='snow', bg='black', width=40, text='Please select music style')
l.pack()

def print_selection():
    l.config(text='Press Start to compose')

start_hit = False
#num = 0
#mode = 0



def start():
    global start_hit
    #global num
    if start_hit == False:
       start_hit = True
       l.config(text= 'Composing started!')
       inception.inception(mode.get(), 0)
       l.config(text= 'Composing finished!')
       start_hit = False
    #num = num + 1
    else:
       start_hit = False
       var.set('')

r1 = tk.Radiobutton(window, fg='gray' , bg='black',text='Pop Major Tone', variable=mode, value=0, command=print_selection)
r1.pack(padx = pad_x, anchor = 'w')

r2 = tk.Radiobutton(window, fg='gray' , bg='black',text='Hsin\'s Minor Tone', variable=mode, value=1, command=print_selection)
r2.pack(padx = pad_x, anchor = 'w')

r3 = tk.Radiobutton(window, fg='gray' , bg='black',text='Pop Minor Tone', variable=mode, value=2, command=print_selection)
r3.pack(padx = pad_x, anchor = 'w')

r4 = tk.Radiobutton(window, fg='gray' , bg='black',text='Beyond\'s Tone', variable=mode, value=3, command=print_selection)
r4.pack(padx = pad_x, anchor = 'w')

r5 = tk.Radiobutton(window,  fg='gray' , bg='black', text='Blue Note', variable=mode, value=4, command=print_selection)
r5.pack(padx = pad_x, anchor = 'w')


#font=('Arial', 12)
b = tk.Button(window, text='Start', width=10, height=1, command=start)
b.pack()

img_gif = tk.PhotoImage(file = 'cover_ss-2.gif')
label_img = tk.Label(window, image = img_gif, compound = tk.CENTER)
label_img.pack()

#canvas = tk.Canvas(window, width = 500, height = 300)
#canvas.pack()



# Add a PhotoImage to the Canvas
#canvas.create_image(0, 0, image=img_gif, anchor='nw')


window.mainloop()



