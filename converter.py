#!/usr/bin/python

import os, sys, getopt
import xml.etree.ElementTree as et
import csv
import re

# waypoints tags
# ele, time, magvar, geoidheight, name, cmt, desc, src, link, sym, type, fix, sat, hdop, vdop, pdop, ageofdgpsdata, dgpsid
def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'test.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
		   print 'test.py -i <inputfile> -o <outputfile>'
		   sys.exit()
		elif opt in ("-i", "--ifile"):
		   inputfile = arg
		elif opt in ("-o", "--ofile"):
		   outputfile = arg

	base_path = os.path.dirname(os.path.realpath(__file__))

	xml_file = os.path.join(base_path, inputfile)
	
	if os.path.isfile(xml_file):
		writeOutput(inputfile, xml_file)
	else:
		print inputfile + ' does not exist. please check file name and try again!'
		sys.exit()

def writeOutput(inputfile, xml_file):
	row_count = 0
	ext_index = re.search(r"\.", inputfile[::-1])
	output_csv_file = inputfile[:-(ext_index.start()+1)] +'.csv'
	with open(output_csv_file, 'w') as csv_file:
		fieldnames = ['lat','lon','ele','time','name','sym']
		writer = csv.DictWriter(csv_file, fieldnames)
		writer.writeheader()

		tree = et.parse(xml_file)

		root = tree.getroot()

		for child in root:
			if re.search("wpt", child.tag):
				lat = child.attrib["lat"]
				lon = child.attrib["lon"]
				elements = child.getchildren()
				ele = elements[0].text
				time = elements[1].text
				name = elements[2].text
				sym = elements[3].text
				writer.writerow({'lat':lat, 'lon':lon, 'ele':ele, 'time':time, 'name':name, 'sym':sym})
				row_count = row_count + 1
	print output_csv_file + ' is created with ' + str(row_count) + ' record(s).'
	

if __name__ == "__main__":
	main(sys.argv[1:])