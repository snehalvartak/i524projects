# Excercise 1

from __future__ import division, print_function
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import pygal as pyg
data = pd.read_csv('2016-first-quarter-citations.csv')
print(data.dtypes)
print(data.columns)
print(data.shape)
data = data.dropna(how='any')
print(data.shape)
data['DateTime Issued'] = data.apply(lambda row : datetime.strptime(row['Date Issued'] +':'+ row['Time Issued'], '%m/%d/%y:%I:%M %p'), axis=1)
data['Day of Week Issued'] = data.apply(lambda row: datetime.strftime(row['DateTime Issued'], '%A'), axis=1)
print(data.head())

days =['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dow_data = [days.index(dow) for dow in data['Day of Week Issued']]
dow_data

#Plot using matplotlib

fig = plt.figure()
ax=fig.add_subplot(1,1,1)
plt.hist(dow_data, bins=len(days))
plt.xticks(range(len(days)),days)
#plt.show()

#Using numpy
ages = data['Cited Person Age'].astype(int)
plt.hist(ages, bins=np.max(ages)- np.min(ages))
#plt.show()

ages = ages[ages < 100]
type(ages)
plt.hist(ages, bins=np.max(ages)- np.min(ages))
plt.savefig('hist.svg')

freq =ages.value_counts()
ages_freq_list = pd.DataFrame({'age':freq.index, 'count':freq.values})
ages_freq_list = ages_freq_list.sort_values(by='age')


#Plot Using Pygal
import pygal as pyg
from pygal.style import Style
custom_style= Style(major_label_font_size = 8,title_font_size=10)

hist_pyg = pyg.Bar(margin_bottom=200,print_labels=True,width=800, height=600,
                      human_readable=True,show_minor_x_labels=False,
                      title='first-quarter citations')
hist_pyg.x_labels = ages_freq_list['age'].unique()
hist_pyg.x_labels_major = ['10','20','30','40','50','60','70','80']

hist_pyg.x_title =('Cited Person Age')
hist_pyg.y_title = ('Frequency')
hist_pyg.add('Frequency',ages_freq_list['count'])
hist_pyg.render_to_file('pygal_chart.svg')
