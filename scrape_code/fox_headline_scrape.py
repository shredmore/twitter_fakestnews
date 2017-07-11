#learn to scrape web pages
import requests
import csv
from datetime import datetime
from bs4 import BeautifulSoup

#choose page to scrape
#I want to look at one with comments
page = requests.get("http://www.foxnews.com/")

source_id = '003'

headlines = []

#check if dl success
#code should be 200
#success
#print(page.status_code)

#look at raw content of page
#doesn't look like it shows actual comment
#just shows that there is a FB comment
# print(page.content)

#parse html
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())

#use li data-vr-contentbox="" for headlines under 'latest news'
#use class="related" for headlines up top
#use class="primary" data-vr-contentbox="" for top headline

#get headlines which always follow class="top-story-title"
for i in soup.find_all(class_="related"):
	bel = i.find_all('a')
	for t in bel:
		headlines.append(t.text.strip())



#create list of lists to put into .csv
list_for_csv = []
for headline in headlines:
	place_holder = []
	place_holder.append(datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S'))
	place_holder.append(source_id)
	place_holder.append(headline)
	list_for_csv.append(place_holder)

# print(list_for_csv)
#include timestamp, source (numeric code for site) and cleaned up headline (no leading/tailing spaces etc)


with open('fox.csv', 'a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerows(list_for_csv)
