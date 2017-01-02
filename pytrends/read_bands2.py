import json, ast
import csv
import sys
# import codecs

sample_bands = "/home/uwhpsc/wdocs/pytrends/newbandlist2588.csv"
# sample_bands = "/home/uwhpsc/wdocs/pytrends/sample_bands_50.csv"
mytext = open(sample_bands, 'r')
lines = mytext.readlines()

# lines = codecs.open(sample_bands, 'r', encoding='utf-8').readlines()

print(lines)
print(lines[1][3:-3])

bandlist = []
for k in range(200):
	if k+1 < 10:                            # get the correct char locations of band names
		band_name = [lines[k+1][3:-3]]
	elif k+1 < 100:
		band_name = [lines[k+1][4:-3]]
	elif k+1 < 1000:
		band_name = [lines[k+1][5:-3]]
	else:
		band_name = [lines[k+1][6:-3]]
	bandlist = bandlist + band_name

print(bandlist)
