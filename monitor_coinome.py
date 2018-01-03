import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime

def fetchData() :
    weblink = "https://www.coinome.com/exchange"
    webpage = urllib.request.urlopen(weblink)
    websoup = BeautifulSoup(webpage, "html.parser")

    therow = websoup.body.nav
    therow = therow.find("div", {"class" : "nav-utility"})
    therow = therow.find("div", {"class" : "row"})
    therow = therow.find_all("div", {"class" : "pl15"})

    datablock = []
    for item in therow :
        item1 = item.a.find("span", {"class" : "last-market-rate-b"})
        datablock.append(item1.span.string)
    return datablock

# ::: MAIN from here :::

datenow = datetime.now().date()
print(" %s \t\t %s \t\t %s \t %s \t %s \n" %
        ("DATE", "TIME", "BTC/INR", "BCH/INR", "LTC/INR"))

while True :
    timenow = datetime.now().strftime('%H:%M:%S')
    data = fetchData()
    print(" %s \t %s \t %s \t %s \t %s " %
            (datenow, timenow, data[0], data[1], data[2]))
