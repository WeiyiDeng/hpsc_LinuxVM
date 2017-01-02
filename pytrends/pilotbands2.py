# with categories

import json, ast
import requests
from pytrends.request import TrendReq
import time
import sys
from numpy import corrcoef
from random import randint

google_username = "weiyiwdeng@gmail.com"
google_password = ""
pytrend = TrendReq(google_username, google_password)

search_bands = [
	"Prince",
	"Bob Dylan",
	"Queen",
	"Kitten",
	"Adele"	
]

for band in search_bands:
	# trend_payload_o = {'q': band}
	# df_o = pytrend.trend(trend_payload_o, return_type='dataframe')
	# df_o.columns = [band.lower()]	
	
	trend_payload_cat = {'q': band, 'cat': '35'}        # music & audio
	df_cat = pytrend.trend(trend_payload_cat, return_type='dataframe')
	df_cat.columns = [band.lower()]	
	
	sugg = pytrend.suggestions(band)

	target_terms = ["band","songwriter","singer","artist","musical group","composer","music producer","musical duo","music performer","actor"]

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
	
	sys.stdout.flush()
	time.sleep(randint(5, 10))
	# time.sleep(3)

	trend_payload = {'q': search_term}
	df = pytrend.trend(trend_payload, return_type='dataframe')
	df.columns = [band.lower()]	
	path = "/home/uwhpsc/wdocs/pytrends/pilot/" + band + ".csv"
	df.to_csv(path)
	# path_o = "/home/uwhpsc/wdocs/pytrends/pilot/" + band + "_original.csv"
	# df_o.to_csv(path_o)
	
	path_cat = "/home/uwhpsc/wdocs/pytrends/pilot/" + band + "_cat.csv"
	df_cat.to_csv(path_cat)
	# corr_matrix = corrcoef(df[band.lower()],df_o[band.lower()])
	corr_matrix = corrcoef(df[band.lower()],df_cat[band.lower()])
	corr_o = corr_matrix[0][1]
	print(corr_o)
	# print(df)
