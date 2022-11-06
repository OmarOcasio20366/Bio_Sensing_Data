##import pandas as pd
##import numpy as np
##import matplotlib.pyplot as plt
##
##bio1 = pd.read_csv(r'C:\Users\schwe\Hackathon\Bunty-20221012.csv')
##bio1
##
####plt.scatter(price, sales_per_day)
####plt.show()
##
##s = pd.read_csv(r"C:\Users\schwe\Hackathon\Bunty-20221012.csv", usecols = ['Time','Temp','Hum','Press','Alt'])
####df = pd.read_csv("student_scores2.csv", usecols = ['IQ','Scores'])
####'Time','Temp','Hum','Press','Alt'
##
##
####print("Use the following to choose your y axis.")
####print("1 for Temperature, 2 for Humidity, 3 for Pressure, or 4 for Altitude")
##
##yAxe = "Hum"
##
##ax = s.plot(x = 'Time' , y = yAxe, kind = 'scatter')
##

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bio1 = pd.read_csv(r'C:\Users\schwe\Hackathon\Bunty-20221012.csv')
bio1

##plt.scatter(price, sales_per_day)
##plt.show()

s = pd.read_csv(r"C:\Users\schwe\Hackathon\Bunty-20221012.csv", usecols = ['Time','Temp','Hum','Press','Alt'])
##df = pd.read_csv("student_scores2.csv", usecols = ['IQ','Scores'])

ax = s.plot(x = 'Time' , y = 'Temp', kind = 'scatter')
bx = s.plot(x = 'Time' , y = 'Hum', kind = 'scatter')
cx = s.plot(x = 'Time' , y = 'Press', kind = 'scatter')
dx = s.plot(x = 'Time' , y = 'Alt', kind = 'scatter')
