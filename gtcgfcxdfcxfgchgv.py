import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bio1 = pd.read_csv(r'C:\Users\schwe\Hackathon\Bunty-20221012.csv')
bio1

##plt.scatter(price, sales_per_day)
##plt.show()

s = pd.read_csv(r"C:\Users\schwe\Hackathon\Bunty-20221012.csv", usecols = ['Press','Hum'])
##df = pd.read_csv("student_scores2.csv", usecols = ['IQ','Scores'])

ax = s.plot(x = 'Hum' , y = 'Press', kind = 'scatter')
