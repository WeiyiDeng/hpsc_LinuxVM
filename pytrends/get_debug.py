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
def requestSuggestions(band_name):  
    from pytrends.request import TrendReq
    # import time
    from random import randint
    
    
    google_username = "cuiminny@gmail.com"  #put your gmail account
    google_password = "" #passwrd
    mes=0
    
    pytrend = TrendReq(google_username, google_password, custom_useragent=randomName())
    # trend_payload_cat = {'q': band, 'cat': '35'}        # music & audio
    # trend_payload_cat = {'q': band, 'cat': '3'}        # art & entertainment
    # trend_payload_lab = {'q': band}                        # original search term
    
    while mes==0:
        try:           
            sugg = pytrend.suggestions(band_name)
	    mes=1
	    
        except Exception:
            renew_tor()
            connectTor()
            showmyip() #optional
            pytrend = TrendReq(google_username, google_password, custom_useragent=randomName()) #connect to Google
            mes=0

    # df_lab.columns = [band.lower()]
    target_terms = ["band","songwriter","singer","artist","musical group","composer","music producer","musical duo","music performer","actor","music"]
    trans_suggests = ast.literal_eval(json.dumps(sugg))
    suggested_labels = trans_suggests['default']['topics']
    
    if suggested_labels ==[]:
	    search_term = band_name + "sth"
    else:
	    length_labels = len(suggested_labels)

		# any(word in 'a' for word in ['a','b'])          # returns True
		# any(word in 'ab' for word in ['a','b'])         # returns True
	    ind = 0
	    for k in range(length_labels):
		label_list = suggested_labels[k]
		if any(w in label_list['type'].lower() for w in target_terms):
			if label_list['title'].lower()==band.lower():
				search_term = label_list['mid']
				ind = ind+1
				break
		if ind==0:
		# print("p not found")
			search_term = band_name	
    return search_term


def requestBands(search_term):  
    from pytrends.request import TrendReq
    # import time
    from random import randint
    
    
    google_username = "weiyiwdeng@gmail.com"  #put your gmail account
    google_password = "" #passwrd
    mes=0
    times_tried = 0
    
    pytrend = TrendReq(google_username, google_password, custom_useragent=randomName())
    # trend_payload_cat = {'q': band, 'cat': '35'}        # music & audio
    # trend_payload_cat = {'q': band, 'cat': '3'}        # art & entertainment
    trend_payload_lab = {'q': search_term}                        # original search term
    
    while mes==0:
        try:           
            df_lab = pytrend.trend(trend_payload_lab, return_type='dataframe')
	    mes=1
	    
        except Exception:
	# except (RateLimitError, ResponseError):
            renew_tor()
            connectTor()
            showmyip() #optional
            pytrend = TrendReq(google_username, google_password, custom_useragent=randomName()) #connect to Google
            mes=0
	    times_tried = times_tried +1
	    if times_tried >15:                                                 # pass after 15 trials
		    import pandas as pd
	            index = [1,2,3]
		    df_lab = pd.DataFrame(index=index, columns=[band])
		    mes=1
	 
	# or ConnectionError ?
        # except (ConnectionError) as err:                            # does not seem to work
	    # print(err)
	    # import pandas as pd
	    # index = [1,2,3]
	    # df_lab = pd.DataFrame(index=index, columns=[band])
	    # mes = 1
	    # pass
    
    df_lab.columns = [band.lower()]
    return df_lab


##############################################
#   Execution
#############################################
import json, ast
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
# search_terms =  bandlist
search_terms = ["I Break Horses", "Pale Seas"]
# search_terms = ["I Break Horses"]

search_list = []
for band in search_terms:
	band_sugg = requestSuggestions(band)
	search_list = search_list+[band_sugg]
	band_data=requestBands(band_sugg)
	sys.stdout.flush()
	time.sleep(10)
	# path = "/home/uwhpsc/wdocs/pytrends/test/" + band + "_cat.csv"
	# path = "/home/uwhpsc/wdocs/pytrends/test/" + band + "_cat3.csv"
	path = "/home/uwhpsc/wdocs/pytrends/test/" + band + "_lab.csv"
	band_data.to_csv(path)
	print(band)

print(search_list)

f = open('/home/uwhpsc/wdocs/pytrends/test/search_list.csv', "w")
mydoc = csv.writer(f, lineterminator='\n')
mydoc.writerow(search_list)
f.close()
