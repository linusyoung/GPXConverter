import getopt
import xml.etree.ElementTree as et
import csv
import re
import os
import sys


def convert(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, 'hi:o:', ['ifile=', 'ofile='])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'gpxconvert -i <inputfile> -o <outputfile>'
            print 'for more help information. please visit github site.'
            sys.exit()
        elif opt in ('-i', '--ifile'):
            inputfile = arg
        elif opt in ('-o', '--ofile'):
            outputfile = arg

    base_path = os.getcwd()
    xml_file = os.path.join(base_path, inputfile)
    if os.path.isfile(xml_file):
        __write_output(inputfile, outputfile, xml_file)
    else:
        print(inputfile +
              """ does not exist.Please check file name and try again!""")
        sys.exit()


def __write_output(inputfile, outputfile, xml_file):
    row_count = 0  # count records
    ext_index = re.search(r'\.', inputfile[::-1])

    if outputfile:
        output_csv_file = outputfile + '.csv'
    else:
        output_csv_file = inputfile[: -(ext_index.start() + 1)] + '.csv'

    with open(output_csv_file, 'w') as csv_file:
        fieldnames = ['lat', 'lon']
        tree = et.parse(xml_file)
        root = tree.getroot()
        head_empty = True

        for child in root:
            if re.search('wpt', child.tag):
                values = []
                values.append(child.attrib['lat'])
                values.append(child.attrib['lon'])
                elements = child.getchildren()
                if head_empty:
                    header = __getHeader(elements)
                    fieldnames.extend(header)
                    writer = csv.DictWriter(csv_file, fieldnames)
                    writer.writeheader()
                    head_empty = False
                for element in elements:
                    values.append(element.text)
                row_value = dict(zip(fieldnames, values))
                writer.writerow(row_value)
                row_count += 1

    print(output_csv_file + ' is created with ' +
          str(row_count) + ' record(s).')


def __getHeader(elements):
    header = []
    for element in elements:
        header.append(re.sub(r'^{.*?}', '', element.tag))
    return header