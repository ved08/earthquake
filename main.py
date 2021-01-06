#initial checkpoints:
#ask for date
#ask for location
#ask for magnitude
#have a paragraph ready
import tweepy
consumer_key = "Uwl6smMGgoC5vYU7cPfU1pOU9"
consumer_secret = "ppyuSbRGI18bNZKAfUTpn3mEXtvyOFHn3Y1DK50LQ0m7oHLtHk"
access_token = "1116939101717127168-g3lqWNUGMg9iBpAEPBuSVVdVlPcXOc"
access_token_secret = "rY184j72O2fgPVanfsiVnllfW66mJIqoj7jx1qix9glFI"


def authenticate_api():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return tweepy.API(auth)
    except Exception as error:
        print(f"An error occurred when attempting to authenticate with the twitter API. reason: {error}")


def main():
    api = authenticate_api()
    # Post tweet
    tweet = api.update_status(f"Hey, this is Sakardharan with an earthquake forecast. I predict that on {credentials.date} an earthquake of {credentials.magnitude} will occur at {credentials.location}. These are just predictions, but, prevention is better than cure :D ") #sankardharan is just a random name
    print('tweet has been tweeted')

class credentials():
    date=(input('PLEASE ENTER THE DATE कृपया तारीख लिखें: '))
    location=(input('PLEASE ENTER THE LOCATION कृपया स्थान लिखें: '))
    magnitude=(input('PLEASE ENTER THE MAGNITUDE कृपया परिमाण लिखिए: '))
credentials()
main ()
