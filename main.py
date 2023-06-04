import tkinter as t
from PIL import Image, ImageTk


#basic root window
root = t.Tk()
root.geometry("744x546")
root.title("E-Mailer")
root.resizable(0,0)

#header frame
header = t.Frame(root, background="red", height=100)
header.pack(side="top", fill="x")
header.pack_propagate(0)

#setting logo
image = Image.open("basic design.png")
image = image.resize((100, 50))
img = ImageTk.PhotoImage(image=image)
logo = t.Label(header, image=img)
logo.pack(side="left", anchor="w")

# setting heading
heading = t.Label(header, text= "E-Mailer", font="20", bg="red")
heading.pack(side="left", anchor="center", fill="both", expand=True)

#Left side frame
leftFrame = t.Frame(root, bg="green", width=372)
leftFrame.pack(side="left", fill="y")

rightFrame = t.Frame(root, bg="blue", width=372)
rightFrame.pack(side="left", fill="y")

root.mainloop()