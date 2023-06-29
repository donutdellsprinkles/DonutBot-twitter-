# use this script to confirm if your access tokens and your api keys are working properly. If they are then authentication should work.

import tweepy

auth = tweepy.OAuthHandler("API_KEY", 
    "API_SECRET")
auth.set_access_token("ACCESS_TOKEN",
                      "ACCESS_TOKEN_SECRET")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Works")
except:
    print("Authentication not working")