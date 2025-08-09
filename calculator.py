import tkinter as tk
reset_display = False

def click(event):
    global reset_display

    current = entry.get()
    button_text = event.widget["text"]

    if button_text == 'C' :
        entry.delete(0, tk.END)
        entry.insert(tk.END, '0')
        reset_display = False
    
    elif button_text == '=':
        try: 
            expression = current.replace('%', '/100')
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
            reset_display = True

        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error!")
            reset_display = True

    else:
        if reset_display:
            entry.delete(0, tk.END)
            current = ""
            reset_display = False

        if current == "0" and button_text.isdigit():
            entry.delete(0, tk.END)
        
        entry.insert(tk.END, button_text)


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


