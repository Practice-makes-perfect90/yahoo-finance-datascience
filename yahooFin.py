import yfinance as yf
import plotly.graph_objs as got
import datetime as dt
import pandas as pd
import requests
import os
from bs4 import BeautifulSoup
import pdb; pdb.set_trace()
##### This is the stock ticker list for the program ######



site = requests.get('https://www.slickcharts.com/sp500', headers={'User-agent': 'Mozilla/5.0'}).text
page=pd.read_html(site)
df=page[0]
df.to_csv('S&P500-Info.csv')
df.to_csv("S&P500-Symbols.csv", columns=['Symbol'])
print(df.head())



print("break!------------")

# this is the ticker symbol
Apple = yf.Ticker('AAPL')
Microsoft = yf.Ticker('MSFT')

# get data from these ranges
oldApple = Apple.history(start="2020-01-01", end="2020-08-21")

oldApple.head()

def chooseTicker():
    #send the choice to the parameters of the other functions
    theChoice = yf.Ticker(choice)


def tupleexample():
    res =tuple( zip(oldApple['Open'],oldApple['High']))
    for stock in res:
         print(stock)
    print("space!")


print(oldApple.head())
print(oldApple['Open'],oldApple['High'])
print("break-------------------------")
print(oldApple['Open'],oldApple['Close'])

def graph():
    df = pd.DataFrame({'Open':oldApple['Open'], 'High':oldApple['High']})
    print(df)

    df.plot( kind = 'scatter', x = 'Open' , y = 'High', color = 'red')
    plt.title("plot")
    plt.show()





exit = False
################

while exit != True:

    print("What do you want to doi? ")
    print("1 for look at stock ticker, 2 for visualize stock ticker,3 for comparing stock ticker,4 to view as tuple ")

    choice = input("Enter your choice ")
    choice = int(choice)
    stock = str("")

    if choice == 1:
        stock =input("enter a stock ticker for example apple is AAPL")

        Astock = yf.Ticker(stock)
        Astock = Astock.history(start="2019-01-01", end="2020-08-21")
        print(Astock)
    if choice == 2:
        graph()

    if choice ==3:
        print("placeholder")

    if choice ==4:
        tupleexample()











