import tkinter as tk
import string
import random
import pyperclip

def generate_password():
    username = username_entry.get()
    password_length = int(password_length_entry.get())

    if password_length <= 0:
        generated_password_entry.delete(0, tk.END)
        generated_password_entry.insert(0, "Invalid password length")
        generated_password_entry.config(fg="red")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        random.seed(username)
        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        generated_password_entry.delete(0, tk.END)
        generated_password_entry.insert(0, generated_password)
        generated_password_entry.config(fg="green")

def reset_fields():
    username_entry.delete(0, tk.END)
    password_length_entry.delete(0, tk.END)
    generated_password_entry.delete(0, tk.END)

def accept_password():
    generated_password = generated_password_entry.get()
    if generated_password:
        pyperclip.copy(generated_password)
        print("Password copied to clipboard.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and format the title label
title_label = tk.Label(root, text="Password Generator", font=("Arial", 16, "underline", "bold"), fg="darkblue")
title_label.grid(row=0, columnspan=2, pady=10)

# Create and format the username label and entry
username_label = tk.Label(root, text="Enter user name:")
username_label.grid(row=1, column=0, pady=5)
username_entry = tk.Entry(root, width=30)
username_entry.grid(row=1, column=1, pady=5)

# Create and format the password length label and entry
password_length_label = tk.Label(root, text="Enter password length:")
password_length_label.grid(row=2, column=0, pady=5)
password_length_entry = tk.Entry(root, width=30)
password_length_entry.grid(row=2, column=1, pady=5)

# Create and format the generated password label and entry
generated_password_label = tk.Label(root, text="Generated password:")
generated_password_label.grid(row=3, column=0, pady=5)
generated_password_entry = tk.Entry(root, width=30)
generated_password_entry.grid(row=3, column=1, pady=5)

# Create the "Generate password" button
generate_button = tk.Button(root, text="GENERATE PASSWORD", bg="darkblue", bd=3, fg="white", command=generate_password)
generate_button.grid(row=4, columnspan=2, pady=10)

# Create the "Accept" button (optional functionality)
accept_button = tk.Button(root, text="ACCEPT", bg="white", bd=3, fg="darkblue", command=accept_password)
accept_button.grid(row=5, columnspan=2, pady=5)

# Create the "Reset" button
reset_button = tk.Button(root, text="RESET", bg="white", bd=3, fg="darkblue", command=reset_fields)
reset_button.grid(row=6, columnspan=2, pady=5)

# Run the main event loop
root.mainloop()
