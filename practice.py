import tkinter as t

root = t.Tk()

root.geometry("700x500")

lb = t.Listbox(root, height=3, highlightcolor="red")
lb.pack()

lb.insert("end", "hello1")
lb.insert("end", "hello2")
lb.insert("end", "hello3")

print(lb.get(0, "end"))

var2 = t.StringVar(root)
var2.set("hello")

t.Entry(root, textvariable=var2).pack()

def printit():
    print(var2.get())

t.Button(text="press", command=printit).pack()


root.mainloop()