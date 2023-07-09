import tkinter as tk
from tkinter import messagebox

def add_item():
    new_item = entry.get()
    if new_item.strip() != "":
        todo_list.append(new_item)
        update_listbox()
        entry.delete(0, tk.END)

def remove_item():
    selected_item = listbox.curselection()
    if selected_item:
        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete the task?")
        if confirmation:
            todo_list.pop(selected_item[0])
            update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def edit_item():
    selected_item = listbox.curselection()
    if selected_item:
        item_text = listbox.get(selected_item)
        entry.delete(0, tk.END)
        entry.insert(tk.END, item_text)
        todo_list.pop(selected_item[0])
        update_listbox()
    else:
            messagebox.showwarning("Warning", "Please select a task to edit.")

def toggle_button(*args):
    if entry.get().strip() != "":
        submit_button.config(state=tk.NORMAL)
    else:
        submit_button.config(state=tk.DISABLED)

def update_listbox():
    listbox.delete(0, tk.END)
    for i, item in enumerate(todo_list, start=1):
        listbox.insert(tk.END, f"{i}. {item}")

root = tk.Tk()
root.title("ToDo List")

header = tk.Label(root, text="ToDo List", bg="green", fg="white", font=("Comic Sans MS", 25, "bold"))
header.pack(fill=tk.X, pady=5)

add_items_label = tk.Label(root, text="Add Items", font=("Comic Sans MS", 16))
add_items_label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

submit_button = tk.Button(root, text="Submit", command=add_item, state=tk.DISABLED)
submit_button.pack(pady=5)

listbox = tk.Listbox(root, width=45)
listbox.pack()

delete_button = tk.Button(root, text="Delete", command=remove_item)
delete_button.pack(side=tk.LEFT, pady=5,padx=5)

edit_button = tk.Button(root, text="Edit", command=edit_item)
edit_button.pack(side=tk.LEFT,pady=5, padx=5)

todo_list = []

listbox.bind("<<ListboxSelect>>", toggle_button)
entry.bind("<KeyRelease>", toggle_button)

root.mainloop()
