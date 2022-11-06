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
def plottingTemp1(d1, d2, d3, d4, d5, d6, d7):
    
    # Figure
    fig = plt.figure(figsize = (20.0, 20.0))
    
    # Subplotting the plots
    ax1 = fig.add_subplot(4, 3, 1)
    ax2 = fig.add_subplot(4, 3, 2)
    ax3 = fig.add_subplot(4, 3, 3)
    ax4 = fig.add_subplot(4, 3, 4)
    ax5 = fig.add_subplot(4, 3, 5)
    ax6 = fig.add_subplot(4, 3, 6)
    ax7 = fig.add_subplot(4, 3, 7)
    
    # Plotting
    ax1.scatter(d1['Time'], d1['Temp'], color = 'red')
    ax2.scatter(d2['Time'], d2['Temp'], color = 'red')
    ax3.scatter(d3['Time'], d3['Temp'], color = 'red')
    ax4.scatter(d4['Time'], d4['Temp'], color = 'red')
    ax5.scatter(d5['Time'], d5['Temp'], color = 'red')
    ax6.scatter(d6['Time'], d6['Temp'], color = 'red')
    ax7.scatter(d7['Time'], d7['Temp'], color = 'red')

def plottingTemp2(d8, d9, d10, d11, d12, d13, d14): 
    
    # Figure 
    fig = plt.figure(figsize = (20.0, 20.0))
    
    # Subplotting the plots 
    ax8 = fig.add_subplot(4, 3, 1)
    ax9 = fig.add_subplot(4, 3, 2)
    ax10 = fig.add_subplot(4, 3, 3)
    ax11 = fig.add_subplot(4, 3, 4)
    ax12 = fig.add_subplot(4, 3, 5)
    ax13 = fig.add_subplot(4, 3, 6)
    ax14 = fig.add_subplot(4, 3, 7)
    
    # Plotting
    ax8.scatter(d8['Time'], d8['Temp'], color = 'red')
    ax9.scatter(d9['Time'], d9['Temp'], color = 'red')
    ax10.scatter(d10['Time'], d10['Temp'], color = 'red')
    ax11.scatter(d11['Time'], d11['Temp'], color = 'red')
    ax12.scatter(d12['Time'], d12['Temp'], color = 'red')
    ax13.scatter(d13['Time'], d13['Temp'], color = 'red')
    ax14.scatter(d14['Time'], d14['Temp'], color = 'red')

# Humidity
def plottingHum1(d1, d2, d3, d4, d5, d6, d7):
    
    # Figure
    fig = plt.figure(figsize = (20.0, 20.0))
    
    # Subplotting the plots
    ax1 = fig.add_subplot(4, 3, 1)
    ax2 = fig.add_subplot(4, 3, 2)
    ax3 = fig.add_subplot(4, 3, 3)
    ax4 = fig.add_subplot(4, 3, 4)
    ax5 = fig.add_subplot(4, 3, 5)
    ax6 = fig.add_subplot(4, 3, 6)
    ax7 = fig.add_subplot(4, 3, 7)
    
    # Plotting
    ax1.scatter(d1['Time'], d1['Hum'])
    ax2.scatter(d2['Time'], d2['Hum'])
    ax3.scatter(d3['Time'], d3['Hum'])
    ax4.scatter(d4['Time'], d4['Hum'])
    ax5.scatter(d5['Time'], d5['Hum'])
    ax6.scatter(d6['Time'], d6['Hum'])
    ax7.scatter(d7['Time'], d7['Hum'])
    
def plottingHum2(d8, d9, d10, d11, d12, d13, d14):
    
    # Figure 
    fig = plt.figure(figsize = (20.0, 20.0))
    
    # Subplotting the plots 
    ax8 = fig.add_subplot(4, 3, 1)
    ax9 = fig.add_subplot(4, 3, 2)
    ax10 = fig.add_subplot(4, 3, 3)
    ax11 = fig.add_subplot(4, 3, 4)
    ax12 = fig.add_subplot(4, 3, 5)
    ax13 = fig.add_subplot(4, 3, 6)
    ax14 = fig.add_subplot(4, 3, 7)
    
    # Plotting
    ax8.scatter(d8['Time'], d8['Hum'])
    ax9.scatter(d9['Time'], d9['Hum'])
    ax10.scatter(d10['Time'], d10['Hum'])
    ax11.scatter(d11['Time'], d11['Hum'])
    ax12.scatter(d12['Time'], d12['Hum'])
    ax13.scatter(d13['Time'], d13['Hum'])
    ax14.scatter(d14['Time'], d14['Hum'])
    
# Pressure
def plottingPress1(d1, d2, d3, d4, d5, d6, d7):
    
    # Figure
    fig = plt.figure(figsize = (20.0, 20.0))
    
    # Subplotting the plots
    ax1 = fig.add_subplot(4, 3, 1)
    ax2 = fig.add_subplot(4, 3, 2)
    ax3 = fig.add_subplot(4, 3, 3)
    ax4 = fig.add_subplot(4, 3, 4)
    ax5 = fig.add_subplot(4, 3, 5)
    ax6 = fig.add_subplot(4, 3, 6)
    ax7 = fig.add_subplot(4, 3, 7)
    
    # Plotting
    ax1.scatter(d1['Time'], d1['Press'], color = 'purple')
    ax2.scatter(d2['Time'], d2['Press'], color = 'purple')
    ax3.scatter(d3['Time'], d3['Press'], color = 'purple')
    ax4.scatter(d4['Time'], d4['Press'], color = 'purple')
    ax5.scatter(d5['Time'], d5['Press'], color = 'purple')
    ax6.scatter(d6['Time'], d6['Press'], color = 'purple')
    ax7.scatter(d7['Time'], d7['Press'], color = 'purple')
    
    
