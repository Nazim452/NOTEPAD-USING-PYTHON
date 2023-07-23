
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename , asksaveasfilename
import os
def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textarea.delete(1.0,END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    if file  == " ":
        file = None
    else:
        root.title(os.path.basename(file) + "-Notepad")
        textarea.delete(1.0,END)
        f= open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()

def savefile():
    global file

    if file == None:
        file = asksaveasfilename(initialfile= "Untitled.txt", defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])

        if file == "":
            file = None
        else:

          f=open(file,"w")
          f.write(textarea.get(1.0,END))
          f.close()

        root.title(os.path.basename(file) + "-Notepad")
    else:
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()

        root.title(os.path.basename(file) + "Notepad")

def quitfile():
    root.destroy()

def cut():
    textarea.event_generate(("<<Cut>>"))

def Copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad - By NAZIM")
if __name__ == '__main__':
    root = Tk()
    root.title("Notepad by Nazim")
    root.geometry("644x788")

    #Add Text area
    textarea = Text(root, font="lucida 13")
    file = None
    textarea.pack(expand = True , fill=BOTH)  #EXPAND-expand karne par pura width le lega ,
                                              #both - X and Y axis

    #menu bar
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)

    #To open a file

    filemenu.add_command( label= "New", command= newfile)
    filemenu.add_command(label="Open" , command = openfile)
    filemenu.add_command(label="Save",command=savefile)

    filemenu.add_separator()

    filemenu.add_command(label = "Exit",command=quitfile)

    menubar.add_cascade(label="File", menu=filemenu)

    #file menu end

    #Edit menu starts

    editmenu = Menu(menubar,tearoff=0)

    editmenu.add_command(label="Cut",command=cut)
    editmenu.add_command(label="Copy", command=Copy)
    editmenu.add_command(label="Paste", command=paste)

    menubar.add_cascade(label="Edit", menu=editmenu)

    #edit menu end


    #Help menu starts

    helpmenu = Menu(menubar, tearoff=0)

    helpmenu.add_command(label="About notepad", command=about)
    menubar.add_cascade(label="Help",menu=helpmenu)






    root.config(menu=menubar)

    #adding scroll bar

    scrollbar = Scrollbar(textarea)
    scrollbar.pack(side=RIGHT , fill=Y)
    scrollbar.config(command=textarea.yview)

    textarea.config(yscrollcommand=scrollbar.set)

















    root.mainloop()