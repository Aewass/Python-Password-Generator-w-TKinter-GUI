
from tkinter import *
import random

root = Tk()
root.geometry("450x300")
root.title("Password Generator")

# intro text
title = StringVar()
label = Label(root, textvariable=title, anchor=N).pack()
title.set("This is a password generator.""\n"" It generates a password based on your choice of password strength.""\n"
          "Please choose one of the following options:")

# choice part


def sel():
    selection = "You have selected the option " + str(choice.get())+"!"
    labelchoice.config(text=selection)


choice = IntVar()
R1 = Radiobutton(root, text="BASIC", variable=choice, value=1, command=sel).pack(anchor=CENTER)
R2 = Radiobutton(root, text="MEDIUM", variable=choice, value=2, command=sel).pack(anchor=CENTER)
R3 = Radiobutton(root, text="EXTRA", variable=choice, value=3, command=sel).pack(anchor=CENTER)
labelchoice = Label(root)
labelchoice.pack()

# pass lenght information
lenlabel = StringVar()
lenlabel.set("""Please choose the lenght of your password:\n
             Minimum amount of characters = 8
             Maximum amount of characters = 24""")
lentitle = Label(root, textvariable=lenlabel).pack()

# pass lenght number
val = IntVar()
spinlenght = Spinbox(root, from_=8, to_=24, textvariable=val).pack()

# passprint


def callback():
    lsum.config(text=passgen())


# clickable button
passgenButton = Button(root, text="Generate Password", relief=RIDGE, bd=5, height=2, command=callback)
passgenButton.pack()
password = str(callback)

# password result message
lsum = Label(root, text="Password: ", anchor=S)
lsum.pack()

# function
lownum = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRQRSTUVWXYZ"
lowupp = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRQRSTUVWXYZ"
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
