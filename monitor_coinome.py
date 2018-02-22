import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import time
import sqlite3
import sys
import os

_printData = True
_storeData = False
_printOnce = False
_sec = 30

def fetchDataOnce() :
    # Fetches data once.
    # Return the datablock as a list.
    # List Structure : DateTime, BTC/INR, BCH/INR, LTC/INR, DASH/INR, DGB/INR, ZEC/INR
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
    print(db[0].date(), db[0].strftime("%H:%M:%S"), db[1], db[2], db[3], db[4], db[5], " ", db[6], sep=" \t ")

def parseArguments(args) :
    global _printData
    global _storeData
    global _printOnce
    global _sec
    for arg in args :
        if arg in ("-n", "--noprint") :
            _storeData = True
            _printData = False
        elif arg in ("-o", '--once') :
            _printOnce = True
        elif arg in ("-s", "--store") :
            _storeData = True
        elif arg in ("-t", "--time") :
            _sec = int(args[args.index(arg)+1])
        elif arg in ("-h", "--help") :
            usage()
            sys.exit(0)
     
def usage() :
    print("Coinome Price fetcher by Yash Yadav (yashdimpu@gmail.com)\n")
    print("Usage : python monitor_coinome.py [options]")
    print("\nOptions :")
    print("-n, --noprint \t\t Only store data, dont print")
    print("-o, --once \t\t Print data once and exit")
    print("-s, --store \t\t Store the data in database")
    print("-t, --time NUM \t\t Set NUM seconds delay between each time data is fetched(Default is 30)")
    print("-h, --help \t\t Display this help and exit")

def printInfo() :
    print("Coinome Price Fetcher")
    print("Store : %s | Refresh frequency : %d" % (_storeData, _sec))

def openDatabase() :
    _fileName = ("data/db_%s.db" % datetime.now().date().strftime("%b_%Y"))
    # Connect to the database
    conn = sqlite3.connect(_fileName)
    curr = conn.cursor()
    # Return cursor
    return curr

def storeData(curr) :
    # Create table
    curr.execute('''CREATE TABLE IF NOT EXISTS RATES_%d
        (time text, BTCINR real, BCHINR real, LTCINR real, DASHINR real, DGBINR real, ZECINR real)''' % datetime.now().day)
    #Store data
    data = (db[0].strftime("%H:%M:%S"),
           float(db[1].replace(',','')),
           float(db[2].replace(',','')),
           float(db[3].replace(',','')),
           float(db[4].replace(',','')),
           float(db[5].replace(',','')),
           float(db[6].replace(',','')))
    curr.execute("INSERT INTO RATES_%d VALUES(?, ?, ?, ?, ?, ?, ?)" % db[0].day, data)


# ::: MAIN from here :::

#Parse Commandline Arguments
parseArguments(sys.argv[1:])

#Creates database folder in the first run
if not os.path.exists("data") :
    os.makedirs("data")

#Print Options
printInfo()

#Print table headers
if(_printData) :
    print("Date", "\t Time", "\t BTC/INR", "BCH/INR", "LTC/INR", "DASH/INR", "DGB/INR", "ZEC/INR", sep=" \t ")
#Open Database
if(_storeData) :
    curr = openDatabase()

#The Scraping happens from here
try :
    while(True) :
        db = fetchDataOnce()
        if(_printData) :
            printData()
        if(_storeData) :
            storeData(curr)
        if(_printOnce) :
            sys.exit(0)
        time.sleep(_sec)
except KeyboardInterrupt : 
    print("\nQuitting")
    if(_storeData) :
        curr.close()
