import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import time
import sqlite3

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
    return datablock

def printData() :
    print("Date/Time\tBTC/INR\tBCH/INR\tLTC/INR")
    while(True) :
        db = fetchDataOnce()
        print("%d\t%d\t%d\t%d" % {db[0], db[1], db[2], db[3]})
        time.sleep(30)

# ::: MAIN from here :::

printData()
