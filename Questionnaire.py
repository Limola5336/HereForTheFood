import openpyxl
from tkinter import *
from tkinter import messagebox

questionnaire = Tk()
# Create the main tkinter window
questionnaire.title("Questionnaire")
questionnaire.geometry('300x300')

def submitFormExcl():
    # Get the user input from the form
    first_name = first_name_entry.get()
    Last_name = Last_name_entry.get()
    email = email_entry.get()
    Mobile = Mobile_entry.get()

    # Create a new row with the user input
    new_row = [first_name, Last_name, email,Mobile]

    # Append the new row to the Excel sheet
    workbook = openpyxl.load_workbook("user_form_data.xlsx")
    sheet = workbook.active
    sheet.append(new_row)
    workbook.save("registration_data.xlsx")
    messagebox.showinfo("Success", "Profile Made!")

def submitFormTxt():
    # Get the user input from the form
    first_name = first_name_entry.get()
    Last_name = Last_name_entry.get()
    email = email_entry.get()
    Mobile = Mobile_entry.get()

    file = open(first_name + " " + Last_name + ".txt", "w")
    file.write(first_name + "\n" + Last_name + "\n" + email + "\n" + Mobile)
    file.close()
    questionnaire.destroy()



# Create labels and entry fields for each input
first_name_label = Label(questionnaire, text="First Name:")
first_name_label.pack()
first_name_entry = Entry(questionnaire)
first_name_entry.pack()

Last_name_label = Label(questionnaire, text="Last Name:")
Last_name_label.pack()
Last_name_entry = Entry(questionnaire)
Last_name_entry.pack()

email_label = Label(questionnaire, text="Email:")
email_label.pack()
email_entry = Entry(questionnaire)
email_entry.pack()

Mobile_label = Label(questionnaire, text="Mobile:")
Mobile_label.pack()
Mobile_entry = Entry(questionnaire)
Mobile_entry.pack()

submit_button = Button(questionnaire, text="Submit", command=submitFormTxt)
submit_button.pack()

questionnaire.mainloop()