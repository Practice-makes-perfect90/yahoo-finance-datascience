def chooseTicker():    #send the choice to the parameters of the other functions
    theChoice = yf.Ticker(choice)


def tupleexample():
    res =tuple( zip(oldApple['Open'],oldApple['High']))
    for stock in res:
         print(stock)
    print("space!")


def graph():
    df = pd.DataFrame({'Open':oldApple['Open'], 'High':oldApple['High']})
    print(df)

    df.plot( kind = 'scatter', x = 'Open' , y = 'High', color = 'red')
    plt.title("plot")
    plt.show()
def checkForTicker(c):
    find = df[df[c].isin(Symbol)]
    if find == True:
          print("IT is here")
    else:
          print("Sorry please use correct ticker symbol") 


