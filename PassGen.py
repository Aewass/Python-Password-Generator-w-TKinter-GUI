
from tkinter import *
import random, string

root = Tk()
root.geometry("400x280")
root.title("Password Generator")
root.attributes("-toolwindow", 1)
root.resizable(width=FALSE, height=FALSE)


# intro text
title = StringVar()
label = Label(root, textvariable=title, anchor=N, pady=10).pack()
title.set("Password strength:")

# choice part


def sel():
    selection = choice.get()

choice = IntVar()
R1 = Radiobutton(root, text="BASIC", variable=choice, value=1, command=sel).pack(anchor=CENTER)
R2 = Radiobutton(root, text="MEDIUM", variable=choice, value=2, command=sel).pack(anchor=CENTER)
R3 = Radiobutton(root, text="EXTRA", variable=choice, value=3, command=sel).pack(anchor=CENTER)
labelchoice = Label(root)
labelchoice.pack()

# pass lenght information
lenlabel = StringVar()
lenlabel.set("Password length:")
lentitle = Label(root, textvariable=lenlabel).pack()

# pass lenght number
val = IntVar()
spinlenght = Spinbox(root, from_=8, to_=24, textvariable=val, width=13).pack()

# passprint


def callback():
    lsum.config(text=passgen())


# clickable button
passgenButton = Button(root, text="Generate Password", relief=RIDGE, bd=5, height=2, command=callback, pady=3)
passgenButton.pack()
password = str(callback)

# password result message
lsum = Label(root, text="")
lsum.pack(side=BOTTOM)

# function
lownum = string.ascii_uppercase + string.ascii_lowercase + string.digits
lowupp = string.ascii_uppercase + string.ascii_lowercase
symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
everything = lowupp + lownum + symbols


def passgen():
    if choice.get() == 1:
        return "".join(random.sample(lowupp, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(lownum, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(everything, val.get()))


root.mainloop()
