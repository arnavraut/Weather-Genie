import tkinter as tk
from view.basic_layout import BasicLayout

class ResultsLayout(BasicLayout):
    """ResultsLayout deals with displaying the
    predictions data in Tk frame"""

    def __init__(self, pred_dict):
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

        temp_label = tk.Label(self.root, 
            text=self.text_data(self.pred_dict['temp'],'F',
            'Temperature'))
        tempmin_label = tk.Label(self.root, 
            text=self.text_data(self.pred_dict['tempmin'],'F',
            'Temperature Minimum'))
        tempmax_label = tk.Label(self.root, 
            text=self.text_data(self.pred_dict['tempmax'],'F',
            'Temperature Maximum'))
        feelslike_label = tk.Label(self.root, 
            text=self.text_data(self.pred_dict['feelslike'],'F',
            'Feels Like Temperature'))
        precipcover_label = tk.Label(self.root, 
            text=self.text_data(self.pred_dict['precipcover'],'%',
            'Precipitation Cover'))
        precipprob_label = tk.Label(self.root, 
            text=self.text_data(self.pred_dict['precipprob'],'%',
            'Precipitation Probability'))
        precip_label = tk.Label(self.root, 
            text=self.text_data(self.pred_dict['precip'],'inches',
            'Precipiation Amount'))
        snowdepth_label = tk.Label(self.root, 
            text=self.text_data(self.pred_dict['snowdepth'],
            'inches','Average Snow Depth on Ground'))
        windspeed_label = tk.Label(self.root, 
            text=self.text_data(self.pred_dict['windspeed'],'mph',
            'Windspeed'))
        
        print(self.pred_dict)

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
        return (f'{category} ({unit}):\n'
            +f'Low: {category_list[0]:<10}'
            +f'High: {category_list[1]:<10}'
            +f'Mean: {category_list[2]}')


