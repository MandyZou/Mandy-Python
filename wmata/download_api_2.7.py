import urllib
import urllib2, mechanize
import requests
import shutil
import os
import bz2
from bs4 import BeautifulSoup

def unique(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def download_file(url, file_name):
    # http://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3
    # with urllib2.urlopen(url) as response, open(file_name, 'wb') as out_file:
    #     shutil.copyfileobj(response, out_file)    
    with open(file_name,'wb') as f:
        f.write(urllib2.urlopen(url).read())
        f.close()

download_dir = "data/"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

br = mechanize.Browser()
br.open('http://files.pushshift.io/wmata/')
html = br.response().read()

url = "http://files.pushshift.io/wmata/"

soup = BeautifulSoup(html, 'html.parser')
train_anchors = soup.find_all('a', href=lambda x: 'trains' in x)
train_links = [link['href'][2:] for link in train_anchors]
train_links = unique(train_links)

# check if file is already saved
files = set(os.listdir(download_dir))
train_links = [link for link in train_links if link not in files]

# and then download the files
for file_name in train_links:
    link = url + file_name
    save_as = download_dir + file_name
    print("downloading {}".format(file_name))
    download_file(link, save_as)