import tkinter as tk
from tkmacosx import Button
from view.home_layout import HomeLayout
from view.load_screen import LoadScreen
from model.scraper import Scraper

class DataController:
    """Manages data between model classes"""

    def __init__(self, location, date):
        self.location = location
        self.date = date
    
    def scrape_and_predict(self):
        self.scr = Scraper(self.location, self.date)
        self.scr.data_search()

