from GUIclass import GUIcustom as GUI 
import EmailSendingModule as em
from tkinter import messagebox
import pandas as pd

email = None
pwd_entry = None
show = False
pwd = None
win = None
flag = False

def changevar(event):
    if(email.get() == "Enter your email"):
        email.set("")

    elif(email.get() == ""):
        email.set("Enter your email")

def changepass(event):
    if(pwd.get() == "Password"):
        pwd.set("")
    elif(pwd.get() == ""):
        pwd.set("Password")

def showpass():
    global show
    if(show == False):
        pwd_entry.config(show="")
    else:
        pwd_entry.config(show="*")

    show = not show

def updateAddr(adresses):
    df = pd.read_csv("saved emails.csv")
    series = df["ids"]
    ids = list(series)

    for id in ids:
        adresses.append(id)

    return adresses


def login():
    email_id = email.get()
    pwd_id = pwd.get()
    df = pd.read_csv("saved emails.csv")
    df.set_index("ids", inplace=True)
    try:
        if(df.loc[f"{email_id}"]["pass"] == f"{pwd_id}"):
            messagebox.showinfo("Logged in","Already logged in")
            win.destroy()
            return
        
    except:
        pass
        

    if(em.check_login(email_id, pwd_id)):
        messagebox.showinfo("Login successful","Logged in successfully")
        with open("saved emails.csv", "a") as f:
            f.write(f"{email_id},{pwd_id}")
        global flag
        flag = True
        win.destroy()
        return  

    else:
        messagebox.showerror("Login failed","Email address or password is incorrect")


def loginForm():
    global email
    global pwd_entry
    global pwd
    global win

    win = GUI("Login", 350, 250, False)
    login_label = win.createLabel(win, text="Login", font="lucida 20 bold", x= 130, y= 20)
    email = win.createStringvar(win, "Enter your email")
    pwd = win.createStringvar(win, "Password")
    email_entry = win.createEntry(win, x= 55, y= 80, textvar=email, font="lucida 12 italic", width=25)
    pwd_entry = win.createEntry(win, x= 55, y= 120, textvar=pwd, font="lucida 12 italic", width=25)
    pwd_entry.config(show="*")
    pwd_entry.bind("<FocusIn>", changepass)
    pwd_entry.bind("<FocusOut>", changepass)
    email_entry.bind("<FocusIn>", changevar)
    email_entry.bind("<FocusOut>", changevar)

    checkbox = win.createCheckbox(win, 55, 150, "Show Password")
    checkbox.config(command=showpass)

    login_btn = win.createButton(win, "Login", login, x= 135, y= 200, bg= "blue", width=5, height=1)
    login_btn.config(font="lucida 13")
    win.mainloop()
    return flag

# loginForm()