# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 21:06:24 2019

@author: iasedric
"""

from pandas_datareader import data
#import matplotlib.pyplot as plt
import pandas as pd
import time
import numpy

# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.

tickers = pd.read_excel('tickers.xlsx', index_col=0)

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2017-11-03'
end_date = '2019-05-03'

Exit_FastStocks = open("Results stock growth.txt", 'w',encoding='utf-8')

for ticker in tickers.iterrows():
    
    print(ticker[0]) 
    
    try:
        panel_data = data.DataReader(ticker[0], 'iex', start_date, end_date)
    
        close = panel_data['close']
    except:
        print("Error: problem with reading")
        
     
    
    try:
        FiveDays = round((close.iloc[-1] - close.iloc[-5])/close.iloc[-5]*100,2)
        
    except:
        FiveDays = 0
   
    try:
        FifteenDays = round((close.iloc[-1] - close.iloc[-15])/close.iloc[-15]*100,2)
        
    except:
        FiveDays = 0
        
    try:
        ThirtyDays = round((close.iloc[-1] - close.iloc[-30])/close.iloc[-30]*100,2)
         
    except:
        ThirtyDays = 0
        
    try:
        SixtyDays = round((close.iloc[-1] - close.iloc[-60])/close.iloc[-60]*100,2)
         
    except:
        SixtyDays = 0    
        
    try:
        NinetyDays = round((close.iloc[-1] - close.iloc[-90])/close.iloc[-90]*100,2)
        
    except:
        NinetyDays = 0
        
    try:
        HFiftyDays = round((close.iloc[-1] - close.iloc[-150])/close.iloc[-150]*100,2)
        
    except:
        HFiftyDays = 0
        
    try:
        ThreeHDays = round((close.iloc[-1] - close.iloc[-360])/close.iloc[-360]*100,2)
    except:
        ThreeHDays = 0
        
 
    growth = [FiveDays, FifteenDays, ThirtyDays, SixtyDays, NinetyDays , HFiftyDays, ThreeHDays]
        
    if min(growth)> 0:
        isPositive =  True
    else:
        isPositive = False
        
    try:   
        Exit_FastStocks.write(str(ticker) + "^" + str(growth[0])+"%"  + "^" + str(growth[1])+"%" + "^" + str(growth[2])+"%" + "^" + str(growth[3])+"%" + "^" + str(growth[4])+"%" + "^" + str(growth[5])+"%" + "^" + str(growth[6])+"%" + "^" + str(close.iloc[-1]) + "^" + str(isPositive) + "^" + str(numpy.average(growth)) + "\n")
    except:
        Exit_FastStocks.write(str(ticker) + "^" + "No information" + "\n") 

    
    time.sleep(2)  

Exit_FastStocks.close()