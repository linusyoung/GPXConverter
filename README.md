# GPXConverter
[![Build Status](https://travis-ci.org/linusyoung/GPXConverter.svg?branch=master)](https://travis-ci.org/linusyoung/GPXConverter)
## How to use

```
$pip install gpxconverter

$gpxconverter -i <input file> -o <output file>

```
*Note: 'csv' extension is not required for output filename.*

[Install pip if necessary](https://pip.pypa.io/en/latest/installing/)

## Output
It will extract waypoints information from input file to a csv file.

Waypoints will be saved as [output file]\_wpt.csv

Route will be saved as [output file]\_rte.csv

## XSD reference documents
GPX XSD is available at the below link.

[http://www.topografix.com/GPX/1/1](http://www.topografix.com/gpx/1/1/gpx.xsd)
