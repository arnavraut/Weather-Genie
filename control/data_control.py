from model.scraper import Scraper
from model.predictions import Predictions

class DataController:
    """Manages data between model classes
        Scraper and Predictions"""

    def __init__(self, location, date):
        """Initialize location and date variables"""
        self.location = location
        self.date = date
    
    def scrape_and_predict(self):
        """Create a Scraper object, use it to get data, and 
            pass the object on to a Predictions object so predictions 
            can be created
        
        :return: the predictions dictionary from Predictions object
            so that the AppController can use it to display results"""
        self.scr = Scraper(self.location, self.date)
        self.scr.data_search()
        self.predict = Predictions(self.scr)
        self.predict.make_predictions()
        return self.predict.pred_dict

