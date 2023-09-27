# Write an GUI application that will check Homework submissions and find the student's name who did not submit the homework.
# from all folders with names in the format "Fullname_id_assignsubmission_file" where Fullname is the student's full name,
# Program should check with the list of students from txt file and find the student's name who did not submit the homework.
# Program has a button to select the folder with homework submissions and a button to select the txt file with the list of students.
# Program has a button to start the process.
# Program displays the student's name who did not submit the homework in the text box.

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
import openpyxl

def select_folder():
    folder_path = filedialog.askdirectory(initialdir="C:/Users/tuyen/OneDrive/Documents")
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

def select_file():
    file_path = filedialog.askopenfilename(initialdir="D:/THCS Luat", filetypes=[("Text Files", "*.txt")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def start_process():
    folder_path = folder_entry.get()
    file_path = file_entry.get()

    if not folder_path or not file_path:
        messagebox.showerror("Error", "Please select a folder and a file.")
        return

    if not os.path.exists(file_path):
        messagebox.showerror("Error", "The selected file does not exist.")
        return

    student_names = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            student_names.append(line.strip())

    missing_students = []
    submitted_students = []
    for folder_name in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, folder_name)):
            full_name = folder_name.split("_")[0]
            # if full_name exists in student_names, this student submitted the homework
            submitted_students.append(full_name)

    for student_name in student_names:
        if student_name not in submitted_students:
            missing_students.append(student_name)
    
    if missing_students:
        messagebox.showinfo("Missing Students", "The following students did not submit the homework:\n" + "\n".join(missing_students))
        write_to_excel(missing_students)
    else:
        messagebox.showinfo("Missing Students", "All students submitted the homework.")

def write_to_excel(missing_students):
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d_%H%M%S")
    filename = "D:/THCS Luat/students_did_not_hw_" + dt_string + ".xlsx"

    workbook = openpyxl.Workbook()
    worksheet = workbook.create_sheet("Missing Students", 0)

    for student in missing_students:
        worksheet.append([student])

    workbook.save(filename)
    messagebox.showinfo("Excel File Created", "The list of missing students has been saved to " + filename)

# Create the Tkinter window
window = tk.Tk()
window.title("Homework Checker")
window.geometry("400x250")

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

