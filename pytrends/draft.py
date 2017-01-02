def divide(x, y):
    quotient = x/y
    remainder = x % y
    return quotient, remainder  

q, r = divide(22, 7)

print(q)
print(r)

d = 3+r
print(d)

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

renew_tor()
connectTor()
showmyip() 

import json, ast
from pprint import pprint
from pytrends.request import TrendReq

google_username = ""
google_password = ""
pytrend = TrendReq(google_username, google_password)

band = 'Diamond Messages'
# uband = u'Los \xc3\x81ngeles Azules'                             # did not work
# band = uband.encode('utf-8')

sugg = pytrend.suggestions(band)
pprint(sugg, width=1)
# sugg == []

target_terms = ["band","songwriter","singer","artist","musical group","composer","music producer","musical duo","music performer","actor","music","dj","electronic duo"]
trans_suggests = ast.literal_eval(json.dumps(sugg))
suggested_labels = trans_suggests['default']['topics']

length_labels = len(suggested_labels)

for k in range(length_labels):
	label_list = suggested_labels[k]
	if any(w in label_list['type'].lower() for w in target_terms):
		if label_list['title'].lower()==band.lower():
			search_term = label_list['mid']
			break
print(search_term)
# print(sugg)
