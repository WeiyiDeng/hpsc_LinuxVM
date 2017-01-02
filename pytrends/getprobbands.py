import json, ast
import csv
import sys
from random import randint
from pprint import pprint

# get problematic bands number
prob_bands = '/home/uwhpsc/wdocs/pytrends/bands2588_lab/problem_list.csv'
mytext0 = open(prob_bands, 'r')
line = mytext0.readlines()
# pprint(line)

probband_list = []
for ind in range(522):
	band_index = ast.literal_eval(line[ind])[1][0]
	probband_list = probband_list + [band_index]
print(probband_list)


# get the problematic bands names again from original newbandlist file
sample_bands = "/home/uwhpsc/wdocs/pytrends/newbandlist2588.csv"
mytext = open(sample_bands, 'r')
lines = mytext.readlines()

bandlist = []
# new_range = [x+20 for x in range(10)]
# for k in new_range:
# for k in range(15):
for k in probband_list:
	if k < 10:                            # get the correct char locations of band names
		band_name = [lines[k][5:-3]]
	elif k < 100:
		band_name = [lines[k][6:-3]]
	elif k < 1000:
		band_name = [lines[k][7:-3]]
	else:
		band_name = [lines[k][8:-3]]
	bandlist = bandlist + band_name
print(bandlist)
search_terms =  bandlist
