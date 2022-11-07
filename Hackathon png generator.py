import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




s = pd.read_csv(r'C:\Users\schwe\Hackathon/Bunty-20221012.csv', usecols = ['Time', 'Temp', 'Hum', 'Press', 'Alt'])
data2 = pd.read_csv(r'C:\Users\schwe\Hackathon/bunty-20221013.csv', usecols = ['Time', 'Temp', 'Hum', 'Press', 'Alt'])


def plottingTemp(data):
    ax1 = data.plot(x = 'Time' , y = 'Temp', kind = 'scatter')
    plt.savefig('my_plot.png')

def plottingHum(data):
    bx1 = data.plot(x = 'Time' , y = 'Hum', kind = 'scatter')

def plottingPress(data):
    cx1 = data.plot(x = 'Time' , y = 'Press', kind = 'scatter')

def plottingAlt(data):
    dx1 = data.plot(x = 'Time' , y = 'Alt', kind = 'scatter')

#plottingTemp(data1)

ax = s.plot(x = 'Time' , y = 'Temp', kind = 'scatter')
plt.savefig('my_plot4.png')
bx = s.plot(x = 'Time' , y = 'Hum', kind = 'scatter')
plt.savefig('my_plot3.png')
cx = s.plot(x = 'Time' , y = 'Press', kind = 'scatter')
plt.savefig('my_plot2.png')
dx = s.plot(x = 'Time' , y = 'Alt', kind = 'scatter')
plt.savefig('my_plot1.png')
#plottingTemp(data2)

