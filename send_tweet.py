# importing the module 
import tweepy 

import keys_and_tokens

consumer_key = keys_and_tokens.consumer_key
consumer_secret = keys_and_tokens.consumer_secret
access_token = keys_and_tokens.access_token
access_token_secret = keys_and_tokens.access_token_secret
  
# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 
  
# update the status 
api.update_status(status ="") 

