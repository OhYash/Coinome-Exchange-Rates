import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

def fetchDataOnce() :
    weblink = "https://www.coinome.com/exchange"
    webpage = urllib.request.urlopen(weblink)
    websoup = BeautifulSoup(webpage, "html.parser")

    therow = websoup.body.nav
    therow = therow.find("div", {"class" : "nav-utility"})
    therow = therow.find("div", {"class" : "row"})
    therow = therow.find_all("div", {"class" : "pl15"})

    datablock = []
    datablock.append(datetime.now().date())
    datablock.append(datetime.now().strftime('%H:%M:%S'))
    for item in therow :
        item1 = item.a.find("span", {"class" : "last-market-rate-b"})
        datablock.append(item1.span.string)
    dataframe = pd.DataFrame(data = [datablock], columns=['Date', 'Time', 'BTC/INR', 'BCH/INR', 'LTC/INR'])
    return dataframe

def printData() :
    df = fetchDataOnce()
    df.set_index(['Date', 'Time'], inplace=True)
    print(df)

# ::: MAIN from here :::

printData()
