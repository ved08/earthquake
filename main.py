#initial checkpoints:
#ask for date
#ask for location
#ask for magnitude
#have a paragraph ready
import tweepy
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


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
    tweet = api.update_status(f"Hey, this is Sakardharan with an earthquake forecast. I predict that on '{credentials.date}' an earthquake of '{credentials.magnitude}' will occur at '{credentials.location}'. These are just predictions, but, prevention is better than cure :D ") #sakardharan is just a random name :D
    print('tweet has been tweeted')

class credentials():
    date=(input('PLEASE ENTER THE DATE कृपया तारीख लिखें: '))
    location=(input('PLEASE ENTER THE LOCATION कृपया स्थान लिखें: '))
    magnitude=(input('PLEASE ENTER THE MAGNITUDE कृपया परिमाण लिखिए: '))

credentials()
main ()
