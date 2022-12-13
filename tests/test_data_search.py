import unittest
from model.scraper import Scraper

class testDataSearch(unittest.TestCase):
    """Tests data_search in Scraper"""
    def test_past_date(self):
        location = 'Boston'
        date = '02-23-2021' #past date
        scrp = Scraper(location, date)
        with self.assertRaises(ValueError):
            scrp.data_search()

    def test_invalid_date(self):
        location = 'Boston'
        date = '02-31-2023' #date doesn't exist
        scrp = Scraper(location, date)
        with self.assertRaises(ValueError):
            scrp.data_search()

    def test_sample(self):
        location = 'Boston'
        date = '02-14-2023'
        scrp = Scraper(location, date)
        scrp.data_search()
        self.assertEqual(len(scrp.temp),10)
        self.assertEqual(len(scrp.tempmax),10)
        #see sample lists are made to correct length

        self.assertEqual(scrp.temp[5],38.0)
        #test 02-14-2018 temperature

