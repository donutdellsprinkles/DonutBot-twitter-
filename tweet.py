import tweepy
import keys
import schedule
import time

# Download the libraries first
#beware, twitter's api thing is a whole mess. You will most likely to have subscribe to one of 
# their tiers to actually get this to work as you will most likely encounter a Forbidden error


def create_api():
    auth = tweepy.OAuthHandler("API_KEY", 
    "API_SECRET")
    auth.set_access_token("ACCESS_TOKEN",
                      "ACCESS_TOKEN_SECRET")

    return tweepy.API(auth)


def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        media = api.media_upload(image_path)
        api.update_status(message, media_ids=[media.media_id])
    else:
        api.update_status(message)

    print('Tweeted!')


if __name__ == '__main__':
    api = create_api()
    tweet(api, 'This is not a donut', 'cat.png')

schedule.every().hour.do(tweet)
schedule.every().hour.do(create_api)

while True:
    schedule.run_pending()
    time.sleep(1)
#this will allow you to tweet with your bot every hour. Haven't really tested it