#initial checkpoints:
#ask for date
#ask for location
#ask for magnitude
#have a paragraph ready
import tweepy
from termcolor import colored
import tkinter as tk
consumer_key = " "
consumer_secret = " "
access_token = " "
access_token_secret = " "

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
    tweet = api.update_status("Hey, this is Sakardharan with an earthquake forecast. I predict that on %s an earthquake of %s will occur at %s. These are just predictions, but, prevention is better than cure :D " % (e1.get(), e3.get(),e2.get())) #sakardharan is just a random name :D
    print('tweet has been tweeted')

master = tk.Tk()
tk.Label(master, 
         text="DATE दिनांक").grid(row=0, column=0 )
tk.Label(master, 
         text="LOCATION स्थान").grid(row=1)
tk.Label(master, 
         text="MAGNITUDE परिमाण").grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Show', command=main).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()




    

# class credentials():
#     date=(input('PLEASE ENTER THE DATE कृपया तारीख लिखें: '))
#     location=(input('PLEASE ENTER THE LOCATION कृपया स्थान लिखें: '))
#     magnitude=(input('PLEASE ENTER THE MAGNITUDE कृपया परिमाण लिखिए: '))

# credentials()

