import time

import socket
import socks

import requests
from bs4 import BeautifulSoup

from stem import Signal
from stem.control import Controller


controller = Controller.from_port(port=9051)

def connectTor():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5 , "127.0.0.1", 9050, True)
    socket.socket = socks.socksocket

def renew_tor():
    # controller.authenticate(<INSERT YOUR PASSPHRASE HERE>)
    controller.authenticate()
    controller.signal(Signal.NEWNYM)

def showmyip():
    url = "http://www.showmyip.gr/"
    r = requests.Session()
    page = r.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    ip_address = soup.find("span",{"class":"ip_address"}).text.strip()
    print(ip_address)


# for i in range(5):
#    renew_tor()
#    connectTor()
#    showmyip()
#   time.sleep(10)
    
#############################################################
# Random Name for custom_useragent
#############################################################

def randomName():
    import string
    import random
    name=""
    
    for i in range(random.randint(5,10)):
        name+=random.choice(string.ascii_letters)     
    return name

################################################################
# Main functions 
################################################################

def requestBands(band):  
    from pytrends.request import TrendReq
    # import time
    from random import randint
    
    
    google_username = "weiyiwdeng@gmail.com"  #put your gmail account
    google_password = "" #passwrd
    mes=0
    
    pytrend = TrendReq(google_username, google_password, custom_useragent=randomName())
    # trend_payload_cat = {'q': band, 'cat': '35'}        # music & audio
    # trend_payload_cat = {'q': band, 'cat': '3'}        # art & entertainment
    trend_payload_cat = {'q': band}                        # original search term
    
    while mes==0:
        try:           
            df_cat = pytrend.trend(trend_payload_cat, return_type='dataframe')
	    mes=1
	    
        except Exception:
            renew_tor()
            connectTor()
            showmyip() #optional
            pytrend = TrendReq(google_username, google_password, custom_useragent=randomName()) #connect to Google
            mes=0

    df_cat.columns = [band.lower()]
    return df_cat


##############################################
#   Execution
#############################################
import csv
import sys

sample_bands = "/home/uwhpsc/wdocs/pytrends/sample_bands_20.csv"
mytext = open(sample_bands, 'r')
lines = mytext.readlines()

bandlist = []
for k in range(20):
	if k+1 < 10:                            # get the correct char locations of band names
		band_name = [lines[k+1][5:-3]]
	elif k+1 < 100:
		band_name = [lines[k+1][6:-3]]
	elif k+1 < 1000:
		band_name = [lines[k+1][7:-3]]
	else:
		band_name = [lines[k+1][8:-3]]
	bandlist = bandlist + band_name
print(bandlist)
search_terms =  bandlist

for band in search_terms:	
	band_data=requestBands(band)
	sys.stdout.flush()
	time.sleep(10)
	# path = "/home/uwhpsc/wdocs/pytrends/test/" + band + "_cat.csv"
	# path = "/home/uwhpsc/wdocs/pytrends/test/" + band + "_cat3.csv"
	path = "/home/uwhpsc/wdocs/pytrends/test/" + band + ".csv"
	band_data.to_csv(path)
	print(band)
	
