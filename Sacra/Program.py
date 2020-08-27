import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os
import json #Might use for saving and storing verticies
from PIL import Image, ImageTk
import functools #Might not use func tools
import time
from concurrent.futures import ProcessPoolExecutor
import Renderer #Renderer is not yet done
import SacraMathEngine as me
#import Audio #Fix audio import
import Audio



"""
Look over the saving functions. Have 3 saving functions. Might be abit overkill.

"""

Audio.PlayAudio.PlaySound().Play('Exodus.mp3')#'wht?'


class LoadError(Exception):
    pass


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
        self.CurrentDirectory = os.getcwd() # Will use this later on to obtain versatile machine usage.
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
        IconPath = os.path.join(self.CurrentDirectory, 'Sacra/sacra_kYY_icon.ico')
        self.master.iconbitmap(IconPath)

        menubar = tk.Menu(self.master)

        FileMenu = tk.Menu(menubar)
        EditMenu = tk.Menu(menubar)
        ViewMenu = tk.Menu(menubar)
        BuildMenu = tk.Menu(menubar)
        show_all = tk.BooleanVar()

        BuildMenu.add_checkbutton(label = "Make Client-server", onvalue = 1, offvalue = 0, variable = show_all)
        BuildMenu.add_command(label = "Build Game", command = self.BuildGame)
        menubar.add_cascade(label = "Build", menu = BuildMenu)

        FileMenu.add_command(label = "Open", command = self.OpenFile)
        FileMenu.add_command(label = "Save", command = self.SaveFile)
        FileMenu.add_command(label = "Exit", command = self.master.destroy)
        FileMenu.add_command(label = "New", command = self.NewFile)

        menubar.add_cascade(label = "File", menu = FileMenu)
        #Add space and breaker

        EditMenu.add_command(label = "Add vertex", command = self.AddVertexMenu)
        EditMenu.add_command(label = "Edit Map")

        self.SecondObject = None
        EditMenu.add_cascade(label = "Merge Objects", command = self.MergeObjects)
        menubar.add_cascade(label = 'Edit', menu = EditMenu) #Add edit commands
        #Add space and breaker

        ViewMenu.add_command(label = "View object")
        ViewMenu.add_command(label = "Inspect object", command = self.ViewObject) #
        menubar.add_cascade(label = "View", menu = ViewMenu) #Add View commands

        self.master.config(menu=menubar)


        #Will probably remove this and make an entire function for this.
        size = ttk.Scale(master = self.master, from_ = 1, to = 100, orient = "h")
        size.place(x = 10, y = 30)

        self.StartUpPage() #Fix Fade on this function
        """
        with ProcessPoolExecutor() as executor:
            executor.submit(self.StartUpPage)
            executor.submit(Audio.Playsound().play('Exodus.mp3'))
        """
        self.ActiveFile = ttk.Label(master = self.master, text = self.CurrentFile)
        self.ActiveFile.place(x = 10, y = 10)
        self.Viewer()

    def Viewer(self):
        self.FilePrewievCanvas = tk.Canvas(master = self.master, bg = 'gray', height = 1000, width = 500)
        #self.FilePrewievCanvas.grid(row = 0, column = 2)
        self.FilePrewievCanvas.place(x = 500, y = -10)
        """
        Add Renderer function.
        """



    def StartUpPage(self):
        """A function that runs only ones, on start up. It displays a topframe of which has an image """
        StartUpPageInterface = tk.Toplevel(master = self.master)
        PhotoPath = os.path.join(self.CurrentDirectory, 'Sacra/SacraGame.png')
        img = ImageTk.PhotoImage(Image.open(PhotoPath))
        label = ttk.Label(master = StartUpPageInterface, image = img)
        label.image = img
        label.pack()
        StartUpPageInterface.after(2000, StartUpPageInterface.destroy)
        StartUpPageInterface.attributes('-topmost', True)

    def Update(self): #Implement static and continuous
        """Function to update the File Configuration """
        self.ActiveFile.configure(text = self.CurrentFile)
        #if self.CurrentFile != None:
        #self.master.after(self.updaterate, self.Update)#Works so it continuously updates


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
        Button = ttk.Button(master = self.NewFileInterface, text = "Press to save", command = self.SaveNewFile)
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

    def MergeObjects(self):
        self.SecondObject = self.CurrentFile
        self.OpenFile()
        if self.SecondObject == self.CurrentFile:
            messagebox.showerror("Cannot Merge same objects", "Choose another file.")
        self.Update()




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

    def PreviedWindow(self, file):
        if isinstance(file, None):
            pass
        else:
            try:
                filename = self.CurrentFile.split('/')
                Data = MeshObject()
                Data(filename[-1])
            except:
                raise LoadError("[System]: Can't load current file.")


    def BuildGame(self):
        pass

class PreviewImage(tk.Canvas):
    """Small Class that will control the previewImage"""


    def __init__(self, master = None, **args):
        super().__init__(master)
        InitialValues = "{Height = 1000, Width = 1000, Position = (500,500)}"
        if not kwargs in InitialValues:
            raise TypeError("[System]: One or more of the inputs are not valid.")


root = tk.Tk()
app = Application(root)
app.mainloop()
# file = app.currentfile #Can use this to place
