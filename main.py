# Write an GUI application that will check Homework submissions and find the student's name who did not submit the homework.
# from all folders with names in the format "Fullname_id_assignsubmission_file" where Fullname is the student's full name,
# Program should check with the list of students from txt file and find the student's name who did not submit the homework.
# Program has a button to select the folder with homework submissions and a button to select the txt file with the list of students.
# Program has a button to start the process.
# Program prints the student's name who did not submit the homework in the text box.

import os
import pandas as pd
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox
from tkinter import simpledialog

# Global variables
# Folder path
folder_path = ""
# Folder path label
folder_path_label = ""
# Txt file path
txt_file_path = ""
# Txt file path label
txt_file_path_label = ""
# List of students
students_list = []
# List of students who did not submit the homework
students_who_did_not_submit = []


# Function to select the folder with homework submissions
def select_folder():
    global folder_path
    folder_selected = filedialog.askdirectory()
    folder_path = folder_selected
    folder_path_label.configure(text=folder_selected)


# Function to select the txt file with the list of students
def select_txt_file():
    global txt_file_path
    txt_file_selected = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    txt_file_path = txt_file_selected
    txt_file_path_label.configure(text=txt_file_selected)


# Function to start the process
def start_process():
    # Check if the folder with homework submissions is selected
    if folder_path == "":
        messagebox.showerror("Error", "Please select the folder with homework submissions")
        return
    # Check if the txt file with the list of students is selected
    if txt_file_path == "":
        messagebox.showerror("Error", "Please select the txt file with the list of students")
        return

    # Read the txt file with the list of students
    global students_list
    students_list = []
    with open(txt_file_path, "r") as txt_file:
        for line in txt_file:
            students_list.append(line.strip())
    # Check if the list of students is empty
    if len(students_list) == 0:
        messagebox.showerror("Error", "List of students is empty")
        return
    # Check if the list of students is not empty
    if len(students_list) != 0:
        # Check if the list of students contains duplicates
        if len(students_list) != len(set(students_list)):
            messagebox.showerror("Error", "List of students contains duplicates")
            return
    # Check if the list of students is not empty
    if len(students_list) != 0:
        # Check if the list of students contains empty strings
        if "" in students_list:
            messagebox.showerror("Error", "List of students contains empty strings")
            return
    # Check if the list of students is not empty
    if len(students_list) != 0:
        # Check if the list of students contains strings with spaces
        if " " in students_list:
            messagebox.showerror("Error", "List of students contains strings with spaces")
            return
    # Check if the list of students is not empty
    if len(students_list) != 0:
        # Check if the list of students contains strings with commas
        if "," in students_list:
            messagebox.showerror("Error", "List of students contains strings with commas")
            return
    # Check if the list of students is not empty
    if len(students_list) != 0:
        # Check if the list of students contains strings with dots
        if "." in students_list:
            messagebox.showerror("Error", "List of students contains strings with dots")
            return
    # Check if the list of students is not empty
    if len(students_list) != 0:
        # Check if the list of students contains strings with slashes
        if "/" in students_list:
            messagebox.showerror("Error", "List of students contains strings with slashes")
            return
        
    # Find the student's name who did not submit the homework
    global students_who_did_not_submit
    students_who_did_not_submit = []
    # Get the list of folders in the folder with homework submissions
    folders_list = os.listdir(folder_path)
    # Check if the list of folders is empty
    if len(folders_list) == 0:
        messagebox.showerror("Error", "Folder with homework submissions is empty")
        return
    
    global start_button
    start_button.configure(state=DISABLED)
    global folder_path_button
    folder_path_button.configure(state=DISABLED)
    global txt_file_path_button
    txt_file_path_button.configure(state=DISABLED)

    # Start the process
    for folder in folders_list:
        # Get the student's name from the folder name
        student_name = folder.split("_")[0]
        # Check if the student's name is in the list of students
        if student_name not in students_list:
            students_who_did_not_submit.append(student_name)
    # Check if the list of students who did not submit the homework is empty
    if len(students_who_did_not_submit) == 0:
        messagebox.showinfo("Info", "All students submitted the homework")
        return
    # Check if the list of students who did not submit the homework is not empty
    if len(students_who_did_not_submit) != 0:
        # Display the list of students who did not submit the homework
        messagebox.showinfo("Info", "Students who did not submit the homework:\n" + "\n".join(students_who_did_not_submit))
        return
    
    start_button.configure(state=NORMAL)
    folder_path_button.configure(state=NORMAL)
    txt_file_path_button.configure(state=NORMAL)

# Run the GUI application
window = Tk()
window.title("Homework submissions")
window.geometry('600x400')

# Folder path label
folder_path_label = Label(window, text="")
folder_path_label.grid(column=0, row=0, padx=10, pady=10)

# Folder path button
folder_path_button = Button(window, text="Select folder with homework submissions", command=select_folder)
folder_path_button.grid(column=0, row=1, padx=10, pady=10)

# Txt file path label
txt_file_path_label = Label(window, text="")
txt_file_path_label.grid(column=0, row=2, padx=10, pady=10)

# Txt file path button
txt_file_path_button = Button(window, text="Select txt file with the list of students", command=select_txt_file)
txt_file_path_button.grid(column=0, row=3, padx=10, pady=10)

# Start button
start_button = Button(window, text="Start", command=start_process)
start_button.grid(column=0, row=4, padx=10, pady=10)

window.mainloop()


