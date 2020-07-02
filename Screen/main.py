import tkinter as tk
from tkinter import filedialog
import os
import json #Might use for saving and storing verticies
from PIL import Image, ImageTk




class Application(tk.Frame):

    updaterate = 1000 # Will use in update
    CurrentMesh = {} #Don't override this, will use it to store the veritices of an object, such as a cube or a sphere, and later
    #on also save it inside SaveCurrentFile function

    def __init__(self, master = None, width = 1000, height = 800):
        super().__init__(master)
        self.master = master
        self.width = width
        self.height = height
        self.currentfile = None #Will use this later on. Using this variable we can set which "Saves" file were using and thus add verticies if needed
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
        filemenu.add_command(label = "Save", command = self.SaveFile)
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
        self.NewFileInterface = tk.Toplevel()
        Label = tk.Label(master = self.NewFileInterface, text = "Enter name of file")
        Label.pack()
        self.Entry = tk.Entry(master = self.NewFileInterface)
        self.Entry.pack()
        Button = tk.Button(master = self.NewFileInterface, text = "Press to save", command = self.SaveNewFile)
        Button.pack()


    def SaveNewFile(self):
        file = self.Entry.get()
        if file not in os.listdir('/Users/andreasevensen/Documents/GitHub/Sacra/Screen/Saves'): #Add so it wont take the name of .json because otherwise it wont work
            filename = os.path.join('/Users/andreasevensen/Documents/GitHub/Sacra/Screen/Saves', file)
            with open(file = f'{filename}.json', mode = "w") as activefile: # Change to json file reading & writing
                activefile.write(f'{file}' + ' = {}') # Might change this in the end, might be easier to just make .py and add verticies
            self.currentfile = file
            self.NewFileInterface.destroy()
        else:
            Label = tk.Label(master = self.NewFileApp, text = 'File already exits')
            Label.pack()

    def Update(self):

        print("Hello")
        self.master.after(self.updaterate, self.Update)#Works so it continuesly updates


    def SaveFile(self):
        self.SavefileInterface = tk.Toplevel()
        Label = tk.Label(master, self.SavefileInterface, text = "Name object")
        Label.pack()
        self.SaveEntry = tk.Entry(master = self.SaveFileInterface)
        self.SaveEntry.pack()
        button = tk.Button(master = self.SavefileInterface, command = self.SaveCurrentFile)


    def SaveCurrentFile(self):
        name = self.SaveEntry.get()
        if file not in os.listdir('/Users/andreasevensen/Documents/GitHub/Sacra/Screen/Saves'):
            with open(file = f'{name}.json', mode = "w") as activefile:
                activefile.write('Test')
            self.SavefileInterface.destroy()
        else:
            label = tk.Label(master = self.SavefileInterface, text = "Cannot overide keyfiles")
            label.pack()


    def SelectedVertex(self):
        pass #Either label verticies or click, paint the vertex red. so it is selected, and then type cooridates in 3d vector

    def ScaleMesh(self, scalar):
        pass #Will take the value of Scale widget.

    def MoveVertex(self, vector):
        pass #Using selected vertex function we'll be able to move that vertex to the new Position

    def AddVertex(self, number = 1):
        pass #Select how mamy verticies that should be added.



#print(dir(tk))
root = tk.Tk()
app = Application(root)
app.mainloop()
# file = app.currentfile #Can use this to place
