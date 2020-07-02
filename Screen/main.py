import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image, ImageTk


class Application(tk.Frame):

    def __init__(self, master = None, width = 1000, height = 800):
        super().__init__(master)
        self.master = master
        self.width = width
        self.height = height
        self.currentfile = None #Will use this later on.
        self.master.title("Sacra Game Engine")
        self.initalize()

    def initalize(self):
        self.master.geometry(f'{self.width}x{self.height}')
        img = ImageTk.PhotoImage(Image.open('/Users/andreasevensen/Documents/GitHub/Sacra/Screen/Sacra.png'))
        label = tk.Label(image = img)
        label.image = img
        label.pack()


        menubar = tk.Menu(self.master)

        filemenu = tk.Menu(menubar)
        filemenu.add_command(label = "Open", command = self.openfile)
        filemenu.add_command(label = "Save", )
        filemenu.add_command(label = "Exit", command = self.master.destroy)
        filemenu.add_command(label = "New", command = self.newfile)

        menubar.add_cascade(label="File", menu=filemenu)

        self.master.config(menu=menubar)




    def openfile(self):
        file = filedialog.askopenfilename(initialdir = '/Users/andreasevensen/Documents/GitHub/Sacra/Screen/Saves',
        title = 'Select a file')
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



root = tk.Tk()
app = Application(root)
app.mainloop()
