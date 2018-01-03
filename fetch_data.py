import urllib.request
# Requires you to have Beautiful Soup pre-installed
from bs4 import BeautifulSoup

# Get the webpage and apply BeautifulSoup
weblink = "https://www.coinome.com/exchange"
webpage = urllib.request.urlopen(weblink)
websoup = BeautifulSoup(webpage, "html.parser")

# Zoom into the data block
therow = websoup.body.nav
therow = therow.find("div", {"class" : "nav-utility"})
therow = therow.find("div", {"class" : "row"})
therow = therow.find_all("div", {"class" : "pl15"})

# Print the data
for item in therow :
    item1 = item.a.find("span", {"class" : "small"})
    item2 = item.a.find("span", {"class" : "last-market-rate-b"})
    print("%s : %s\n" % (item1.string, item2.span.string))