def plottingPress2(d8, d9, d10, d11, d12, d13, d14):
    
    # Figure 
    fig = plt.figure(figsize = (20.0, 20.0))
    
    # Subplotting the plots 
    ax8 = fig.add_subplot(4, 3, 1)
    ax9 = fig.add_subplot(4, 3, 2)
    ax10 = fig.add_subplot(4, 3, 3)
    ax11 = fig.add_subplot(4, 3, 4)
    ax12 = fig.add_subplot(4, 3, 5)
    ax13 = fig.add_subplot(4, 3, 6)
    ax14 = fig.add_subplot(4, 3, 7)
    
    # Plotting
    ax8.scatter(d8['Time'], d8['Press'], color = 'purple')
    ax9.scatter(d9['Time'], d9['Press'], color = 'purple')
    ax10.scatter(d10['Time'], d10['Press'], color = 'purple')
    ax11.scatter(d11['Time'], d11['Press'], color = 'purple')
    ax12.scatter(d12['Time'], d12['Press'], color = 'purple')
    ax13.scatter(d13['Time'], d13['Press'], color = 'purple')
    ax14.scatter(d14['Time'], d14['Press'], color = 'purple')
    
# Altitude
def plottingAlt1(d1, d2, d3, d4, d5, d6, d7):
    
    # Figure
    fig = plt.figure(figsize = (20.0, 20.0))
    
    # Subplotting the plots
    ax1 = fig.add_subplot(4, 3, 1)
    ax2 = fig.add_subplot(4, 3, 2)
    ax3 = fig.add_subplot(4, 3, 3)
    ax4 = fig.add_subplot(4, 3, 4)
    ax5 = fig.add_subplot(4, 3, 5)
    ax6 = fig.add_subplot(4, 3, 6)
    ax7 = fig.add_subplot(4, 3, 7)
    
    # Plotting
    ax1.scatter(d1['Time'], d1['Alt'], color = 'orange')
    ax2.scatter(d2['Time'], d2['Alt'], color = 'orange')
    ax3.scatter(d3['Time'], d3['Alt'], color = 'orange')
    ax4.scatter(d4['Time'], d4['Alt'], color = 'orange')
    ax5.scatter(d5['Time'], d5['Alt'], color = 'orange')
    ax6.scatter(d6['Time'], d6['Alt'], color = 'orange')
    ax7.scatter(d7['Time'], d7['Alt'], color = 'orange')
    
    
def plottingAlt2(d8, d9, d10, d11, d12, d13, d14): 
    
    # Figure 
    fig = plt.figure(figsize = (20.0, 20.0))
    
    # Subplotting the plots 
    ax8 = fig.add_subplot(4, 3, 1)
    ax9 = fig.add_subplot(4, 3, 2)
    ax10 = fig.add_subplot(4, 3, 3)
    ax11 = fig.add_subplot(4, 3, 4)
    ax12 = fig.add_subplot(4, 3, 5)
    ax13 = fig.add_subplot(4, 3, 6)
    ax14 = fig.add_subplot(4, 3, 7)
    
    # Plotting
    ax8.scatter(d8['Time'], d8['Alt'], color = 'orange')
    ax9.scatter(d9['Time'], d9['Alt'], color = 'orange')
    ax10.scatter(d10['Time'], d10['Alt'], color = 'orange')
    ax11.scatter(d11['Time'], d11['Alt'], color = 'orange')
    ax12.scatter(d12['Time'], d12['Alt'], color = 'orange')
    ax13.scatter(d13['Time'], d13['Alt'], color = 'orange')
    ax14.scatter(d14['Time'], d14['Alt'], color = 'orange')
# Menu to view plots seperately 
def menu():    
    
    # User Input
    userChoice = int(input('Select: 1 for temperature, 2 for humidity, 3 for pressure, 4 for altitude.'))

    # Temperature 
    if userChoice == 1:

        # Plotting
        plottingTemp1(data1, data2, data3, data4, data5, data6, data7)
        plottingTemp2(data8, data9, data10, data11, data12, data13, data14)
        
    # Humidity
    elif userChoice == 2:

        # Plotting
        plottingHum1(data1, data2, data3, data4, data5, data6, data7)
        plottingHum2(data8, data9, data10, data11, data12, data13, data14)
    
    # Pressure
    elif userChoice == 3:

        # Plotting 
        plottingPress1(data1, data2, data3, data4, data5, data6, data7)
        plottingPress2(data8, data9, data10, data11, data12, data13, data14)

    # Altitude
    elif userChoice == 4:

        # Plotting 
        plottingAlt1(data1, data2, data3, data4, data5, data6, data7)
        plottingAlt2(data8, data9, data10, data11, data12, data13, data14)

    # Error Validation if input is less than 1, more than 4, a float or a string   
    else: 
        check_user_input(userChoice)
        
# Validating that user input is correct        
def check_user_input(input):
    
    try:
        # Verify if int
        val = int(input)
        print('Input is incorrect integer', val)
        menu()
    
    except ValueError:
        try:
            # Verify if float 
            val = float(input)
            print('Incorrect, input is float', val)
            menu()
            
        except ValueError:
            print('Invalid, value cannot be string')
            menu()
            
# Running menu            
menu()