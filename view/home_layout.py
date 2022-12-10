import tkinter as tk
from view.basic_layout import BasicLayout
from tkmacosx import Button

class HomeLayout(BasicLayout):
    """Home layout which user first encounters"""

    def __init__(self):
        """Construct HomeLayout"""
        super().__init__()
        self.construct()
    
    def construct(self):
        """Construct the HomeLayout, called from constructor so 
        constructor can remain simple"""

        #ask for location
        self.location_label = tk.Label(self.root, text='Enter Location', 
        font=('Times New Roman',14))
        self.location_label.pack(pady=10)

        #location entry
        self.location_entry = tk.Entry()
        self.location_entry.pack()

        self.location_content = tk.StringVar()
        self.location_content.set('San Francisco')
        self.location_entry['textvariable'] = self.location_content

        self.spacer_label = tk.Label(self.root, text='')
        self.spacer_label.pack(pady=40)

        #ask for date
        self.date_label = tk.Label(self.root, 
        text='Enter Future Date (up to two years)', 
        font=('Times New Roman',14))
        self.date_label_two = tk.Label(self.root, 
            text='(format: MM-DD-YYYY)',
            font=('Times New Roman',14))
        self.date_label.pack()
        self.date_label_two.pack()

        #date entry
        self.date_entry = tk.Entry()
        self.date_content = tk.StringVar()
        self.date_content.set('')
        self.date_entry['textvariable'] = self.date_content
        self.date_entry.pack(pady=10)

        #enter button
        self.enter_button = Button(
            text= 'Enter Data',
            font=('Times',15),
        )
        self.enter_button['fg'] = 'black'
        self.enter_button.pack()