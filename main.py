# import tkinter as t
# from PIL import Image, ImageTk


# #basic root window
# root = t.Tk()
# root.geometry("744x546")
# root.title("E-Mailer")
# root.resizable(0,0)

# #header frame
# header = t.Frame(root, background="red", height=100)
# header.pack(side="top", fill="x")
# header.pack_propagate(0)

# #setting logo
# image = Image.open("basic design.png")
# image = image.resize((100, 50))
# img = ImageTk.PhotoImage(image=image)
# logo = t.Label(header, image=img)
# logo.pack(side="left", anchor="w")

# # setting heading
# heading = t.Label(header, text= "E-Mailer", font="20", bg="red")
# heading.pack(side="left", anchor="center", fill="both", expand=True)

# #Left side frame
# leftFrame = t.Frame(root, bg="green", width=372)
# leftFrame.pack(side="left", fill="y")

# rightFrame = t.Frame(root, bg="blue", width=372)
# rightFrame.pack(side="left", fill="y")

# root.mainloop()

from GUIclass import GUIcustom as GUI

root = GUI("E-Mailer", 744, 546, False)

header = root.createFrame(root, bg="red", height=20, side="top", fill="x", packpropagate=True)

logo = root.createLabel(header, image="basic design.png", side="left", anchor="w", resize=(100, 50))

bottomFrame = root.createFrame(root, bg= "yellow", expand=True, fill="x", side="bottom", height=20, packpropagate=True, anchor="s")

leftFrame = root.createFrame(root, bg= "green", width= 50, side= "left", fill="y", height= 60, packpropagate=True)
rightFrame = root.createFrame(root, bg= "blue", width= 50, side= "left", fill="y", height= 60, packpropagate=True)

fromFrame = root.createFrame(leftFrame, side="top", width= 50, height=20, fill="x", packpropagate=True)
fromLabel = root.createLabel(fromFrame, side="left", anchor="center", text="From : ", width=12, font="lucida 15")
fromEntry = root.createEntry(fromFrame, side="right", anchor="center", width=45, ipady=2, padx=5, expand=True, font="lucida 13")

toFrame = root.createFrame(leftFrame, side="top", width= 50, height=20, fill="x", packpropagate=True)
toLabel = root.createLabel(toFrame, side="left", anchor="center", text="To : ", width=12, font="lucida 15")
toEntry = root.createEntry(toFrame, side="right", anchor="center", width=45, ipady=2, padx=5, expand=True, font="lucida 13")


root.mainloop()
