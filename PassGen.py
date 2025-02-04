from tkinter import *
from tkinter import ttk  # For better-looking widgets
import random, string
import platform
import pyperclip  # For copy functionality

root = Tk()
root.geometry("400x500")
root.title("Password Generator")
root.configure(bg='#f0f0f0')  # Light gray background

# Set minimum window size
root.minsize(400, 500)

# Create main frame with padding
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=BOTH, expand=True)

# Styling
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TRadiobutton', font=('Helvetica', 11))
style.configure('TButton', font=('Helvetica', 11))

# Title with better formatting
title_label = ttk.Label(
    main_frame, 
    text="Password Generator", 
    font=('Helvetica', 16, 'bold')
)
title_label.pack(pady=10)

# Strength selection frame
strength_frame = ttk.LabelFrame(main_frame, text="Password Strength", padding="10")
strength_frame.pack(fill=X, pady=10)

choice = IntVar(value=2)  # Default to MEDIUM
strengths = {
    1: ("BASIC", "Letters only"),
    2: ("MEDIUM", "Letters & Numbers"),
    3: ("STRONG", "Letters, Numbers & Symbols")
}

for val, (text, desc) in strengths.items():
    ttk.Radiobutton(
        strength_frame,
        text=f"{text} - {desc}",
        variable=choice,
        value=val
    ).pack(anchor=W, pady=2)

# Length selection frame
length_frame = ttk.LabelFrame(main_frame, text="Password Length", padding="10")
length_frame.pack(fill=X, pady=10)

val = IntVar(value=12)  # Default length
length_spinbox = ttk.Spinbox(
    length_frame,
    from_=8,
    to=32,
    textvariable=val,
    width=10
)
length_spinbox.pack(pady=5)

# Result frame
result_frame = ttk.LabelFrame(main_frame, text="Generated Password", padding="10")
result_frame.pack(fill=X, pady=10)

password_var = StringVar()
password_entry = ttk.Entry(
    result_frame,
    textvariable=password_var,
    font=('Courier', 12),
    justify='center'
)
password_entry.pack(fill=X, pady=5)

def generate_password():
    length = val.get()
    strength = choice.get()
    
    if strength == 1:  # BASIC
        chars = string.ascii_letters
    elif strength == 2:  # MEDIUM
        chars = string.ascii_letters + string.digits
    else:  # STRONG
        chars = string.ascii_letters + string.digits + r"""!@#$%^&*()_-+=[]{}|:;<>,.?"""
    
    # Ensure at least one character from each required set based on strength
    password = []
    if strength >= 1:
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.ascii_uppercase))
    if strength >= 2:
        password.append(random.choice(string.digits))
    if strength >= 3:
        password.append(random.choice(r"""!@#$%^&*()_-+=[]{}|:;<>,.?"""))
    
    # Fill the rest randomly
    remaining_length = length - len(password)
    password.extend(random.choices(chars, k=remaining_length))
    
    # Shuffle the password
    random.shuffle(password)
    result = ''.join(password)
    password_var.set(result)
    return result

def copy_to_clipboard():
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        status_label.config(text="Password copied to clipboard!", foreground="green")
        root.after(2000, lambda: status_label.config(text=""))

# Buttons frame
button_frame = ttk.Frame(main_frame)
button_frame.pack(fill=X, pady=10)

generate_btn = ttk.Button(
    button_frame,
    text="Generate Password",
    command=generate_password
)
generate_btn.pack(side=LEFT, expand=True, padx=5)

copy_btn = ttk.Button(
    button_frame,
    text="Copy to Clipboard",
    command=copy_to_clipboard
)
copy_btn.pack(side=LEFT, expand=True, padx=5)

# Status label for copy confirmation
status_label = ttk.Label(main_frame, text="", font=('Helvetica', 10))
status_label.pack(pady=5)

# Generate initial password
generate_password()

if platform.system() == "Darwin":  # macOS
    root.attributes("-type", "dialog")

root.mainloop()
