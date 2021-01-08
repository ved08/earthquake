import flask
from flask import Flask, render_template, request
import tweepy

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html') 


@app.route('/getvalue', methods=['POST'])
def getvalue():
    api = authenticate_api()
    Name = request.form['yourName']

    EnterpriseId = request.form['enterpriseId']

    Servers = request.form['server']
    tweet = api.update_status("Hey, this is Sakardharan with an earthquake forecast. I predict that on %s an earthquake of %s will occur at %s. These are just predictions, but, prevention is better than cure :D " % (Name, EnterpriseId,Servers)) #sakardharan is just a random name :D
    print('tweet has been tweeted')
    return render_template('index.html', n=Name, eId=EnterpriseId, sName=Servers)   

#initial checkpoints:
#ask for date
#ask for location
#ask for magnitude
#have a paragraph ready


if __name__ == '__main__':
    app.run(debug=True)
    