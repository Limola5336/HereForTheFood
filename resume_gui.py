import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from resume_generator import generate_resume, generate_work_history, generate_education
from openpyxl import Workbook
from rake_nltk import Rake
import nltk
import os


# Objectives:
# Fill in the fields, and have those data be used to fill in resume templates
# Showing templates, allow user to refresh or confirm, or even refill the resume
root = tk.Tk()
root.title("AI Resume Generator")

# Questions for the user
questions = [
    "Name",
    "Age",
    "Gender",
    "Professional Experience (years)",
    "Qualification",
    "Achievements",
    "Work Locations (comma-separated)",
    "Roles (comma-separated)",
    "Email",
    "Phone",
    "Address",
    "Skills (comma-separated)",
    "Schools (comma-separated)",
    "Year(s) of Graduation (comma-separated)", #okay might delete, or maybe not nevermind lazy
    "Degrees (comma-separated)"
]

def submit_form():

    answers = [entry.get() for entry in entry_fields]
    # save_to_excel(answers)
    generate_and_show_resume(answers)


def generate_and_show_resume(answers):
    resume = generate_resume({
        "name": answers[0],
        "age": answers[1],
        "gender": answers[2],
        "experience": answers[3],
        "qualification": answers[4],
        "achievements": answers[5],
        "locations": answers[6].split(','),
        "roles": answers[7].split(','),
        "email": answers[8],
        "phone": answers[9],
        "address": answers[10],
        "skills": answers[11].split(','),
        "schools": answers[12].split(','),
        "years": answers[13].split(','),
        "degrees": answers[14].split(',')
    })
    show_resume_popup(resume, answers)


# def save_to_excel(answers):
#     wb = Workbook()
#     ws = wb.active
#     ws.append(questions)
#     ws.append(answers)
#     wb.save("user_responses.xlsx")


def clear_form():
    for entry in entry_fields:
        entry.delete(0, tk.END)

#Generating templates for resume
def show_resume_popup(resume, answers):
    popup = tk.Toplevel(root)
    popup.title("Generated Resume")
    root_x = root.winfo_x()
    root_y = root.winfo_y()
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    #MATHS!...... -.-
    popup.geometry(f"500x500+{root_x + root_width // 2 - 200}+{root_y + root_height // 2 - 200}")
    popup.resizable(False, False)

    font_style = tkFont.Font(family="Helvetica", size=12)
    resume_label = tk.Label(popup, text=resume, justify="left", wraplength=450, font=font_style)
    resume_label.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    button_frame = tk.Frame(popup)
    button_frame.pack(pady=10)

    ok_button = tk.Button(button_frame, text="Refill", command=lambda: close_popup_and_clear_form(popup)) #Yeah this works..... shlda done this from the start
    ok_button.pack(side="left", padx=5)

    refresh_button = tk.Button(button_frame, text="Refresh Resume", command=lambda: refresh_resume(answers, popup))
    refresh_button.pack(side="right", padx=5)

    confirm_button = tk.Button(button_frame, text="Confirm", command=lambda: confirm_resume(resume))
    confirm_button.pack(side="right", padx=5)

def close_popup_and_clear_form(popup):
    popup.destroy()
    clear_form()
def refresh_resume(answers, popup):
    popup.destroy()
    generate_and_show_resume(answers)

def confirm_resume(resume):
    # Save the resume to a new file
    file_index = 1
    while os.path.exists(f"resume_{file_index}.txt"):
        file_index += 1
    with open(f"resume_{file_index}.txt", "w") as file:
        file.write(resume)
    messagebox.showinfo("Confirmed", f"Resume saved as resume_{file_index}.txt")


#Labeling
entry_fields = []

for i, question in enumerate(questions):
    label = tk.Label(root, text=question + ":")
    label.grid(row=i, column=0, sticky="e", padx=10, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entry_fields.append(entry)
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=len(questions), columnspan=2, pady=10)


root.mainloop()
