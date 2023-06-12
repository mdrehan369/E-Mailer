
from PIL import Image, ImageTk
from os.path import basename
from GUIclass import GUIcustom as GUI
import EmailSendingModule as email
import LoginFormModule as log


adresses = []
to_lb = None
attachments = []
attach_lb = None

adresses = log.updateAddr(adresses)

def send_email1():
    status_var.set("Sending...")
    to_email_lst = to_lb.get(0, "end")
    if attach_lb is not None:
        files = attach_lb.get(0, "end")
    try:
        email.send_email(from_addr=from_addr.get(), to_addr=to_email_lst, subject=subject.get("1.0", "end"), body=body.get("1.0", "end"), files=files)
        status_var.set("Email Sent!")
        status_label.config(bg= "green")
    except:
        status_var.set("Email Not Sent!")
        status_label.config(bg= "red")

def add_reciever_email(event):
    global to_lb
    
    if(to_lb is None):
        to_lb = root.createListbox(toFrame, height=0, width=34, x= 140, y= 40)
        to_lb.bind("<Delete>", deleteOption)

    to_lb.insert("end", to_email.get())
    to_email.set("")
    if(to_lb.size() == 1 or to_lb.size() == 2):
        to_lb.config(height=to_lb.size())
    else:
        to_lb.config(height=3)

def attachfile():
    global attach_lb
    files = root.openFile()


    if files is not None:
        if(attach_lb is None):
            attach_lb = root.createListbox(attachmentFrame, height=0, width= 37, x= 112, y= 33)
            attach_lb.bind("<Delete>", deleteAttach)

        for file in files:
            # attachments.append(file)
            attach_lb.insert("end", file.name)

    if(attach_lb is not None and attach_lb.size() < 5):
        attach_lb.config(height=attach_lb.size())

    elif(attach_lb is not None):
        
        attach_lb.config(height=5)

def updateStatus(event):
     status_var.set("Compose Email")
     status_label.config(bg= "grey")

def deleteAttach(event):

    global attach_lb
    if(attach_lb is not None):
        attach_lb.delete("active")
        if(attach_lb.size() < 5):
            attach_lb.config(height=attach_lb.size())
        if(attach_lb.size() == 0):
            attach_lb.destroy()
            attach_lb = None

def deleteOption(event):

    global to_lb
    if to_lb is not None:
        to_lb.delete("active")
        if(to_lb.size() < 3):
            to_lb.config(height=to_lb.size())
        if(to_lb.size() == 0):
            to_lb.destroy()
            to_lb = None

def changevar(event):
    if(to_email.get() == "Add A New Email Address"):
        to_email.set("")
        toEntry.config(font="lucida 12")
    else:
        toEntry.config(font="lucida 10 italic")
        to_email.set("Add A New Email Address")

    status_var.set("Compose Email")
    status_label.config(bg= "grey")

def copy1(event):
    text = body.selection_get()
    body.clipboard_append(text)

def copy2(event):
    text = subject.selection_get()
    subject.clipboard_append(text)

def cancel():
    global to_email_lst
    global to_lb
    global attachments
    global attach_lb
    to_email_lst = []
    if(to_lb is not None):
        to_lb.destroy()
        to_lb = None
    attachments = []
    if(attach_lb is not None):
        attach_lb.destroy()
        attach_lb = None
    subject.delete("1.0", "end")
    body.delete("1.0", "end")

def login():
    global adresses
    log.loginForm()
    adresses = log.updateAddr(adresses)
    # fromMenu.configure(value=)
    print(adresses)

# def createeLoginWindow():
#     if(adresses is None):
#         win = GUI("Login", 400, 200, False)
#         emaillabel = win.createLabel(win, x= )

root = GUI("E-Mailer", 744, 546, False)

header = root.createFrame(root, bg="#686869", height=20, side="top", fill="x", packpropagate=True)

rawImage = Image.open("logo.jpeg")
rawImage = rawImage.resize((200,200))
img = ImageTk.PhotoImage(image=rawImage)

logo = root.createLabel(header, image=img, side="left", anchor="w", resize=(140, 50))

root.iconphoto(False, img)

bottomFrame = root.createFrame(root, expand=True, fill="x", side="bottom", height=20, packpropagate=True, anchor="s")


leftFrame = root.createFrame(root, width= 50, side= "left", fill="y", height= 60, packpropagate=True)
rightFrame = root.createFrame(root, width= 50, side= "left", fill="y", height= 60, packpropagate=True)



fromFrame = root.createFrame(leftFrame, side="top", width= 50, height=10, fill="x", packpropagate=True, padx = 15)
fromLabel = root.createLabel(fromFrame, side="left", anchor="center", text="From : ", width=12, font="lucida 15")
from_addr = root.createStringvar(root)
from_addr.set("Select your email")
#md.latif2@gmail.com4
fromMenu = root.createOptionmenu(master= fromFrame, variable=from_addr, values=adresses, x= 150, y= 13)

to_email_lst = []
to_email = root.createStringvar(root)
to_email.set("Add A New Email Address")
toFrame = root.createFrame(leftFrame, side="top", width= 50, height=20, fill="x", packpropagate=True)
toLabel = root.createLabel(toFrame, side="left", anchor="n", text="To : ", width=12, font="lucida 15", pady=15, padx = 15)
toEntry = root.createEntry(toFrame, side="right", anchor="n", width=40, ipady=2, padx=5, font="lucida 10 italic", textvar=to_email, pady= 15)
toEntry.bind("<Return>", add_reciever_email)
toEntry.bind("<FocusIn>", changevar)
toEntry.bind("<FocusOut>", changevar)


attachment = root.createStringvar(root)
attachmentFrame = root.createFrame(leftFrame, side="top", width= 50, height=30, fill="x", packpropagate=True)
attachmentLabel = root.createLabel(attachmentFrame, side="left", anchor="n", text="Attachments : ", width=12, font="lucida 15", padx=10)
attachButton = root.createButton(attachmentFrame, "Add An Attachment", command= attachfile, x= 150, y= 7, width=20, bg="grey")

subject = root.createTextarea(rightFrame, 3, 30, 120, 10)
subject_label = root.createLabel(rightFrame, side="left", text="Subject : ", anchor="n",padx=10, font="lucida 15", height=3)
subject.bind("<Control c>", copy2)

body_label = root.createLabel(rightFrame,x=10,y=70, font="lucida 15 ", padx=5, text="Body : ")
body = root.createTextarea(rightFrame, height=11, width=40, x= 10, y= 100)
body.bind("<Control c>", copy1)

send_btn = root.createButton(bottomFrame, "Send", command= send_email1, x = 375, y= 20, bg="#686869", width=8, height=1)
send_btn.config(font="lucida 13")
#bg="#2596be"
cancel_btn = root.createButton(bottomFrame, "Cancel", command= cancel, x = 275, y= 20, bg="#686869", width=8, height=1)
cancel_btn.config(font="lucida 13")

status_var = root.createStringvar(root, "Compose Email")
status_label = root.createLabel(bottomFrame, side="bottom", font="lucida 11 italic", bg= "grey", anchor="w", height=1, fill="x")
status_label.config(textvariable=status_var)
status_label.config(relief="sunken")

root.bind("<Button>", updateStatus)

mymenu = root.createMenu(root, login)
root.mainloop()
