# Importing Libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Calling the bio-sensing data 
data1 = pd.read_csv('Bunty-20221012.csv', usecols = ['Time', 'Temp', 'Hum', 'Press', 'Alt'])
data2 = pd.read_csv('bunty-20221013.csv', usecols = ['Time', 'Temp', 'Hum', 'Press', 'Alt'])
data3 = pd.read_csv('bunty-20221014.csv', usecols = ['Time', 'Temp', 'Hum', 'Press', 'Alt'])
data4 = pd.read_csv('bunty-20221015.csv', usecols = ['Time', 'Temp', 'Hum', 'Press', 'Alt'])
data5 = pd.read_csv('bunty-20221023.csv', usecols = ['Time', 'Temp', 'Hum', 'Press', 'Alt'])
data6 = pd.read_csv('bunty-20221024.csv', usecols = ['Time', 'Temp', 'Hum', 'Press', 'Alt'])
data7 = pd.read_csv('bunty-20221031.csv', usecols = ['Time', 'Temp', 'Hum', 'Press', 'Alt'])
data8 = pd.read_csv('bunty-20221101.csv', usecols = ['Time', 'Temp', 'Hum', 'Press', 'Alt'])
data9 = pd.read_csv('heron-20221025.csv', usecols = ['Time', 'Temp', 'Hum', 'Press', 'Alt'])
data10 = pd.read_csv('heron-20221026.csv', usecols = ['Time', 'Temp', 'Hum', 'Press', 'Alt'])
data11 = pd.read_csv('heron-20221027.csv', usecols = ['Time', 'Temp', 'Hum', 'Press', 'Alt'])
data12 = pd.read_csv('heron-20221028.csv', usecols = ['Time', 'Temp', 'Hum', 'Press', 'Alt'])
data13 = pd.read_csv('heron-20221031.csv', usecols = ['Time', 'Temp', 'Hum', 'Press', 'Alt'])
data14 = pd.read_csv('heron-20221101.csv', usecols = ['Time', 'Temp', 'Hum', 'Press', 'Alt'])

# Plotting All the Data 
# Temperature
def plottingTemp(data):
    ax1 = data.plot(x = 'Time' , y = 'Temp', kind = 'scatter')
    
# Humidity
def plottingHum(data):
    bx1 = data.plot(x = 'Time' , y = 'Hum', kind = 'scatter')
    
# Pressure
def plottingPress(data):
    cx1 = data.plot(x = 'Time' , y = 'Press', kind = 'scatter')
    
# Altitude
def plottingAlt(data):
    dx1 = data.plot(x = 'Time' , y = 'Alt', kind = 'scatter')
    
# Menu to view plots seperately 
def menu():    
    
    # User Input
    userChoice = int(input('Select: 1 for temperature, 2 for humidity, 3 for pressure, 4 for altitude.'))

    # Temperature 
    if userChoice == 1:

        # Plotting
        plottingTemp(data1)
        plottingTemp(data2)
        plottingTemp(data3)
        plottingTemp(data4)
        plottingTemp(data5)
        plottingTemp(data6)
        plottingTemp(data7)
        plottingTemp(data8)
        plottingTemp(data9)
        plottingTemp(data10)
        plottingTemp(data11)
        plottingTemp(data12)
        plottingTemp(data13)
        plottingTemp(data14)

    # Humidity
    elif userChoice == 2:

        # Plotting
        plottingHum(data1)
        plottingHum(data2)
        plottingHum(data3)
        plottingHum(data4)
        plottingHum(data5)
        plottingHum(data6)
        plottingHum(data7)
        plottingHum(data8)
        plottingHum(data9)
        plottingHum(data10)
        plottingHum(data11)
        plottingHum(data12)
        plottingHum(data13)
        plottingHum(data14)

    # Pressure
    elif userChoice == 3:

        # Plotting 
        plottingPress(data1)
        plottingPress(data2)
        plottingPress(data3)
        plottingPress(data4)
        plottingPress(data5)
        plottingPress(data6)
        plottingPress(data7)
        plottingPress(data8)
        plottingPress(data9)
        plottingPress(data10)
        plottingPress(data11)
        plottingPress(data12)
        plottingPress(data13)
        plottingPress(data14)

    # Altitude
    elif userChoice == 4:

        # Plotting 
        plottingAlt(data1)
        plottingAlt(data2)
        plottingAlt(data3)
        plottingAlt(data4)
        plottingAlt(data5)
        plottingAlt(data6)
        plottingAlt(data7)
        plottingAlt(data8)
        plottingAlt(data9)
        plottingAlt(data10)
        plottingAlt(data11)
        plottingAlt(data12)
        plottingAlt(data13)
        plottingAlt(data14)
      
    # Error Validation if input is less than 1, more than 4, a float or a string   
    else: 
        check_user_input(userChoice)
        
# Validating that user input is correct        
def check_user_input(input):
    
    try:
        # Convert to int
        val = int(input)
        print('Input is incorrect integer')
        menu()
    
    except ValueError:
        try:
            # Convert to float 
            val = float(input)
            print('Incorrect, input is float')
            menu()
            
        except ValueError:
            print('Invalid, value cannot be string')
            menu()
            
# Running menu            
menu()