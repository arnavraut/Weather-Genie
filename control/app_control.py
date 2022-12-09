import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import tkinter as tk
from view.home_layout import HomeLayout
from view.load_screen import LoadScreen
from model.scraper import Scraper
from control.data_control import DataController

class AppController:
    def __init__(self, model, view: HomeLayout) -> None:
        self.model = model
        self.view = view
        self.view.enter_button['command'] = lambda:self.enter_pressed()
        self.error_label = tk.Label(self.view.root, text='', 
            font=('Times New Roman',14))


    def run_app(self):
        """This methods runs the app"""
        self.view.root.mainloop()
        
    def enter_pressed(self):
        """Handles when the enter button is pressed"""
        self.location_data = self.view.location_content.get()
        self.date_data = self.view.date_content.get()
        self.load = LoadScreen()
        print('testhere')
        try:
            data_ctr = DataController(self.location_data,
            self.date_data)
            data_ctr.scrape_and_predict()
            #can raise exception in this method if date or location
            #are invalid
        except ValueError as e:
            self.load.root.destroy()
            self.error_label['text'] = 'Error: ' +e.__str__()
            self.error_label.pack()
        except:
            self.load.root.destroy()
            self.error_label['text'] = 'Error: Invalid location'
            self.error_label.pack()

        

control = AppController(None, HomeLayout())
control.run_app()