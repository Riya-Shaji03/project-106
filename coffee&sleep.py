import numpy as np
import csv
import pandas as pd
import plotly_express as pe

def getDataSource(data_path):
    cupsOfCoffee = []
    sleepHours = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for i in csv_reader:
            cupsOfCoffee.append(float(i['Coffee in ml']))
            sleepHours.append(float(i['sleep in hours']))
    
    return{'x' : cupsOfCoffee, 'y' : sleepHours}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource['x'],datasource['y'])
    print('Correlation between cups of coffee and number of hours of sleep is:  \n --->', correlation[0,1])
    
def plotFigure(data_path):
    df = pd.read_csv('data.csv')
    scatter = pe.scatter(df, x='week', y='Coffee in ml', color='sleep in hours')
    scatter.show()

def setup():
    data_path = 'data.csv'
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    plotFigure(data_path)

setup()