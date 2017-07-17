import json, ast
import csv
import sys
# import codecs

sample_bands = "/home/uwhpsc/wdocs/pytrends/newbandlist4061.csv"
# sample_bands = "/home/uwhpsc/wdocs/pytrends/sample_bands_50.csv"
mytext = open(sample_bands, 'r')
lines = mytext.readlines()

# lines = codecs.open(sample_bands, 'r', encoding='utf-8').readlines()

# print(lines)
# print(lines[1][3:-3])

def isEnglish(s):             # detects if string contains only English/Roman letters and symbols
    try:
        s.decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

bandlist = []
for k in range(200):
	if " " in lines[k+1] or isEnglish(lines[k+1])==0:
		d = 0                               # if there are spaces or non-English characters in band names, there are double quotes 
	else:                                   # if no space or non_English in band name, there are no quotes and the indices expand
		d = 1                               
	if k+1 < 10:                            # get the correct char locations of band names
		band_name = lines[k+1][3-d:-3+d]
	elif k+1 < 100:
		band_name = lines[k+1][4-d:-3+d]
	elif k+1 < 1000:
		band_name = lines[k+1][5-d:-3+d]
	else:
		band_name = lines[k+1][6-d:-3+d]
	bandlist = bandlist + [band_name.replace("\"","")]      # remove additional double quotes from string

print(bandlist)
