from model.scraper import Scraper

class Predictions:

    def __init__(self, scraper: Scraper):
        self.scraper = scraper

    def make_predictions(self):
        """Use Scraper object to make weather predictions.
        The predictions are made by a list of each weather category
        with the first element being the minimum value in the range,
        second element being the maximum, and third element the mean
        
        These three data points are later outputted to the user"""

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

        print(self.pred_dict)



    def make_list(self, lst):
        """Makes three elment data list for each weather category"""
        return_list = []
        return_list.append(min(lst)) #minimum value
        return_list.append(max(lst)) #maximum value
        mean = sum(lst)/len(lst)
        return_list.append(round(mean, 2)) #mean value
        return return_list

