# with categories

import json, ast
import requests
from pytrends.request import TrendReq
import time
import sys
from numpy import corrcoef
from random import randint
import csv

google_username = "cuiminny@gmail.com"
google_password = ""
# pytrend = TrendReq(google_username, google_password,custom_useragent=str(randint(0,1000)))

# search_bands = [
# 	"Prince",
# 	"Bob Dylan",
# 	"Queen",
# 	"Kitten",
# 	"Adele"	
# ]

# read band names from csv
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
search_bands =  bandlist

for band in search_bands:
	# trend_payload_o = {'q': band}
	# df_o = pytrend.trend(trend_payload_o, return_type='dataframe')
	# df_o.columns = [band.lower()]	
	
	pytrend = TrendReq(google_username, google_password,custom_useragent=str(randint(0,1000)))
	
	trend_payload_cat = {'q': band, 'cat': '35'}        # music & audio
	df_cat = pytrend.trend(trend_payload_cat, return_type='dataframe')
	df_cat.columns = [band.lower()]	
	
	sys.stdout.flush()
	time.sleep(randint(10, 12))
	
	sugg = pytrend.suggestions(band)

	target_terms = ["band","songwriter","singer","artist","musical group","composer","music producer","musical duo","music performer","actor","music"]

	trans_suggests = ast.literal_eval(json.dumps(sugg))
	suggested_labels = trans_suggests['default']['topics']

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
		search_term = band

	print(search_term)
	
	pytrend = TrendReq(google_username, google_password,custom_useragent=str(randint(0,1000)))

	trend_payload = {'q': search_term}
	df = pytrend.trend(trend_payload, return_type='dataframe')
	df.columns = [band.lower()]	
	path = "/home/uwhpsc/wdocs/pytrends/pilot20/" + band + ".csv"
	df.to_csv(path)
	# path_o = "/home/uwhpsc/wdocs/pytrends/pilot20/" + band + "_original.csv"
	# df_o.to_csv(path_o)
	
	path_cat = "/home/uwhpsc/wdocs/pytrends/pilot20/" + band + "_cat.csv"
	df_cat.to_csv(path_cat)
	
	sys.stdout.flush()
	time.sleep(randint(10, 12))
	# time.sleep(3)
	
	# corr_matrix = corrcoef(df[band.lower()],df_o[band.lower()])
	corr_matrix = corrcoef(df[band.lower()],df_cat[band.lower()])
	corr_o = corr_matrix[0][1]
	print(corr_o)
	# print(df)
