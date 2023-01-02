import yfinance as yf
import plotly.graph_objs as got
import datetime as dt
import pandas as pd
import requests
import os
from bs4 import BeautifulSoup
#import pdb; pdb.set_trace() # Debugger 
from functions import chooseTicker 
from functions import graph
from functions import tupleexample 

##### This is the stock ticker list for the program ######
#--------------------------------------------------------------
# Examples of what to do ot get output 
# this is the ticker symbol
#Apple = yf.Ticker('AAPL')
#Microsoft = yf.Ticker('MSFT')print(oldApple.head())
#print(oldApple['Open'],oldApple['High'])
#print("break-------------------------")
#print(oldApple['Open'],oldApple['Close'])
#--------------------------------------------------------------
#This is how you get data from ranges 
#oldApple = Apple.history(start="2020-01-01", end="2020-08-21")
#oldApple.head()



site = requests.get('https://www.slickcharts.com/sp500', headers={'User-agent': 'Mozilla/5.0'}).text
page=pd.read_html(site)
df=page[0]
df.to_csv('S&P500-Info.csv')
df.to_csv("S&P500-Symbols.csv", columns=['Symbol'])
print(df.head())
print(df.tail())
print(df.info())
print(df['Price'])
print(df[['Chg','Price']])



exit = False


while exit != True:

    print("What do you want to do? ")
    print("1 for look at stock ticker, 2 for visualize stock ticker,3 for comparing stock ticker,4 to view as tuple ")

    choice = input("Enter your choice ")
    choice = int(choice)
    stock = str("")

    if choice == 1:
        print("Enter a stock ticker from the S%P 500, Make sure it is listed ")
        stock =input(" enter a stock ticker for example apple is AAPL ")
        find = stock in df["Symbol"].unique()
        print(find)
        if find == True:
            print("IT is here")
        else:
            print("Sorry please use correct ticker symbol")

        Astock = yf.Ticker(stock)
        Astock = Astock.history(start="2019-01-01", end="2020-08-21")
        print(Astock)
    if choice == 2:
        graph()

    if choice ==3:
        print("placeholder")

    if choice ==4:
        tupleexample()











