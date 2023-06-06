import tkinter as tk
from PIL import Image, ImageTk

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

    def createLabel(self, master, side, fill= "none", expand= False, text= None, image= None, resize= (0,0), padx= 0, pady= 0, anchor= "center", bg= None, width=0, height=0, font="lucida"):

        img = None
        if(image != None):
            img = self.setImage(image, resize)

        label = tk.Label(master= master, bg = bg, text= text, image= img, width=width, height=height, font=font)
        label.pack(side=side, fill= fill, expand= expand, padx=padx, pady= pady, anchor=anchor)

        return label

    def createEntry(self, master, side, padx= 0, pady= 0, anchor= "center", width=0, textvar= None, fill="none", expand= False, ipadx=0, ipady= 0, font= "lucida"):

        entry = tk.Entry(master=master, textvariable=textvar, width=width, font=font)
        entry.pack(side=side, padx=padx, pady= pady, anchor=anchor, fill=fill, expand=expand, ipady=ipady, ipadx= ipadx)

        return entry