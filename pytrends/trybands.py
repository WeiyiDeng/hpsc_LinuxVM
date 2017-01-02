import json, ast
import requests
from pytrends.request import TrendReq

google_username = "weiyiwdeng@gmail.com"
google_password = ""
pytrend = TrendReq(google_username, google_password)

sugg = pytrend.suggestions('Prince')

target_terms = ["band","songwriter","singer"]

trans_suggests = ast.literal_eval(json.dumps(sugg))
suggested_labels = trans_suggests['default']['topics']

length_labels = len(suggested_labels)

# any(word in 'a' for word in ['a','b'])          # returns True
# any(word in 'ab' for word in ['a','b'])         # returns True
for k in range(length_labels):
	label_list = suggested_labels[k]
	if any(w in label_list['type'].lower() for w in target_terms):
		if label_list['title'].lower()=='Prince'.lower():
			search_term = label_list['mid']
			break
		else:
			print("Prince not found")
			search_term = "Prince"

print(search_term)

trend_payload = {'q': search_term}
df = pytrend.trend(trend_payload, return_type='dataframe')
df.to_csv('/home/uwhpsc/wdocs/pytrends/prince.csv')
print(df)
