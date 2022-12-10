import tkinter as tk
from tkmacosx import Button
from view.basic_layout import BasicLayout

class LoadScreen(BasicLayout):
    """Class to represent the screen after data entry"""

    def __init__(self):
        """Construct LoadScreen, which just adds a label to 
        a BasicLayout
        """

        super().__init__()

        self.location_label = tk.Label(self.root, text='Loading...', 
        font=('Times New Roman',14))
        self.location_label.pack()
