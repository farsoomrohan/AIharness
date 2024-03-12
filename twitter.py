import tweepy
import json

#Get all these authorizations from the twitter developer account
api_key = 'YOUR_API_KEY'
api_key_secret = 'YOUR_API_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#This is what we need to work on. figure out what search words and dates.
search_words = "#examplehashtag"
date_since = "2021-01-01"


tweets = tweepy.Cursor(api.search_tweets,
              q=search_words,
              lang="en",
              since=date_since).items(5)

tweets_data = []
for tweet in tweets:
    tweets_data.append(tweet._json)  

with open('tweets.json', 'w') as outfile:
    json.dump(tweets_data, outfile, indent=4)

print("Tweets have been saved to tweets.json")
