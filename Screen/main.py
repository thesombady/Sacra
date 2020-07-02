import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image, ImageTk
import time
from concurrent.futures import ThreadPoolExecutor


class Application(tk.Frame):

    updaterate = 1000 # Will use in update

    def __init__(self, master = None, width = 1000, height = 800):
        super().__init__(master)
        self.master = master
        self.width = width
        self.height = height
        self.currentfile = None #Will use this later on.
        self.master.title("Sacra Game Engine")
        self.initalize()
        self.Update()



    def initalize(self):
        self.master.geometry(f'{self.width}x{self.height}')
        img = ImageTk.PhotoImage(Image.open('/Users/andreasevensen/Documents/GitHub/Sacra/Screen/Sacra.png'))
        label = tk.Label(image = img)
        label.image = img
        label.grid(row = 1)


        menubar = tk.Menu(self.master)

        filemenu = tk.Menu(menubar)
        editmenu = tk.Menu(menubar)
        viewmenu = tk.Menu(menubar)
        filemenu.add_command(label = "Open", command = self.openfile)
        filemenu.add_command(label = "Save", )
        filemenu.add_command(label = "Exit", command = self.master.destroy)
        filemenu.add_command(label = "New", command = self.newfile)

        menubar.add_cascade(label = "File", menu = filemenu)
        #Add space and breaker

        editmenu.add_command(label = "Add vertex")
        menubar.add_cascade(label = 'Edit', menu = editmenu) #Add edit commands
        #Add space and breaker

        viewmenu.add_command(label = "View object")
        viewmenu.add_command(label = "Inspect object")
        menubar.add_cascade(label = "View", menu = viewmenu) #Add View commands

        self.master.config(menu=menubar)



        #self.Canvas1 = tk.Canvas(master = self.master, width = int(self.width / 2), height = int(2 * self.height / 3), bg = 'black')
        #self.Canvas1.pack(side = 'right')

        self.Canvas = tk.Canvas(master = self.master, bg = 'gray', width = int(self.width / 2), height = self.height)
        self.Canvas.grid(row = 1, column = 2)
        #Look up Columnspan
        size = tk.Scale(master = self.master, from_ = 1, to = 100, orient = "h")
        size.grid(row = 0, column = 1)


    def openfile(self):
        file = filedialog.askopenfilename(initialdir = '/Users/andreasevensen/Documents/GitHub/Sacra/Screen/Saves',
        title = 'Select a file') # Change Position
        self.currentfile = file

    def newfile(self):
        self.NewFileApp = tk.Toplevel()
        Label = tk.Label(master = self.NewFileApp, text = "Enter name of file")
        Label.pack()
        self.Entry = tk.Entry(master = self.NewFileApp)
        self.Entry.pack()
        Button = tk.Button(master = self.NewFileApp, text = "Press to save", command = self.SaveNewFile)
        Button.pack()


    def SaveNewFile(self):
        file = self.Entry.get()
        if file not in os.listdir('/Users/andreasevensen/Documents/GitHub/Sacra/Screen/Saves'):
            filename = os.path.join('/Users/andreasevensen/Documents/GitHub/Sacra/Screen/Saves', file)
            with open(file = f'{filename}', mode = "w", ) as activefile:
                activefile.write(f'{file}')
            self.currentfile = file
            self.NewFileApp.destroy()
        else:
            Label = tk.Label(master = self.NewFileApp, text = 'File already exits')
            Label.pack()

    def Update(self):

        print("Hello")
        self.master.after(self.updaterate, self.Update)#Works so it continuesly updates



#print(dir(tk))
root = tk.Tk()
app = Application(root)
app.mainloop()
# file = app.currentfile #Can use this to place
