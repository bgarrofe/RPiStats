from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import ImageTk, Image
import time

def quit(*args):
	root.destroy()

def show_stats():
	txt.set(time.strftime("%H:%M:%S"))
	root.after(1000, show_stats)

root = Tk()
root.geometry("480x300")
#root.attributes("-fullscreen", True)
root.configure(background='black')
root.bind("<Escape>", quit)
root.bind("x", quit)
#root.after(1000, show_stats)

# Uptime icon
img = Image.open("uptime.png")
img = img.resize((35, 35), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(root, image=img, background="black")
panel.image = img
panel.place(x=23, y=10)

# Uptime text
fnt = font.Font(family='Helvetica', size=14, weight='bold')
lbl_uptime = ttk.Label(root, text="Uptime", font=fnt, foreground="white", background="black")
lbl_uptime.place(x=70, y=15)

# Uptime value
txt0 = StringVar()
txt0.set("14 d 13 h 20 m 32 s")
fnt = font.Font(family='Helvetica', size=12, weight='bold')
lbl_uptime = ttk.Label(root, textvariable=txt0, font=fnt, foreground="white", background="black")
lbl_uptime.place(x=180, y=17)

# CPU icon
img = Image.open("cpu.png")
img = img.resize((40, 25), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(root, image=img, background="black")
panel.image = img
panel.place(x=20, y=65)

# CPU text
fnt = font.Font(family='Helvetica', size=14, weight='bold')
lbl_cpu = ttk.Label(root, text="CPU", font=fnt, foreground="white", background="black")
lbl_cpu.place(x=70, y=65)

fnt = font.Font(family='Helvetica', size=8, weight='bold')
lbl_cpu0 = ttk.Label(root, text="Core 0\rCore 1\rCore 2\rCore 3", font=fnt, foreground="white", background="black")
lbl_cpu0.place(x=180, y=55)

# CPU bars
canvas = Canvas(root, width=100, height=10, bg="black")
a = canvas.create_rectangle(0, 0, 50, 10, fill='white')
canvas.move(a, 0, 0)
canvas.place(x=225, y=57)

canvas = Canvas(root, width=100, height=10, bg="black")
a = canvas.create_rectangle(0, 0, 30, 10, fill='white')
canvas.move(a, 0, 0)
canvas.place(x=225, y=70)

canvas = Canvas(root, width=100, height=10, bg="black")
a = canvas.create_rectangle(0, 0, 70, 10, fill='white')
canvas.move(a, 0, 0)
canvas.place(x=225, y=83)

canvas = Canvas(root, width=100, height=10, bg="black")
a = canvas.create_rectangle(0, 0, 20, 10, fill='white')
canvas.move(a, 0, 0)
canvas.place(x=225, y=96)

# Memory icon
img = Image.open("memory.png")
img = img.resize((40, 25), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(root, image=img, background="black")
panel.image = img
panel.place(x=20, y=120)

# Memory text
fnt = font.Font(family='Helvetica', size=14, weight='bold')
lbl_memory = ttk.Label(root, text="Memory", font=fnt, foreground="white", background="black")
lbl_memory.place(x=70, y=120)

# Memory bar
canvas = Canvas(root, width=145, height=30, bg="black")
a = canvas.create_rectangle(0, 0, 20, 30, fill='white')
canvas.move(a, 0, 0)
canvas.place(x=180, y=120)

# Memory value
txt1 = StringVar()
txt1.set("Total: 4.0 GB | Free: 1.5 GB")
fnt = font.Font(family='Helvetica', size=8, weight='bold')
lbl_uptime = ttk.Label(root, textvariable=txt1, font=fnt, foreground="white", background="black")
lbl_uptime.place(x=180, y=156)

# Storage icon
img = Image.open("storage.png")
img = img.resize((40, 40), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(root, image=img, background="black")
panel.image = img
panel.place(x=20, y=170)

# Storage text
fnt = font.Font(family='Helvetica', size=14, weight='bold')
lbl_storage = ttk.Label(root, text="Storage", font=fnt, foreground="white", background="black")
lbl_storage.place(x=70, y=180)

# Storage
fnt = font.Font(family='Helvetica', size=8, weight='bold')
lbl_cpu0 = ttk.Label(root, text="/sda0\r\r/sda1", font=fnt, foreground="white", background="black")
lbl_cpu0.place(x=180, y=180)

canvas = Canvas(root, width=100, height=10, bg="black")
a = canvas.create_rectangle(0, 0, 50, 10, fill='white')
canvas.move(a, 0, 0)
canvas.place(x=225, y=180)

canvas = Canvas(root, width=100, height=10, bg="black")
a = canvas.create_rectangle(0, 0, 30, 10, fill='white')
canvas.move(a, 0, 0)
canvas.place(x=225, y=210)

# IP icon
img = Image.open("ip.png")
img = img.resize((40, 40), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(root, image=img, background="black")
panel.image = img
panel.place(x=20, y=230)

# IP text
fnt = font.Font(family='Helvetica', size=14, weight='bold')
lbl_ip = ttk.Label(root, text="IP", font=fnt, foreground="white", background="black")
lbl_ip.place(x=70, y=240)

# IP Value
txt2 = StringVar()
txt2.set("192.168.0.2")
fnt = font.Font(family='Helvetica', size=14, weight='bold')
lbl_uptime = ttk.Label(root, textvariable=txt2, font=fnt, foreground="white", background="black")
lbl_uptime.place(x=180, y=240)

def helloCallBack():
   pass

# Reboot button
fnt = font.Font(family='Helvetica', size=12, weight='bold')
btn_Reboot = Button(root, text ="REBOOT", font=fnt, width=10, height=2, command = helloCallBack)
btn_Reboot.place(x=360, y=10)

# Shutdown button
btn_Shutdown = Button(root, text ="SHUTDOWN", width=10, height=2, font=fnt, command = helloCallBack)
btn_Shutdown.place(x=360, y=120)

# Quit button
btn_Quit = Button(root, text ="QUIT", width=10, height=2, font=fnt, command = helloCallBack)
btn_Quit.place(x=360, y=240)

root.mainloop()