import tkinter as tk

class BasicLayout():
    """Represents the basic app layout"""
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x600')
        self.root.title('Weather Genie')

        self.title = tk.Label(self.root, text='Weather Genie', 
        font=('Times New Roman',24))
        self.title.pack(padx=10, pady=20)

        


