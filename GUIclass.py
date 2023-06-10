import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfiles
# from tkinter import messagebox

class GUIcustom(tk.Tk):

    def __init__(self, title, width, height, resizable = True):

        super().__init__()
        # self.title = title
        self.width = width
        self.height = height

        self.title(title)
        self.geometry(f"{width}x{height}")

        if(resizable == False):
            self.resizable(0,0)

    def getPixels(self, percent, what):

        if(percent == 0):
            return None

        if(what == "width"):
            return (percent / 100) * self.width
        
        else:
            return (percent / 100) * self.height

    def setImage(self, imageFile, resize):

        rawImage = Image.open(imageFile)
        rawImage = rawImage.resize(resize)
        image = ImageTk.PhotoImage(image = rawImage)

        return image
        
    def createFrame(self, master, side, packpropagate = False, expand= False, height= 0, width= 0, fill= "none", padx= 0, pady= 0, anchor= "center", bg= None):

        frame = tk.Frame(master = master, bg = bg, height=self.getPixels(height, "height"), width = self.getPixels(width, "width"))
        frame.pack(side = side, fill = fill, expand=expand, padx=padx, pady= pady, anchor=anchor)

        if(packpropagate == True):
            frame.pack_propagate(0);

        return frame

    def createLabel(self, master, side="top", fill= "none", expand= False, text= None, image= None, resize= (0,0), padx= 0, pady= 0, anchor= "center", bg= None, width=0, height=0, font="lucida", x= None, y= None):

        label = tk.Label(master= master, bg = bg, text= text, image= image, width=width, height=height, font=font, anchor="w")
        if(x is None):
            label.pack(side=side, fill= fill, expand= expand, padx=padx, pady= pady, anchor=anchor)
        else:
            label.place(x= x, y= y)
        return label

    def createEntry(self, master, side="top", padx= 0, pady= 0, anchor= "center", width=0, textvar= None, fill="none", expand= False, ipadx=0, ipady= 0, font= "lucida", x= None, y= None):

        entry = tk.Entry(master=master, textvariable=textvar, width=width, font=font, bd=5, relief="sunken")

        if(x is None):
            entry.pack(side=side, padx=padx, pady= pady, anchor=anchor, fill=fill, expand=expand, ipady=ipady, ipadx= ipadx)

        else:
            entry.place(x= x, y= y)


        return entry
    
    def createOptionmenu(self, master, variable, values, x, y):

        optionmenu = tk.OptionMenu(master, variable, *values)
        optionmenu.place(x= x, y= y)

        return optionmenu
    
    def createStringvar(self, master, value= ""):

        stringvar = tk.StringVar(master= master, value=value)

        return stringvar

    def createButton(self, master, text, command, x, y, bg, fg= "black", width=None, height= None):

        btn = tk.Button(master, bg= bg, text=text, command=command, fg= fg, width=width, height=height)
        btn.place(x= x, y= y)

        return btn


    def createListbox(self, master, height, width, x, y, font= "lucida"):

        scroll = tk.Scrollbar(master, orient="vertical")

        lb = tk.Listbox(master=master, height=height, width=width, yscrollcommand=scroll.set, font="lucida 11", selectmode=tk.MULTIPLE)
        scroll.config(command=lb.yview)
        lb.place(x= x, y= y)
        
        return lb
    
    def openFile(self):

        file = askopenfiles(mode="r",
                             filetypes=[
                                        ("Any", "*.*"),
                                        ("Text File", "*.txt"),
                                        ("Python Source File", "*.py"),
                                        ("Cpp Source File", "*.cpp"),
                                        ("Java Source File", "*.java"),
                                        ("PNG File", "*.png"),
                                        ("JPG File", "*.jpg"),
                                        ("Excel Spreadsheet", "*.xlsx")
                                        ])
        
        
        return file
    
    def createTextarea(self, master, height, width, x, y):

        text = tk.Text(master=master, height=height, width=width, font="lucida 11", padx=3, pady=3, relief=tk.SUNKEN, borderwidth=2, exportselection=True)
        text.place(x= x, y= y)

        scroll = tk.Scrollbar(self, orient="vertical")
        scroll.pack()
        text.config(yscrollcommand=scroll.set)
        scroll.config(command=text.yview)

        return text
    
    def createCheckbox(self, master, x, y, text):

        cb = tk.Checkbutton(master, text=text)
        cb.place(x= x, y= y)

        return cb

    def createMenu(self, master, command1):

        mymenu = tk.Menu(master)
        mymenu.add_command(label="Log in", command=command1)

        # master.config(Menu= mymenu)
        self.config(menu=mymenu)

        return mymenu
    
    