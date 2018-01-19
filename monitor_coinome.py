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
    print("Date", "\t Time", "\t BTC/INR", "BCH/INR", "LTC/INR", "DASH\INR", sep=" \t ")
    while(True) :
        db = fetchDataOnce()
        #print("%s\t%s\t%s\t%s" % {db[1], db[2], db[3], db[4]})
        print(db[0].date(), db[0].strftime("%H:%M:%S"), db[1], db[2], db[3], db[4], sep=" \t ")
        time.sleep(30)

# ::: MAIN from here :::

printData()
