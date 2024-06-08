from tkinter import *
from tkinter import messagebox, Entry
import ast

window = Tk()
window.title("Login")
window.geometry('925x500+300+200')
window.configure(bg = '#fff')
window.resizable(True,True)


#initializing the signin
def signin():
    username = user.get()
    password = pwd.get()
    d = {username:password}
    loginfile=open('data.txt','r')
    d = loginfile.read()
    r = ast.literal_eval(d)

    if username in r.keys() and password == r[username]:
            window.destroy()
            import Home
    else:
        messagebox.showinfo("Login Failed","You have not logged in")

#changing the page from Login to SignUp
def signup():
    window.destroy()
    import SignUp

#initializing the page
frame = Frame(window,width=350, height=390, bg='white')
frame.place(x=480, y=50)

heading=Label(frame,text='Sign In', fg='pink', bg='white', font =('Comfortaa',23,'bold'))
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


#Buttons

Button(frame,width=39,pady=7,text='Sign In',bg='pink',fg= 'white',border=0,command= signin).place(x=35,y=204)
label= Label(frame, text="Don't have an account?",fg= 'black',bg='white', font=('Comfortaa',9)).place(x=75, y=270)

signin=Button(frame,width=6,text='Sign Up',border=0,bg='white',cursor='hand2',fg='pink',command= signup)
signin.place(x=215,y=270)





window.mainloop()
