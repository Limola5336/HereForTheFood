from tkinter import *
from tkinter import messagebox, Entry
import ast

window = Tk()
window.title("Sign Up")
window.geometry('925x500+300+200')
window.configure(bg = '#fff')
window.resizable(True,True)

#change to the Login page
def signin():
    window.destroy()
    import Login


#initializing signing up
def signup():
    username=user.get()
    password=pwd.get()
    con_password = con_pwd.get()

    if password==con_password:
        try:
            file=open('data.txt','r+')
            datareader=file.read()
            r=ast.literal_eval(datareader)

            dict_data={username:password}
            r.update(dict_data)
            file.truncate(0)
            file.close()

            file=open('data.txt','w')
            file.write(str(r))
            messagebox.showinfo('Sign Up Successfully','You have successfully signed up')

        except:
            file=open('data.txt','w')
            pp=str({"Username":"Password"})
            file.write(pp)
            file.close()
    else:
        messagebox.showerror('Invalid','Passwords did not match')


frame = Frame(window,width=350, height=390, bg='white')
frame.place(x=480, y=50)

heading=Label(frame,text='Sign Up', fg='pink', bg='white', font =('Comfortaa',23,'bold'))
heading.place(x=100, y=5)

#username field
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')
user=Entry(frame,width=25, fg='black', border=2, bg='white',font =('Comfortaa',11,))
user.place(x=30, y=80)
user.insert(0,'Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame,width=295, height =2, bg='black').place(x=25,y=107)

#Password field
def on_enter(e):
    pwd.delete(0,'end')
def on_leave(e):
    if pwd.get()=='':
        pwd.insert(0,'Password')
pwd=Entry(frame,width=25, fg='black', border=2, bg='white',font =('Comfortaa',11,))
pwd.place(x=30, y=150)
pwd.insert(0,'Password')
pwd.bind("<FocusIn>", on_enter)
pwd.bind("<FocusOut>", on_leave)

Frame(frame,width=295, height =2, bg='black').place(x=25,y=177)

#Confirm Password field
def on_enter(e):
    con_pwd.delete(0,'end')
def on_leave(e):
    if con_pwd.get()=='':
        con_pwd.insert(0,'Confirm Password')
con_pwd=Entry(frame,width=25, fg='black', border=2, bg='white',font =('Comfortaa',11,))
con_pwd.place(x=30, y=220)
con_pwd.insert(0,'Confirm Password')
con_pwd.bind("<FocusIn>", on_enter)
con_pwd.bind("<FocusOut>", on_leave)

Frame(frame,width=295, height =2, bg='black').place(x=25,y=247)

#Buttons

Button(frame,width=39,pady=7,text='Sign Up',bg='pink',fg= 'white',border=0,command=signup).place(x=35,y=280)
label= Label(frame, text="I have an account",fg= 'black',bg='white', font=('Comfortaa',9)).place(x=90, y=340)

signin=Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='pink',command = signin)
signin.place(x=200,y=340)





window.mainloop()