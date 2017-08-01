# count (int, optional):
#             Number of results to return.  Default is 15 and maxmimum that
#             Twitter returns is 100 irrespective of what you type in.


import twitter
import re
from datetime import datetime
import csv

api = twitter.Api(consumer_key='P2jn6plFXmwOTBH6NSBkWCJPN',
                      consumer_secret='sJ5MvwbwZB5bxoiiOW6eQRpmNzRUnjBgZqMpuEbfgiG3LUz2Kz',
                      access_token_key='2242498214-mp3RRlz2tw1K6W3g0D70ao0ha2p6DmplZp1qYZ8',
                      access_token_secret='feUuZ12xNcx40rLlkJYPPk79k4k87vNfSoSDOUpVvPqD4')

# print(api.VerifyCredentials())

#set query variables (100 is max)
key_word_1 = 'fakenews'
count = '3'

fakenews = api.GetSearch(raw_query="q="+key_word_1+"%20OR%20"+"%23"+key_word_1+"&count="+count)

#create twitter list for table
tweets = []
user = []
hashtags = []
urls = []
mentions = []
place = []
for i in fakenews:
	
	#create temp lists for each tweet that will be appended
	#to master list and then written to .csv
	tweets_temp = []
	user_temp = []
	places_temp = []

	#put twitter status object into dictionary form for pulling
	#desired data more easily
	new_dict = i.AsDict()

	#create variables that several tables will use
	created_at = new_dict['created_at']
	tweet_id = new_dict['id_str']

	#get tweets data
	tweets_temp.append(created_at)
	tweets_temp.append(tweet_id)
	tweets_temp.append(new_dict['user']['name'])
	tweets_temp.append(str(new_dict['user']['id']))
	tweets_temp.append(new_dict['text'])
	tweets_temp.append(new_dict['lang'])
	source = re.match(r"^.*>(.*)<.*$",new_dict['source'])
	tweets_temp.append(source.group(1))
	try:
		tweets_temp.append(new_dict['coordinates'][0])
		tweets_temp.append(new_dict['coordinates'][1])
	except KeyError:
		tweets_temp.append(None)
		tweets_temp.append(None)
	tweets.append(tweets_temp)

	#get hashtag data
	try:
		for tag in new_dict['hashtags']:
			hashtags_temp =[]
			hashtags_temp.append(created_at)
			hashtags_temp.append(tweet_id)
			for i in tag:
				hashtags_temp.append(i)
				hashtags_temp.append(tag[i])
			hashtags.append(hashtags_temp)
	except KeyError:
		hashtags_temp = []
		hashtags_temp.append(created_at)
		hashtags_temp.append(tweet_id)
		hashtags_temp.append(None)
		hashtags_temp.append(None)
		hashtags.append(hashtags_temp)

	#get urls
	try:
		for url in new_dict['urls']:
			urls_temp =[]
			urls_temp.append(created_at)
			urls_temp.append(tweet_id)
			for i in url:
				urls_temp.append(i)
				urls_temp.append(url[i])
			urls.append(urls_temp)
	except KeyError:
		urls_temp = []
		urls_temp.append(created_at)
		urls_temp.append(tweet_id)
		urls_temp.append(None)
		urls_temp.append(None)
		urls.append(urls_temp)

	#get mentions
	try:
		for mention in new_dict['user_mentions']:
			mentions_temp =[]
			mentions_temp.append(created_at)
			mentions_temp.append(tweet_id)
			for i in mention:
				mentions_temp.append(mention[i])
			mentions.append(mentions_temp)
	except KeyError:
		mentions_temp = []
		mentions_temp.append(created_at)
		mentions_temp.append(tweet_id)
		mentions_temp.append(None)
		mentions_temp.append(None)
		mentions_temp.append(None)
		mentions.append(mentions_temp)

	#get place data
	places_temp.append(created_at)
	places_temp.append(tweet_id)
	try:
		places_temp.append(new_dict['places']['country'])
	except KeyError:
		places_temp.append(None)
	try:
		places_temp.append(new_dict['places']['country_code'])
	except KeyError:
		places_temp.append(None)
	try:
		places_temp.append(new_dict['places']['full_name'])
	except KeyError:
		places_temp.append(None)
	try:
		places_temp.append(new_dict['places']['id'])
	except KeyError:
		places_temp.append(None)
	try:
		places_temp.append(new_dict['places']['name'])
	except KeyError:
		places_temp.append(None)
	try:
		places_temp.append(new_dict['places']['place_type'])
	except KeyError:
		places_temp.append(None)
	try:
		places_temp.append(new_dict['places']['url'])
	except KeyError:
		places_temp.append(None)

	place.append(places_temp)


	#get user data
	user_temp.append(new_dict['user']['created_at'])
	user_temp.append(str(new_dict['user']['id']))
	user_temp.append(new_dict['user']['name'])
	user_temp.append(new_dict['user']['screen_name'])
	try:
		user_temp.append(new_dict['user']['verified'])
	except KeyError:
		user_temp.append('false')
	try:
		user_temp.append(new_dict['user']['description'])
	except KeyError:
		user_temp.append(None)
	try:
		user_temp.append(new_dict['user']['url'])
	except KeyError:
		user_temp.append(None)
	try:
		user_temp.append(new_dict['user']['location'])
	except KeyError:
		user_temp.append(None)
	try:	
		user_temp.append(new_dict['user']['time_zone'])
	except KeyError:
		user_temp.append(None)
	try:
		user_temp.append(new_dict['user']['statuses_count'])
	except KeyError:
		user_temp.append(0)
	try:
		user_temp.append(new_dict['user']['followers_count'])
	except KeyError:
		user_temp.append(0)
	try:
		user_temp.append(new_dict['user']['friends_count'])
	except KeyError:
		user_temp.append(0)
	try:
		user_temp.append(new_dict['user']['listed_count'])
	except KeyError:
		user_temp.append(0)
	try:
		user_temp.append(new_dict['user']['geo_enabled'])
	except KeyError:
		user_temp.append('false')
	try:
		user_temp.append(new_dict['user']['lang'])
	except KeyError:
		user_temp.append(None)
	try:
		user_temp.append(new_dict['user']['favourites_count'])
	except KeyError:
		user_temp.append(0)
	try:
		user_temp.append(new_dict['user']['default_profile_image'])
	except KeyError:
		user_temp.append(None)
	try:
		user_temp.append(new_dict['user']['withheld_in_countries'])
	except KeyError:
		user_temp.append(None)
	try:
		user_temp.append(new_dict['user']['withheld_scope'])
	except KeyError:
		user_temp.append(None)

	user.append(user_temp)

