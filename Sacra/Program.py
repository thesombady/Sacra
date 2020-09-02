import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os
import json #Might use for saving and storing verticies
from PIL import Image, ImageTk
import functools #Might not use func tools
import time
from concurrent.futures import ProcessPoolExecutor
from Renderer import * #Renderer is not yet done
import SacraMathEngine as me
import SacraPhysicsEngine as pe
#import Audio #Fix audio import
import Audio
#Add curser controle, and be ability of tabbing through triangles/verticies



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
        EditMenu.add_command(label = "Move Object", command = self.MoveObject)

        self.SecondObject = None
        EditMenu.add_cascade(label = "Merge Objects", command = self.MergeObjects)
        menubar.add_cascade(label = 'Edit', menu = EditMenu) #Add edit commands
        #Add space and breaker

        ViewMenu.add_command(label = "View object")
        ViewMenu.add_command(label = "Inspect object", command = self.ViewObject) #
        menubar.add_cascade(label = "View", menu = ViewMenu) #Add View commands

        self.master.config(menu=menubar)


        #Will probably remove this and make an entire function for this.
        self.ScaleMeshValue = ttk.Scale(master = self.master, from_ = 1, to = 100, orient = "h")
        self.ScaleMeshValue.place(x = 10, y = 30)

        self.StartUpPage() #Fix Fade on this function
        """
        with ProcessPoolExecutor() as executor:
            executor.submit(self.StartUpPage)
            executor.submit(Audio.Playsound().play('Exodus.mp3'))
        """
        self.ActiveFile = ttk.Label(master = self.master, text = self.CurrentFile)
        self.ActiveFile.place(x = 10, y = 10)
        self.ViewerCanvas()

    def ViewerCanvas(self):
        self.FilePrewievCanvas = tk.Canvas(master = self.master, bg = 'gray', height = 1000, width = 500)
        #self.FilePrewievCanvas.grid(row = 0, column = 2)
        self.FilePrewievCanvas.place(x = 500, y = -10)
        """
        Add Renderer function.
        """

    def Viewer(self):
        Directory = os.getcwd()
        FrameFile = os.path.join(Directory, 'Sacra/Renderer/CurrentFrame/Frame.png')
        img = ImageTk.PhotoImage(Image.open(FrameFile))
        label = tk.Label(master = self.master, image = img)
        label.image = img
        label.place(x = 500, y = -10)


    def StartUpPage(self):
        """A function that runs only ones, on start up. It displays a topframe of which has an image """
        StartUpPageInterface = tk.Toplevel(master = self.master)
        PhotoPath = os.path.join(self.CurrentDirectory, 'Sacra/SacraGame.png')
        img = ImageTk.PhotoImage(Image.open(PhotoPath))
        label = tk.Label(master = StartUpPageInterface, image = img)
        label.image = img
        label.pack()
        StartUpPageInterface.after(2000, StartUpPageInterface.destroy)
        StartUpPageInterface.attributes('-topmost', True)

    def Update(self): #Implement static and continuous
        """Function to update the File Configuration """
        self.ActiveFile.configure(text = self.CurrentFile)
        CurrentFile = self.CurrentFile
        self.Mesh = None

        if CurrentFile != None:
            try:
                CurrentMeshFile = CurrentFile.split('/')
                Filename = CurrentMeshFile[-1]
                Filename = Filename.split('.')
                Filename = Filename[0] #To retrieve the correct filename without any exentisons.
                self.Mesh = me.MeshObject()
                self.Mesh.setter(Filename)
                RenderObject = Renderer(self.Mesh)
                RenderObject.DrawObject()
            except Exception as E:
                raise E
        self.Viewer()
        self.master.after(500, self.Update)#Works fine


    def OpenFile(self):
        """Opens the filedialog to choose a file. """
        file = filedialog.askopenfilename(initialdir = self.MeshDirectory,
        title = 'Select a file')
        self.CurrentFile = file
        self.Update()
        #print(type(self.CurrentFile))

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
        Label = ttk.Label(master = self.SavefileInterface, text = "Name object")
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

    def MoveObject(self):
        try:
            def MoveUp():
                self.Mesh = self.Mesh + me.vec3d(0,1,0)
                self.Update()
            def MoveDown():
                self.Mesh = self.Mesh + me.vec3d(0,-1,0)
                self.Update()
            def MoveRight():
                self.Mesh = self.Mesh + me.vec3d(1,0,0)
                self.Update()
            def MoveLeft():
                self.Mesh = self.Mesh + me.vec3d(-1,0,0)
                self.Update()
        except Exception as E:
            raise E
        MoveButton = tk.Toplevel()
        MoveRightV = tk.Button(master = MoveButton, text = "Move Right", command = MoveRight)
        MoveRightV.pack()
        MoveLeftV = tk.Button(master = MoveButton, text = "Move Left", command = MoveLeft)
        MoveLeftV.pack()
        MoveUpV = tk.Button(master = MoveButton, text = "Move up", command = MoveUp)
        MoveUpV.pack()
        MoveDownV = tk.Button(master = MoveButton, text = "Move down", command = MoveDown)
        MoveDownV.pack()





    def ScaleMesh(self):
        if self.Mesh != None:
            ScalarValue = self.ScaleMeshValue.get()
            try:
                self.Mesh = self.Mesh * ScalarValue
            except Exception as E:
                raise E
        #pass #Will take the value of Scale widget.

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



root = tk.Tk()
app = Application(root)
app.mainloop()
# file = app.currentfile #Can use this to place
