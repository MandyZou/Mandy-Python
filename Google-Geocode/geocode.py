import urllib2, json, urllib,csv
import urlparse
from urllib import urlencode

output = open('Geocode.csv','w')
writer = csv.writer(output, delimiter = ",")

writer.writerow(['Name','Lat','Ing'])

geo_re = []

for line in open("geocode01.csv"):
    geo_columns = line.split(";")
    # print geo_columns[1]

    url = "https://maps.googleapis.com/maps/api/geocode/json?address="+geo_columns[1]+"&key=Your_API_Key"

    geo_page = urllib2.urlopen(url).read()

    geo_detail = json.loads(geo_page)

    geo_re.append(geo_detail)

    for geo_detail in geo_re:

        geo_result = geo_detail['results']

        for geo_detail2 in geo_result:

            geo_geometry = geo_detail2['geometry']

            # print geo_geometry['location']

            latitude = geo_geometry['location']['lat']

            altitude = geo_geometry['location']['lng']

    name = geo_columns[0].replace('+',' ')

    writer.writerow([name, latitude, altitude])