# print(tweets)
# print(user)
# print(hashtags)
# print(urls)
# print(mentions)
# print(place)

file_name_twt = 'tweets_' + datetime.today().strftime('%Y-%m-%d_%H-%M-%S') + '.csv'
file_name_usr = 'users_' + datetime.today().strftime('%Y-%m-%d_%H-%M-%S') + '.csv'
file_name_hsh = 'hashtags_' + datetime.today().strftime('%Y-%m-%d_%H-%M-%S') + '.csv'
file_name_url = 'urls_' + datetime.today().strftime('%Y-%m-%d_%H-%M-%S') + '.csv'
file_name_mnt = 'mentions_' + datetime.today().strftime('%Y-%m-%d_%H-%M-%S') + '.csv'
file_name_plc = 'places_' + datetime.today().strftime('%Y-%m-%d_%H-%M-%S') + '.csv'


with open(file_name_twt, 'w', newline='') as csvfile:
    tweetwriter = csv.writer(csvfile)
    tweetwriter.writerows(tweets)

with open(file_name_usr, 'w', newline='') as csvfile:
    tweetwriter = csv.writer(csvfile)
    tweetwriter.writerows(user)

with open(file_name_hsh, 'w', newline='') as csvfile:
    tweetwriter = csv.writer(csvfile)
    tweetwriter.writerows(hashtags)

with open(file_name_url, 'w', newline='') as csvfile:
    tweetwriter = csv.writer(csvfile)
    tweetwriter.writerows(urls)

