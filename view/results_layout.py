import tkinter as tk
from view.basic_layout import BasicLayout

class ResultsLayout(BasicLayout):
    """ResultsLayout deals with displaying the
    predictions data in Tk frame"""

    def __init__(self, pred_dict):
        """Construct ResultsLayout and initialize dictionary
        
        :param pred_dict: a dictionary"""

        super().__init__()
        self.pred_dict = pred_dict
        self.construct()

    def construct(self):
        """Construct the ResultsLayout, called from constructor so 
        constructor can remain simple"""

        results_text = ('Results from past ten years\n'
            +'for given date and location:')
        results_label = tk.Label(self.root, text=results_text, 
        font=('Times New Roman',16))
        results_label.pack(pady=10)

        #make Label for each weather category
        temp_label = tk.Label(self.root, 
            text=self.text_data(self.pred_dict['temp'],'F',
            'Temperature'),font=('Times',12))
        tempmin_label = tk.Label(self.root, 
            text=self.text_data(self.pred_dict['tempmin'],'F',
            'Temperature Minimum'),font=('Times',12))
        tempmax_label = tk.Label(self.root, 
            text=self.text_data(self.pred_dict['tempmax'],'F',
            'Temperature Maximum'),font=('Times',12))
        feelslike_label = tk.Label(self.root, 
            text=self.text_data(self.pred_dict['feelslike'],'F',
            'Feels Like Temperature'),font=('Times',12))
        precipcover_label = tk.Label(self.root, 
            text=self.text_data(self.pred_dict['precipcover'],'%',
            'Precipitation Cover'),font=('Times',12))
        precipprob_label = tk.Label(self.root, 
            text=self.text_data(self.pred_dict['precipprob'],'%',
            'Precipitation Probability'),font=('Times',12))
        precip_label = tk.Label(self.root, 
            text=self.text_data(self.pred_dict['precip'],'inches',
            'Precipiation Amount'),font=('Times',12))
        snowdepth_label = tk.Label(self.root, 
            text=self.text_data(self.pred_dict['snowdepth'],
            'inches','Average Snow Depth on Ground'),
            font=('Times',12))
        windspeed_label = tk.Label(self.root, 
            text=self.text_data(self.pred_dict['windspeed'],'mph',
            'Windspeed'),font=('Times',12))

        #add Labels to frame
        temp_label.pack(pady=5)
        tempmin_label.pack(pady=5)
        tempmax_label.pack(pady=5)
        feelslike_label.pack(pady=5)
        precipcover_label.pack(pady=5)
        precipprob_label.pack(pady=5)
        precip_label.pack(pady=5)
        snowdepth_label.pack(pady=5)
        windspeed_label.pack(pady=5)
        self.root.mainloop()

    
    def text_data(self,category_list,unit,category):
        """Returns the appropriate label text for the given
            weather category
        
        :param category_list: a list
        :param unit: a string
        :param category: a string"""

        return (f'{category} ({unit}):\n'
            +f'Low: {category_list[0]:<10}'
            +f'High: {category_list[1]:<10}'
            +f'Mean: {category_list[2]}')


