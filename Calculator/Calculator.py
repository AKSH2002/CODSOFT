import tkinter as tk
import math

def on_button_click(event):
    current = entry.get()
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            # Handling special operations
            if "√" in current:
                index = current.find("√")
                number = float(current[index + 1:])
                result = math.sqrt(number)
            elif "!" in current:
                index = current.find("!")
                number = int(current[:index])
                result = math.factorial(number)
            else:
                result = eval(current)
                
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "<-":
        entry.delete(len(current) - 1)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font=("Arial", 20), bd=5, justify=tk.RIGHT)
entry.pack(padx=10, pady=10, fill=tk.X)

button_frame = tk.Frame(root)
button_frame.pack()

button_texts = [
    "C", "√", "/", "<-",
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "!", "0", ".", "="
]

row = 0
col = 0
for button_text in button_texts:
    button = tk.Button(button_frame, text=button_text, font=("Arial", 20), bd=3, relief=tk.GROOVE)
    button.grid(row=row, column=col, padx=15, pady=8, sticky=tk.NSEW)
    col += 1
    if col > 3:
        col = 0
        row += 1

    button.bind("<Button-1>", on_button_click)

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)
button_frame.columnconfigure(3, weight=1)
button_frame.rowconfigure(0, weight=1)
button_frame.rowconfigure(1, weight=1)
button_frame.rowconfigure(2, weight=1)
button_frame.rowconfigure(3, weight=1)
button_frame.rowconfigure(4, weight=1)

root.mainloop()