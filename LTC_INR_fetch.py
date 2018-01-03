import urllib.request
from bs4 import BeautifulSoup
weblink = "https://www.coinome.com/exchange"

webpage = urllib.request.urlopen(weblink)
websoup = BeautifulSoup(webpage, "html.parser")

therow = websoup.body.nav
therow = therow.find("div", {"class" : "nav_utility"})
therow = therow.find("div", {"class" : "row"})
therow = therow.find_all("div", {"class" : "pl15"})

for item in therow :
    item1 = item.a.find("span", {"class" : "small"})
    item2 = item.a.find("span", {"class" : "last-market-share-b"})
    print("%s : %s\n" % (item1.string, item2.span.string))
