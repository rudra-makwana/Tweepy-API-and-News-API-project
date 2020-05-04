from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import pandas as pd
import re
import csv
import tweepy

#keys and tokens required for accessing tweepy API
consumerKey = "TaCKN579SHEtOJFSoFyNTChCa"
consumerSecKey = "AwQkIc5OcMVeDZtDoR4WHEfhWZKAzskpGtmnd7M9jvNibuuO0P"
accessToken = "3190728600-DynDLFi0xltlQPQpdd16rZyLYPuKjZZ70scu1ql"
accessSecToken = "G77ncPEdowqRr5tHdgHzS1AFwRYDoa9ClCrbluFvXhd5y"

authentication = tweepy.OAuthHandler(consumerKey, consumerSecKey)
authentication.set_access_token(accessToken, accessSecToken)
api = tweepy.API(authentication,wait_on_rate_limit="true")

#following function will clean the twitter text by reoving emojis and websites from the text
def cleaning(inputString):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               "]+",flags=re.UNICODE)
    inputString = emoji_pattern.sub(r'',inputString)
    inputString = re.sub(r'http\S+', '', inputString)
    inputString = re.sub('[^A-Za-z0-9]+',' ', inputString)
    return inputString

#The following keywords will be searched on twitter
query = ["Canada","University","Halifax","Canada Education","Dalhousie University"]
language = "en"
dataSets = []
for q in query:
    for tweet in tweepy.Cursor(api.search,
                               q=q,
                               lang=language).items(700):
        dict_ = {"id":tweet.id_str,"createdAt":str(tweet.created_at),"tweetText":cleaning(tweet.text),
                "RTCount":tweet.retweet_count,"favCount":tweet.favorite_count,"location":tweet.user.location}
        
        dataSets.append(dict_)


#Converting to JSON format
data = json.dumps(dataSets)
data = json.loads(data)
with open('twitterData.json','w') as outfile:
    json.dump(data,outfile,indent=4)

#Creating CSV file
csvFile = open('twitterData.csv', 'w')
csvWriter = csv.writer(csvFile)

