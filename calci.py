import tkinter as tk

# Button click handler
def press(v):
    entry.insert(tk.END, v)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calc():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Expression")

# Main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# Entry display
entry = tk.Entry(
    root,
    font=("Times New Roman", 20),
    bg="#2d2d2d",
    fg="white",
    bd=0,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)

# Buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

r = 1
c = 0

for b in buttons:
    cmd = calc if b == "=" else lambda x=b: press(x)

    tk.Button(
        root,
        text=b,
        command=cmd,
        font=("Calibri", 14),
        width=5,
        height=2,
        bg="#ff9500" if b in "=+-*/" else "#3a3a3a",
        fg="white",
        bd=0
    ).grid(row=r, column=c, padx=6, pady=6)

    c += 1
    if c == 4:
        r += 1
        c = 0

# Clear button (big)
tk.Button(
    root,
    text="Clear",
    command=clear,
    font=("Calibri", 14),
    width=16,
    height=2,
    bg="#ff3b30",
    fg="white",
    bd=0
).grid(row=r, column=0, columnspan=3, padx=6, pady=6)

# Backspace button (small, beside Clear)
tk.Button(
    root,
    text="B",
    command=backspace,
    font=("Calibri", 14),
    width=5,
    height=2,
    bg="#555555",
    fg="white",
    bd=0
).grid(row=r, column=3, padx=6, pady=6)

# Run app
root.mainloop()
