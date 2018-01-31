from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import sys

locations = ["Half-Moon-Bay-California", "Huntington-Beach", "Providence-Rhode-Island", "Wrightsville-Beach-North-Carolina"]
state = 0
data = []
outfile = "results.csv"

for location in locations:
	url = "https://www.tide-forecast.com/locations/{}/tides/latest".format(location)
	site = urlopen(url)
	dataIn = BeautifulSoup(site, "html.parser")
	
	for ele in dataIn.find_all('td'):
		if ele.get_text() == 'Sunrise':
			state = 1
		if ele.get_text() == 'Sunset':
			state = 0
		if state == 1:
			if ele.get_text() == "Low Tide":
				time = ele.parent.find_all("td", class_="time")[0].get_text()
				zone = ele.parent.find_all("td", class_="time-zone")[0].get_text()
				level = ele.parent.find_all("td", class_="level metric")[0].get_text()
				data.append((location, '{} {}'.format(time, zone), level))

with open(outfile, 'wt') as f:
	out=csv.writer(f)
	out.writerow(['location','time', 'level'])
	for row in data:
		out.writerow(row)

print(data)
