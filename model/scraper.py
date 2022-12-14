from datetime import datetime
from dateutil.relativedelta import relativedelta
import urllib.request, json

class Scraper:
    """This class will create the lists of weather data
    from the online database"""

    def __init__(self, location, date):
        """Initialize location and date variables to make
        the object, as well as create the category lists"""
        self.location = location
        self.date = date
        self.tempmin = []
        self.tempmax = []
        self.temp = []
        self.feelslike = []
        self.precipcover = []
        self.precipprob = []
        self.precip = []
        self.snowdepth = []
        self.windspeed = []

    def data_search(self):
        """Scrape online database and create lists"""

        #check date formatting
        try:
            self.date = datetime.strptime(self.date, '%m-%d-%Y').date()
        except:
            raise ValueError('Date not correctly formatted.')
        
        today = datetime.now().date()
        two_years = today + relativedelta(years=2)

        #check date is in range (within next two years)
        if self.date < today or self.date > two_years:
            raise ValueError('Date must be within the next two years.')

        #remove whitespace for url
        self.location = self.location.replace(' ','')

        years_ago = 10
        if self.date - relativedelta(years=1) > today:
            #for dates between one and two years in the future
            years_ago += 1

        #scrape past ten years of weather data
        for i in range(10):
            self.url_scrape(years_ago)
            years_ago -= 1

        #print the lists made by url_scrape
        print('\n')
        print(f'Temperature minimum (F): {self.tempmin}')
        print(f'Temperature maximum (F): {self.tempmax}')
        print(f'Temperature mean (F): {self.temp}')
        print(f'Feels like (F): {self.feelslike}')
        print(f'Precipitation Cover (%): {self.precipcover}')
        print(f'Precipitation Probability (%): {self.precipprob}')
        print(f'Precipitation (inches): {self.precip}')
        print(f'Average snow depth on ground (inches): {self.snowdepth}')
        print(f'Windspeed (mph): {self.windspeed}')
        print()


    def url_scrape(self, years_ago):
        """used by data_search to scrape multiple years of 
        weather data and generate required lists
        
        :param years_ago: an integer"""

        date_to_scrape = self.date - relativedelta(years=years_ago)
        date_to_scrape = date_to_scrape.strftime('%Y-%m-%d')

        #API key
        my_key = 'WYTMT69D7EFPWQEDW35UFHCD2'

        #uses "Visual Crossing" weather database
        url = ('https://weather.visualcrossing.com/Visual'
        +'CrossingWebServices/rest/services/timeline/'
        +f'{self.location}/{date_to_scrape}?key={my_key}')

        #database given in JSON format
        result = urllib.request.urlopen(url)
        data = json.loads(result.read())

        #get dictionary from the list in file dictionary
        #which has all essential weather dataa
        day_data = data['days']
        data_dict = day_data[0]

        #making the lists
        self.tempmin.append(data_dict['tempmin'])
        self.tempmax.append(data_dict['tempmax'])
        self.temp.append(data_dict['temp'])
        self.feelslike.append(data_dict['feelslike'])
        self.precipcover.append(data_dict['precipcover'])
        self.precipprob.append(data_dict['precipprob'])
        self.precip.append(data_dict['precip'])
        if data_dict['snowdepth'] == None:
            #snowdepth data is sometimes shown as None
            self.snowdepth.append(0.0)
        else:
            self.snowdepth.append(data_dict['snowdepth'])
        self.windspeed.append(data_dict['windspeed'])