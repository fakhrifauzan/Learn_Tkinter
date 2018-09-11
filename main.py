from tkinter import *

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter First Window")
        self.minsize(640, 400)
        self.wm_iconbitmap('icon.ico')
        self.configure(background = '#4D4D4D')
        self.create_widget()
    
    def create_widget(self):
        label = Label(self, text = "Selamat Datang")
        label2 = Label(self, text = "Di Program Phyton Pertama")
        
        # Positioning Using GRID
        #label.grid(column = 0, row = 0)      
        #label2.grid(column = 0, row = 1)
        
        #Positioning Using Geometry
        label.place(x = 20, y = 50)
        label2.place(x = 20, y = 100)
                       
root = Root()
root.mainloop()