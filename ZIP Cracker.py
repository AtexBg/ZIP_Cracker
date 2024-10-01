import zipfile
import itertools
import string
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_zip(zip_filepath, password):
    try:
        with zipfile.ZipFile(zip_filepath) as zf:
            zf.extractall(pwd=password.encode())
            return True
    except:
        return False

def start_brute_force(zip_filepath, characters, password_length):
    for password in itertools.product(characters, repeat=password_length):
        password = ''.join(password)
        if extract_zip(zip_filepath, password):
            return password
    return None

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Zip files", "*.zip")])
    zip_path_entry.delete(0, tk.END)
    zip_path_entry.insert(0, filename)

def on_start():
    zip_filepath = zip_path_entry.get()
    characters = chars_entry.get()
    password_length = int(length_entry.get())
    
    if not zip_filepath or not characters or not password_length:
        messagebox.showerror("Error", "All fields must be filled")
        return
    
    result = start_brute_force(zip_filepath, characters, password_length)
    
    if result:
        messagebox.showinfo("Success", f'The password is: {result}')
    else:
        messagebox.showerror("Failed", "Password not found")

root = tk.Tk()
root.title("Zip Password Cracker")

tk.Label(root, text="Zip File Path:").grid(row=0, column=0, padx=10, pady=10)
zip_path_entry = tk.Entry(root, width=50)
zip_path_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Characters to use:").grid(row=1, column=0, padx=10, pady=10)
chars_entry = tk.Entry(root, width=50)
chars_entry.insert(0, string.ascii_lowercase + string.digits)
chars_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Password length:").grid(row=2, column=0, padx=10, pady=10)
length_entry = tk.Entry(root, width=50)
length_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Start", command=on_start).grid(row=3, column=1, pady=20)

root.mainloop()
