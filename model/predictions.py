from model.scraper import Scraper

class Predictions:
    """This class gets a Scraper object and uses it to make 
    weather calculations which are eventually displayed to user
    """

    def __init__(self, scraper: Scraper):
        """Initialize scraper field"""
        self.scraper = scraper

    def make_predictions(self):
        """Use Scraper object to make weather predictions.
        """

        #dictionary which organizes all weather category
        #calculations, uses lists in Scraper object
        self.pred_dict = {}
        self.pred_dict['temp'] = self.make_list(
            self.scraper.temp)
        self.pred_dict['tempmin'] = self.make_list(
            self.scraper.tempmin)
        self.pred_dict['tempmax'] = self.make_list(
            self.scraper.tempmax)
        self.pred_dict['feelslike'] = self.make_list(
            self.scraper.feelslike)
        self.pred_dict['precipcover'] = self.make_list(
            self.scraper.precipcover)
        self.pred_dict['precipprob'] = self.make_list(
            self.scraper.precipprob)
        self.pred_dict['precip'] = self.make_list(
            self.scraper.precip)
        self.pred_dict['snowdepth'] = self.make_list(
            self.scraper.snowdepth)
        self.pred_dict['windspeed'] = self.make_list(
            self.scraper.windspeed)

    def make_list(self, lst):
        """Makes three element data list for each weather category
            [0]: min value  [1]: max value  [2]: mean value
        
        :param lst: a list"""
        
        return_list = []
        return_list.append(min(lst)) #minimum value
        return_list.append(max(lst)) #maximum value
        mean = sum(lst)/len(lst)
        return_list.append(round(mean, 2)) #mean value
        return return_list

