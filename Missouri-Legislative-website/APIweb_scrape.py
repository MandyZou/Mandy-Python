import urllib2, json, urllib,csv, mechanize, requests, ast
import urlparse
from urllib import urlencode
from bs4 import BeautifulSoup
import time
from datetime import datetime
import os

output = open('BillChangew.csv','w')
writer = csv.writer(output)

writer.writerow(['bill_id','bill_title','date','action'])

# Type today's time in the format of "yyyy-mm-dd 00:00:00"
today_time = "2016-05-09 00:00:00"

br = mechanize.Browser()

# output = open('ApiList.csv','w')
# writer = csv.writer(output, delimiter = ",")

# writer.writerow(['bill_id','primary sponsor','bill_title'])


response = urllib2.urlopen('http://openstates.org/api/v1/bills/?apikey=1f366e0712bd4ad6b079afe3bb993434&state=mo&search_window=session').read()

bills = json.loads(response)


# Set up a list, in order to put all Json code into a list (after read each bill_detail page)
bill_re = []

# Set up another list to save the final result
bill_final = []

for bill in bills:

    # This is the processing piece I mentioned in the assignment description. To include
    # a bill ID (which has spaces in it)through a URL in Python, you need to do this first.
    encoded_bill_id = urllib.quote(bill['bill_id'])

    # Put a list of bill id into url
    url = 'http://openstates.org/api/v1/bills/mo/2016/'+encoded_bill_id+'/?apikey=1f366e0712bd4ad6b079afe3bb993434'

    # Read each bill_detail page
    bill_page = urllib2.urlopen(url).read()

    bill_detail = json.loads(bill_page)

    bill_re.append(bill_detail)

    
    # Get sponsor, title, id from each page
    for bill_detail in bill_re:

        bill_actions = bill_detail['actions']

        last_one = bill_actions[-1]

    # print last_one

        # Get rid of 'u' in a dict
        bill_action = ast.literal_eval(json.dumps(last_one))

        bill_the_action = bill_action['action']

    # print bill_action
        bill_date = bill_action['date']

        bill_print_id = bill_detail['bill_id'].encode('utf-8')

        bill_print_title = bill_detail['title'].encode('utf-8')

    # print bill_date
    if bill_date == today_time:

        writer.writerow([bill_print_id, bill_print_title, bill_date, bill_the_action])

os.system('say "your program has finished"')


