#learn to scrape web pages
import requests
import csv
import subprocess
from datetime import datetime
from bs4 import BeautifulSoup

#choose page to scrape
#I want to look at one with comments
page = requests.get("https://www.nytimes.com/")

source_id = '002'

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


#get headlines which always follow class="top-story-title"
for i in soup.find_all(class_="story-heading"):
	bel = i.find_all('a')
	for t in bel:
		headlines.append(t.text.strip())

#get last used headline id and add 1
my_file = Path("./nyt.csv")
if my_file.is_file():
	last_line = subprocess.check_output(["tail", "-1", "nyt.csv"])
	last_id = last_line.split(b',')[-1:]
	for i in last_id:
		id = int(i)
	id += 1	
else:
	id = 0

#create list of lists to put into .csv
list_for_csv = []
for headline in headlines:
	place_holder = []
	place_holder.append(datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S'))
	place_holder.append(source_id)
	place_holder.append(headline)
	place_holder.append(id)
	list_for_csv.append(place_holder)
	id += 1

# print(list_for_csv)
#include timestamp, source (numeric code for site) and cleaned up headline (no leading/tailing spaces etc)
with open('nyt.csv', 'a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerows(list_for_csv)