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
import functools
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
        self.CurrentMesh = None
        self.master.title("Sacra Game Engine")
        self.MeshDirectory = os.path.join(self.CurrentDirectory, 'Saves')
        #self.bind_all('<Button-1>', self.CallBack)
        self.initalize()


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

        EditMenu.add_command(label = "Add vertex")
        EditMenu.add_command(label = "Edit Map")
        EditMenu.add_command(label = "Move Object", command = self.MoveObject)

        self.SecondObject = None
        EditMenu.add_cascade(label = "Merge Objects", command = self.MergeObjects)
        menubar.add_cascade(label = 'Edit', menu = EditMenu) #Add edit commands
        #Add space and breaker

        ViewMenu.add_command(label = "View object")
        ViewMenu.add_command(label = "Inspect object", command = self.InspectObject) #
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

    def Viewer(self):
        Directory = os.getcwd()
        FrameFile = os.path.join(Directory, 'Sacra/Renderer/CurrentFrame/Frame2.png')
        img = ImageTk.PhotoImage(Image.open(FrameFile))
        label = tk.Label(master = self.master, image = img)
        label.image = img
        label.place(x = 500, y = -10)

    def RenderFunction(self):
        try:
            Mesh = self.CurrentMesh
            RenderMesh = Renderer2(Mesh)._Draw(EVector = me.vec3d(100,100,100), Orientation=me.vec3d(0,0,0))
        except Exception as E:
            print(E)


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
        try:
            #self.ActiveObject._saver(self.CurrentFile)
            pass
        except:
            print("Saving issue")
        self.RenderFunction()
        self.ShowInfo()
        self.Viewer()


    def ShowInfo(self):
        ListBoxOfMesh = tk.Listbox(master = self.master, width = 30)
        try:
            Mesh = self.CurrentMesh
            for i in range(len(Mesh)):
                ListBoxOfMesh.insert(i, Mesh[i])
        except:
            pass
        def Remove():
            Value
            ListBoxOfMesh.delete(ANCHOR)
            self.ShowInfo()
        ListBoxOfMesh.place(x = 20,y = 100)
        RemoveButton = tk.Button(master = self.master, text = "Remove", command = Remove)
        RemoveButton.place(x = 20, y = 300)


    def OpenFile(self):
        """Opens the filedialog to choose a file. """
        file = filedialog.askopenfilename(initialdir = self.MeshDirectory,
        title = 'Select a file')
        Filename = file.split('/')
        Filename = Filename[-1]
        Filename = Filename.split('.')
        Filename = Filename[0] #To retrieve the correct filename without any exentisons.
        self.CurrentFile = Filename
        self.ActiveObject = me.MeshObject3d()
        self.CurrentMesh = self.ActiveObject._setter(self.CurrentFile)
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
        def MoveRight():
            try:
                self.ActiveObject = self.ActiveObject + me.vec3d(1,0,0)
                self.Update()
            except:
                pass
        def MoveLeft():
            try:
                self.ActiveObject = self.ActiveObject + me.vec3d(-1,0,0)
                self.Update()
            except:
                pass
        def MoveDown():
            try:
                self.ActiveObject = self.ActiveObject + me.vec3d(0,1,0)
                self.Update()
            except:
                pass
        def MoveUp():
            try:
                self.ActiveObject = self.ActiveObject + me.vec3d(0,-1,0)
                self.Update()
            except:
                pass
        MoveButton = tk.Toplevel()
        MoveRightV = tk.Button(master = MoveButton, text = "Move Right", command = MoveRight)
        MoveRightV.pack()
        MoveLeftV = tk.Button(master = MoveButton, text = "Move Left", command = MoveLeft)
        MoveLeftV.pack()
        MoveUpV = tk.Button(master = MoveButton, text = "Move up", command = MoveUp)
        MoveUpV.pack()
        MoveDownV = tk.Button(master = MoveButton, text = "Move down", command = MoveDown)
        MoveDownV.pack()

    def Sound(self, NameOfFile):
        pass #Using the import we can play any sound

    def GetMousePosition(self): #Implement, to have SelectVertex function
        x,y = None, None
        return None

    def CallBack(self):
        print(f'Clicked at ({self.event.x}, {self.event.y}')

    def SelectVertex(self): #Will be implemented in GetMousePosition
        pass


    def InspectObject(self): #MenuFunction
        """Linked to the View Menu. """
        InspectObjectInterface = tk.Toplevel()
        Button = ttk.Button(master = InspectObjectInterface, text = "Exit", command = InspectObjectInterface.destroy)
        Button.pack()
        Mesh = me.MeshObject3d()._setter(self.CurrentFile)
        MeshRenderer = Renderer2(Mesh)
        Directory = os.getcwd()
        Spinx = ttk.Button(master = InspectObjectInterface, text = "Spin in x direction")
        Spinx.pack()
        Spiny = ttk.Button(master = InspectObjectInterface, text = "Spin in y direction")
        Spiny.pack()
        Spinz = ttk.Button(master = InspectObjectInterface, text = "Spin in z direction")
        Spinz.pack()
        FrameFile = os.path.join(Directory, 'Sacra/Renderer/CurrentFrame/Frame2.png')
        load = Image.open(FrameFile)
        render = ImageTk.PhotoImage(load)
        image = tk.Label(master = InspectObjectInterface, image = render)
        image.image = render
        image.pack()

    def PreviedWindow(self, file):
        if isinstance(file, None):
            pass
        else:
            try:
                filename = self.CurrentFile.split('/')
                Data = MeshObject3d()
                Data(filename[-1])
            except:
                raise LoadError("[System]: Can't load current file.")


    def BuildGame(self):
        pass



root = tk.Tk()
app = Application(root)
app.mainloop()
# file = app.currentfile #Can use this to place
