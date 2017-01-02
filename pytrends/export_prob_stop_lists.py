import json, ast
import csv
import sys
from random import randint
from pprint import pprint

prob_bands = '/home/uwhpsc/wdocs/pytrends/bands2588_lab/problem_list.csv'
mytext0 = open(prob_bands, 'r')
line = mytext0.readlines()

probband_list = []
for ind in range(522):
	band_index = ast.literal_eval(line[ind])[1][0]
	probband_list = probband_list + [band_index]
print(probband_list)

stop_bands = '/home/uwhpsc/wdocs/pytrends/bands2588_lab/stopped_list.csv'
mytext = open(stop_bands, 'r')
lines = mytext.readlines()

for ind in range(14):
	band_index = ast.literal_eval(lines[ind])[1][0]
	probband_list = probband_list + [band_index]
print(probband_list)

f = open('/home/uwhpsc/wdocs/pytrends/bands2588_lab/export_list.csv', "w")
mydoc = csv.writer(f, lineterminator='\n')
mydoc.writerow(probband_list)
f.close()
