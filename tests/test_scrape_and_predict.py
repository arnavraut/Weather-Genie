import unittest
from control.data_control import DataController

class TestScrapeAndPredict(unittest.TestCase):
    """Tests scrape_and_predict in DataController"""

    def test_invalid_date(self):
        date = '03-43-2023'
        location = 'San Francisco'
        datactr = DataController(location,date)
        with self.assertRaises(ValueError):
            datactr.scrape_and_predict()

    def test_sample(self):
        date = '03-13-2023'
        location = 'San Francisco'
        datactr = DataController(location,date)
        dictonary = datactr.scrape_and_predict()
        self.assertEquals(len(dictonary['temp']),3)
        #test the returned dictionary has correct length

        self.assertEquals(dictonary['tempmax'][1],73.9)
        #test maximum temperature found, double checked online

        self.assertEquals(dictonary['tempmin'][0],44.6)
         #test minimum temperature found, double checked online
         #remember index 0 is low and index 1 is high
