import tkinter as tk
from tkinter import filedialog
import os
import json #Might use for saving and storing verticies
from PIL import Image, ImageTk
import functools
import time
from concurrent.futures import ProcessPoolExecutor
from tkinter import ttk
#from ..Audio import PlaySound
#from ..Audio.PlayAudio import PlaySound
#sys.path.append?
#import MathEngine #Does not work, problem based on the same as Audio. If audio gets fixed, do the same for Mathengine and do 'as me'


class Application(tk.Frame):
    """ The Application to building Objects. """

    updaterate = 1000 # Will use in update
    CurrentMesh = {} #Don't override this, will use it to store the veritices of an object, such as a cube or a sphere, and later
    #on also save it inside SaveCurrentFile function

    def __init__(self, master = None, width = 1000, height = 800):
        super().__init__(master)
        style = ttk.Style()
        style.configure("BW.TLabel", foreground="black", background="white", font = ('Helvetica', 12))
        self.master = master
        self.width = width
        self.height = height
        self.CurrentDirectory = os.getcwd() # Will use this later on to obtain versitile machine usage.
        self.CurrentFile = None #Will use this later on. Using this variable we can set which "Saves" file were using and thus add verticies if needed
        self.CurrentVertex = None
        self.master.title("Sacra Game Engine")
        self.MeshDirectory = os.path.join(self.CurrentDirectory, 'Saves')
        #self.bind_all('<Button-1>', self.CallBack)
        self.initalize()
        self.Update()



    def initalize(self):
        """Simple initalize function that creates the pulldown menus, and sets some definitions """
        self.master.geometry(f'{self.width}x{self.height}')
        IconPath = os.path.join(self.CurrentDirectory, 'Screen/sacra_kYY_icon.ico')
        self.master.iconbitmap(IconPath)

        menubar = tk.Menu(self.master)

        FileMenu = tk.Menu(menubar)
        EditMenu = tk.Menu(menubar)
        ViewMenu = tk.Menu(menubar)
        FileMenu.add_command(label = "Open", command = self.OpenFile)
        FileMenu.add_command(label = "Save", command = self.SaveFile)
        FileMenu.add_command(label = "Exit", command = self.master.destroy)
        FileMenu.add_command(label = "New", command = self.NewFile)

        menubar.add_cascade(label = "File", menu = FileMenu)
        #Add space and breaker

        EditMenu.add_command(label = "Add vertex", command = self.AddVertexMenu)
        menubar.add_cascade(label = 'Edit', menu = EditMenu) #Add edit commands
        #Add space and breaker

        ViewMenu.add_command(label = "View object")
        ViewMenu.add_command(label = "Inspect object", command = self.ViewObject) #
        menubar.add_cascade(label = "View", menu = ViewMenu) #Add View commands

        self.master.config(menu=menubar)

        self.Canvas = tk.Canvas(master = self.master, bg = 'gray', width = int(self.width / 2), height = self.height)
        self.Canvas.grid(row = 1, column = 5) # Fix the Layout.
        #Look up Columnspan
        size = tk.Scale(master = self.master, from_ = 1, to = 100, orient = "h")
        size.grid(row = 0, column = 1)

        self.StartUpPage() #Fix Fade on this function
        """
        with ProcessPoolExecutor() as executor:
            executor.submit(self.StartUpPage)
            executor.submit(Audio.Playsound().play('Exodus.mp3'))
        """
        self.ActiveFile = ttk.Label(master = self.master, text = self.CurrentFile)
        self.ActiveFile.grid(row = 0, column = 2)



    def StartUpPage(self):
        """A function that runs only ones, on start up. It displays a topframe of which has an image """
        StartUpPageInterface = tk.Toplevel(master = self.master)
        PhotoPath = os.path.join(self.CurrentDirectory, 'Screen/Sacra.png')
        img = ImageTk.PhotoImage(Image.open(PhotoPath))
        label = tk.Label(master = StartUpPageInterface, image = img)
        label.image = img
        label.pack()
        StartUpPageInterface.after(1000, StartUpPageInterface.destroy)
        StartUpPageInterface.attributes('-topmost', True)

    def Update(self): #Implement static and contionus
        """Function to update the File Configuration """
        self.ActiveFile.configure(text = self.CurrentFile)
        #if self.CurrentFile != None:
        #self.master.after(self.updaterate, self.Update)#Works so it continuesly updates


    def OpenFile(self):
        """Opens the filedialog to choose a file. """
        file = filedialog.askopenfilename(initialdir = self.MeshDirectory,
        title = 'Select a file')
        self.CurrentFile = file
        self.Update()

    def NewFile(self):
        """Creates a topframe of which one enters the name of a file.
        Calls the SaveNewFile function to save it. """
        self.NewFileInterface = tk.Toplevel()
        Label = ttk.Label(master = self.NewFileInterface, text = "Enter name of file")
        Label.pack()
        self.Entry = ttk.Entry(master = self.NewFileInterface)
        self.Entry.pack()
        Button = tk.Button(master = self.NewFileInterface, text = "Press to save", command = self.SaveNewFile)
        Button.pack()


    def SaveNewFile(self):
        """Function that checks wether the file already exits or not, and does appropiate depending on the expression. """
        file = self.Entry.get()
        test = file + '.json'
        filename = os.path.join(self.MeshDirectory, file)
        if test not in os.listdir(self.MeshDirectory): #Add so it wont take the name of .json because otherwise it wont work
            with open(file = f'{filename}.json', mode = "w") as activefile: # Change to json file reading & writing
                activefile.write(f'{file}' + ' = {}') # Might change this in the end, might be easier to just make .py and add verticies
            self.CurrentFile = filename + '.json'
            self.NewFileInterface.destroy()
        else:
            Label = ttk.Label(master = self.NewFileInterface, text = 'File already exits')
            Label.pack()
        self.Update()


    def SaveFile(self):
        """ Saves the file """
        self.SavefileInterface = tk.Toplevel()
        Label = ttk.Label(master, self.SavefileInterface, text = "Name object")
        Label.pack()
        self.SaveEntry = ttk.Entry(master = self.SaveFileInterface)
        self.SaveEntry.pack()
        button = tk.Button(master = self.SavefileInterface, command = self.SaveCurrentFile)
        self.Update()


    def SaveCurrentFile(self):
        """Saves the current-file """
        file = self.SaveEntry.get()
        if file not in os.listdir(self.MeshDirectory):
            name = os.path.join(self.MeshDirectory, file)
            with open(file = f'{name}.json', mode = "w") as activefile:
                activefile.write('Test')
            self.SavefileInterface.destroy()
        else:
            label = ttk.Label(master = self.SavefileInterface, text = "Cannot overide keyfiles, being Cube and Sphere")
            label.pack()
        self.Update()

    def AddVertexMenu(self):
        """Small function that is linked with the menu option """
        self.AddVertexInterface = tk.Toplevel()
        Label = ttk.Label(master = self.AddVertexInterface, text = "Number of Verticies")
        Label.pack()
        self.SaveNumberOfVerticies = ttk.Entry(master = self.AddVertexInterface)
        self.SaveNumberOfVerticies.pack()
        button = ttk.Button(master = self.AddVertexInterface, text = "Submit", command = self.GetnumberOfVerticies)
        button.pack()

    def GetnumberOfVerticies(self):
        """Linked to AddVertexMenu function, tells how many verticies one should add """
        NumberOfVerticies = self.SaveNumberOfVerticies.get()
        if NumberOfVerticies != 0: #This does not work, its either a blankspace line or space. Thus we'll use utf8
            self.AddVertex(NumberOfVerticies)
        else:
            self.AddVertex(number = 1)
        self.AddVertexInterface.destroy()

    def AddVertex(self, number = 1):#MenuFunction
        """Linked to GetnumberOfVerticies function, by default one vertex to add """
        print(number) #Used for testing purposes
        pass #Select how mamy verticies that should be added.

    def MoveVertex(self, vector):
        pass #Using selected vertex function we'll be able to move that vertex to the new Position



    def SelectedVertex(self):
        pass #Either label verticies or click, paint the vertex red. so it is selected, and then type cooridates in 3d vector

    def RemoveSelectedVertex(self):
        pass #Remove a Vertex.



    def ScaleMesh(self, scalar):
        pass #Will take the value of Scale widget.

    def Sound(self, NameOfFile):
        pass #Using the import we can play any sound

    def GetMousePosition(self): #Implement, to have SelectVertex function
        x,y = None, None
        return None


    def CallBack(self):
        print(f'Clicked at ({self.event.x}, {self.event.y}')



    def SelectVertex(self): #Will be implemented in GetMousePosition
        pass


    def ViewObject(self): #MenuFunction
        """Linked to the View Menu. """
        self.ViewObjectInterface = tk.Toplevel()
        Button = ttk.Button(master = self.ViewObjectInterface, text = "Exit", command = self.ViewObjectInterface.destroy)
        Button.pack()
        #Will implement view object



root = tk.Tk()
app = Application(root)
app.mainloop()
# file = app.currentfile #Can use this to place
