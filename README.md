# Coinome-Exchange-Rates
---
Web Scraper written in python 3 with BeautifulSoup4 library to catch live exchange rates from coinome.  
Supports but displaying and storing the data in database (database backend is sqlite3).

Head over to the `basic` branch for a minimal scraper.

# Installation  
Requires [Python 3](https://www.python.org/downloads/) and [BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)    

## Usage
Clone this repository and run 'monitor_coinome.py'   

Usage : python monitor_coinome.py [options]

Options :
-n, --noprint            Only store data, dont print
-o, --once               Print data once and exit
-s, --store              Store the data in database (Default : False)
-t, --time NUM           Set NUM seconds delay between each time data is fetched (Default : 30)
-h, --help               Display help and exit
