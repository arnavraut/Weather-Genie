import tkinter as tk
import threading
from view.home_layout import HomeLayout
from view.load_screen import LoadScreen
from view.results_layout import ResultsLayout
from control.data_control import DataController

class AppController:
    """The main controller class, connects model and 
    view classes
    """

    def __init__(self, view: HomeLayout) -> None:
        """Initialize view field,
        set enter button's command to local method,
        initialize error label
        """
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

        #thread allows load screen to be created without
        #having to wait for entire scraping method
        threading.Thread(target=self.data_control_help).start()
        self.exception_thrown = False
        self.load.root.mainloop()

        #display results after giving time for scraping + predictions
        if not self.exception_thrown:
            self.view.root.after(2000,self.display_results())


    def data_control_help(self):
        """This method uses DataController to scrape and predict
        weather data
        """

        try:
            data_ctr = DataController(self.location_data,
            self.date_data)
            self.pred_dict = data_ctr.scrape_and_predict()
            #can raise exception in this method if date or location
            #are invalid

            #destroy these frames to make way for ResultsLayout
            self.view.root.destroy()
            self.load.root.destroy()

        #display appropriate error message to user
        except ValueError as e:
            self.exception_thrown = True
            self.load.root.destroy()
            self.error_label['text'] = 'Error: ' +e.__str__()
            self.error_label.pack()
        except:
            self.exception_thrown = True
            self.load.root.destroy()
            self.error_label['text'] = 'Error: Invalid location'
            self.error_label.pack()

    def display_results(self):
        """Uses prediction dictionary from DataController object
        and pass it to ResultsLayout object to display results"""
        ResultsLayout(self.pred_dict)