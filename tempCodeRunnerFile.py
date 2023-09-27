import os
import tkinter as tk
from tkinter import filedialog, messagebox

def select_folder():
    folder_path = filedialog.askdirectory(initialdir="C:/Users/tuyen/OneDrive/Documents")
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

def select_file():
    file_path = filedialog.askopenfilename(initialdir="D:/THCS Luat/DSLMH.txt", filetypes=[("Text Files", "*.txt")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def start_process():
    folder_path = folder_entry.get()
    file_path = file_entry.get()

    if not folder_path or not file_path:
        messagebox.showerror("Error", "Please select a folder and a file.")
        return

    student_names = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            student_names.append(line.strip())

    missing_students = []
    for folder_name in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, folder_name)):
            full_name = folder_name.split("_")[0]
            if full_name not in student_names:
                missing_students.append(full_name)

    if missing_students:
        messagebox.showinfo("Missing Students", "The following students did not submit the homework:\n" + "\n".join(missing_students))
    else:
        messagebox.showinfo("Missing Students", "All students submitted the homework.")

# Create the Tkinter window
window = tk.Tk()
window.title("Homework Checker")
window.geometry("400x200")

# Create the folder selection button and entry
folder_label = tk.Label(window, text="Select the folder with homework submissions:")
folder_label.pack()
folder_entry = tk.Entry(window)
folder_entry.pack()
folder_button = tk.Button(window, text="Select Folder", command=select_folder)
folder_button.pack()

# Create the file selection button and entry
file_label = tk.Label(window, text="Select the txt file with the list of students:")
file_label.pack()
file_entry = tk.Entry(window)
file_entry.pack()
file_button = tk.Button(window, text="Select File", command=select_file)
file_button.pack()

# Create the start button
start_button = tk.Button(window, text="Start", command=start_process)
start_button.pack()

# Run the Tkinter event loop
window.mainloop()
