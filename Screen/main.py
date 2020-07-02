import tkinter as tk

class Mainwindow(tk.Frame):

    def __init__(self, master = None, Title = None, Width = None, Height = None):
        super().__init__(master)
        self.Width = Width
        self.Height = Height
        self.master = master
        self.Title = Title
        self.master.title(self.Title)
        self.master.geometry(f'{self.Width}x{self.Height}')
        self.initalize()

    def initalize(self):
        self.Canvas = tk.Canvas(height = self.Height/2, width = self.Width, bg = 'Blue')
        self.Canvas.place(x = 0, y = self.Height/2)
        self.button1 = tk.Button(text = "Press to update", command = self.get)
        self.button1.pack()
        self.slider1 = tk.Scale(from_=0, to = 100, orient = 'horizontal')
        self.slider1.pack()

        Name = Loadingscreen()

    def get(self):
        print(self.slider1.get())


    def quit(self):
        self.root.destroy()




root = tk.Tk()
app = Mainwindow(root, Title = "Fuck", Width = 1000, Height = 500)
app.mainloop()
