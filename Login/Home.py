from tkinter import *
from tkinter import Entry


Homewind = Tk()
Homewind.title("Home")
Homewind.geometry('875x500+300+50')
Homewind.configure(bg = '#fff')
Homewind.resizable(FALSE,FALSE)

nav = PhotoImage(file = "Images/Rectangle 2.png")
inbox=PhotoImage(file = "Images/inbox.png")
wish=PhotoImage(file = "Images/lblwish.png")
notif=PhotoImage(file = "Images/notif.png")
prof=PhotoImage(file = "Images/myprof.png")

navigation = Frame(Homewind,width=250, height=500)
navigation.place(x=0, y=0)
NavLabel = Label(navigation, image = nav)
NavLabel.place(x = 0, y = -1)


searchframe = Frame(Homewind,width=650, height=500, bg='white')
searchframe.place(x=250, y=0)


def on_enter(e):
    Search.delete(0,'end')
def on_leave(e):
    if Search.get()==" ":
        Search.insert(0,'Search🔍')

Search = Entry(searchframe,width=85,fg='grey',borderwidth=0,bg='white',font=('Comfortaa',11))
Search.place(x=10,y=5)
Search.insert(0,'Search🔍')
Search.bind("<FocusIn>",on_enter)
Search.bind("<FocusOut>",on_leave)

contentframe = Frame(Homewind,width=600, height=460, bg='#F1F1F1')
contentframe.place(x=260, y=40)

chatbot = Button(contentframe,text="Let's Talk\n🤖",border=0,fg='black',bg='pink',font=('Comfortaa',20))
chatbot.place(x=420,y=390)

MyProfile = Button(navigation,text="My Profile",border=0,fg='black',bg='pink',font=('Comfortaa',20),width=15)
MyProfile.place(x=10,y=10)

def openinbox():
    inbox_Homewind = Toplevel(Homewind)
    inbox_Homewind.title("Inbox")
    inbox_Homewind.geometry('900x500+300+50')
    inbox_Homewind.configure(bg='#fff')
    inbox_Homewind.resizable(FALSE, FALSE)
    Inblbl= Label(inbox_Homewind, image=inbox)
    Inblbl.pack()

Inbox = Button(navigation, text="Inbox", borderwidth=0, fg='black', bg='pink', font=('Comfortaa', 20), command=openinbox)
Inbox.place(x=10, y=200)
Inbox = Button(navigation,text="Inbox",border=0,fg='black',bg='pink',font=('Comfortaa',20), command= openinbox)
Inbox.place(x=10,y=200)


def openwish():
    open_wish = Toplevel(Homewind)
    open_wish.title("Wishlist")
    open_wish.geometry('900x500+300+50')
    open_wish.configure(bg='#fff')
    open_wish.resizable(FALSE, FALSE)
    Wishlbl = Label(open_wish, image=wish)
    Wishlbl.pack()
Wishlist = Button(navigation,text="Wishlist",border=0,fg='black',bg='pink',font=('Comfortaa',20), command=openwish)
Wishlist.place(x=10,y=250)

def openapp():
    open_app = Toplevel(Homewind)
    open_app.title("Resume Generator")
    open_app.geometry('900x500+300+50')
    open_app.configure(bg='#fff')
    open_app.resizable(FALSE, FALSE)
Applications = Button(navigation,text="Resume Generator",border=0, fg='black',bg='pink',font=('Comfortaa',20),command=openapp)
Applications.place(x=10,y=300)


def opennotif():
    open_notif = Toplevel(Homewind)
    open_notif.title("Notifications")
    open_notif.geometry('900x500+300+50')
    open_notif.configure(bg='#fff')
    open_notif.resizable(FALSE, FALSE)
    Notiflbl = Label(open_notif, image=notif)
    Notiflbl.pack()
Notifications = Button(navigation,text="Notifications",border=0,fg='black',bg='pink',font=('Comfortaa',20),command=opennotif)
Notifications.place(x=10,y=350)

def opensett():
    open_sett = Toplevel(Homewind)
    open_sett.title("Settings")
    open_sett.geometry('900x500+300+50')
    open_sett.configure(bg='#fff')
    open_sett.resizable(FALSE, FALSE)


    b1 = Button(open_sett, text="My Information", border=0, fg='black', bg='pink', font=('Comfortaa', 20), width=70, height=1)
    b1.place(x=10, y=10)
    b2 = Button(open_sett, text="Appearance", border=0, fg='black', bg='pink', font=('Comfortaa', 20), width=70, height=1)
    b2.place(x=10, y=70)
    b3 = Button(open_sett, text="Language", border=0, fg='black', bg='pink', font=('Comfortaa', 20), width=70,height=1)
    b3.place(x=10, y=130)
    b4 = Button(open_sett, text="Notifications", border=0, fg='black', bg='pink', font=('Comfortaa', 20), width=70, height=1)
    b4.place(x=10, y=190)
    b5 = Button(open_sett, text="Customer Support", border=0, fg='black', bg='pink', font=('Comfortaa', 20), width=70, height=1)
    b5.place(x=10, y=250)
    b6 = Button(open_sett, text="Delete Account", border=0, fg='black', bg='pink', font=('Comfortaa', 20), width=70,height=1)
    b6.place(x=10, y=310)

Settings = Button(navigation,text="Settings",border=0,fg='black',bg='pink',font=('Comfortaa',20),command=opensett)
Settings.place(x=10,y=400)

def logoutbtn():
    Homewind.destroy()
Logout = Button(navigation,text="Logout",border=0,fg='black',bg='pink',font=('Comfortaa',20),command=logoutbtn)
Logout.place(x=10,y=450)


Homewind.mainloop()