with open(file_name_mnt, 'w', newline='') as csvfile:
    tweetwriter = csv.writer(csvfile)
    tweetwriter.writerows(mentions)

with open(file_name_plc, 'w', newline='') as csvfile:
    tweetwriter = csv.writer(csvfile)
    tweetwriter.writerows(place)


######
#Example of pull with kohls as keyword


#create model from reulsts and interate
# for i in kohls:
# 	new_dict = i.AsDict()
# 	for j in new_dict:
# 		print(j)
# created_at - "created_at": "Sat Jul 29 18:39:26 +0000 2017"
# hashtags - "hashtags": [{"text": "job"}, {"text": "Retail"}, {"text": "Jeff"}, {"text": "Hiring"}]
# id - (unique tweet int) "id": 891367580660678656 The integer representation of the unique identifier for this Tweet. This number is greater than 53 bits and some programming languages may have difficulty/silent defects in interpreting it. Using a signed 64 bit integer for storing this identifier is safe. Use id_str for fetching the identifier to stay on the safe side. See Twitter IDs, JSON and Snowflake . Example:
# id_str - (string/safer version of id) , "id_str": "891367580660678656"
# lang - "lang": "en" idetifies language
# source - how tweet was posted (will be web for twitter website) "source": "<a href=\"http://www.tweetmyjobs.com\" rel=\"nofollow\">TweetMyJOBS</a>"
# text - UTF-8 text of tweet ; "text": "Join the Kohl's Corporation team! See our latest #job opening here: https://t.co/0BAAMibE0I #Retail #Jeff, IN #Hiring"	
	# - may want to check if can use https://github.com/twitter/twitter-text/blob/master/rb/lib/twitter-text/regex.rb to parse tweets for valid chars
# urls - urls in tweet text "urls": [{"expanded_url": "http://bit.ly/2oOB6oR", "url": "https://t.co/0BAAMibE0I"}]
# user - dict of user attributes/profile info
	# "user": {"created_at": "Fri Apr 03 13:06:40 +0000 2009",
	# "description": "Follow this account for geo-targeted Retail job tweets in Louisville, KY. Need help? Tweet us at @CareerArc!",
	# "followers_count": 401, "friends_count": 308, "geo_enabled": true, "id": 28557854, "lang": "en",
	# "listed_count": 101, "location": "Louisville, KY", "name": "TMJ-SDF Retail Jobs",
	# "profile_background_color": "253956", "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/315483274/Twitter-BG_2_bg-image.jpg",
	# "profile_banner_url": "https://pbs.twimg.com/profile_banners/28557854/1448455299",
	# "profile_image_url": "http://pbs.twimg.com/profile_images/669496158457237504/B2UphjKF_normal.jpg",
	# "profile_link_color": "4A913C", "profile_sidebar_fill_color": "407DB0", "profile_text_color": "000000",
	# "screen_name": "tmj_sdf_retail", "statuses_count": 212, "time_zone": "Eastern Time (US & Canada)",
	# "url": "https://t.co/DByWt45HZj", "utc_offset": -14400}
# user_mentions - other users mentioned  "user_mentions": [{"id": 181989393, "name": "Coralie - LBPC", "screen_name": "CoralieSeright"}, {"id": 263317217, "name": "Hartz", "screen_name": "HartzPets"}]}
# coordinates (long,lat) - location "coordinates": {"coordinates": [-85.6948458, 38.3325704]
	# - check "place" (associated place of tweet but not necessarily origin) dictionary too
	# place": {"attributes": {}, "bounding_box": {"coordinates": [[[-85.7574498, 38.2675375], [-85.638925, 38.2675375], [-85.638925, 38.402733], [-85.7574498, 38.402733]]], "type": "Polygon"},
	# "contained_within": [],
	# "country": "United States",
	# "country_code": "US",
	# "full_name": "Jeffersonville, IN",
	# "id": "6c0e077597395926",
	# "name": "Jeffersonville",
	# "place_type": "city",
	# "url": "https://api.twitter.com/1.1/geo/id/6c0e077597395926.json"}
	# - geo is depricated!!
