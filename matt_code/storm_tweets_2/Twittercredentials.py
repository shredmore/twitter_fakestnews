import tweepy

consumer_key = "gLdJ3EyZeUPdOTRmhLXDYzspD";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "yTt63tz00nhf0aGdtP1d4mgSWZTShJOARWdexk13kHZ4TX2XFu";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "1074739122-lQ6wmQ47cOoAx5AvwXQCVQ5MrfKCjP2PkWJlaZC";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "HZaKOemjLnEKDLS7wTaF8eXMSWE3wPT9A11aTZTlGrWjB";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)




