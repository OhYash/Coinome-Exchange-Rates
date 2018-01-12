import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

def fetchDataOnce() :
    # Fetches data once.
    # Return the datablock as a list.
    # List Structure : DateTime, BTC/INR, BCH/INR, LTC/INR
    weblink = "https://www.coinome.com/exchange"
    webpage = urllib.request.urlopen(weblink)
    datetimenow = datetime.now()
    websoup = BeautifulSoup(webpage, "html.parser")

    therow = websoup.body.nav
    therow = therow.find("div", {"class" : "nav-utility"})
    therow = therow.find("div", {"class" : "row"})
    therow = therow.find_all("div", {"class" : "pl15"})

    datablock = []
    datablock.append(datetimenow)
    for item in therow :
        item1 = item.a.find("span", {"class" : "last-market-rate-b"})
        datablock.append(item1.span.string)
    #dataframe = pd.DataFrame(data = [datablock], columns=['Date', 'Time', 'BTC/INR', 'BCH/INR', 'LTC/INR'])
    #return dataframe
    return datablock

def printData() :
    db = fetchDataOnce()
    df = pd.DataFrame(data = [db], columns=['Date-Time', 'BTC/INR', 'BCH/INR', 'LTC/INR'])
    df.set_index(['Date-Time'], inplace=True)
    print(df)

# ::: MAIN from here :::

printData()
