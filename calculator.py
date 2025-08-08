import tkinter as tk


def click():
    pass


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)
root.configure(bg="#FFDEF8")

# Entry Widget
entry = tk.Entry(root, bd=5, font=('DS-Digital', 20), justify = 'right', width=18, bg="#f9b6dc")
entry.pack(pady=5)

# Button Frame
btnFrame = tk.Frame(root)
btnFrame.pack(padx=10, pady=10)
btnFrame.configure(bg="#FFDEF8")

# Calculator Buttons
buttons = [['C', '(', ')', '/'],
           ['7', '8', '9', '*'],
           ['4', '5', '6', '-'],
           ['1', '2', '3', '+'],
           ['.', '0', '%', '=']]

for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        btn = tk.Button(btnFrame, text=buttons[i][j],
                        font=('Arial', 16), width=3, height=1,)
        btn.grid(row=i, column=j, padx=10, pady=10)
        btn.configure(bg="#FF89CA")
        btn.bind('<Button-1>', click)

root.mainloop()


