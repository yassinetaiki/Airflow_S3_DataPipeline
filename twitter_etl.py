import tweepy
import pandas as pd
import numpy as np 
import s3fs



def connexion(name_user,count_tweet,tweet_modee):
    access_key="BxdnU4IHl1zSnAsxeeSmLyfLJ"
    access_secret="xO9vmAhcKg5FTc48bBild8C9vWbjxz7wQfdK0RIU8OxKUOk6gE"
    consumer_key="1651889006857125890-HWohI4IwN77ypkW0qLX2ChHrsCaLbR"
    consumer_secret= "5KFBNJwKl4lzaPV7kqpKblaGF77OObXF95Qd4iP632BCP"

    #twitter authentification
    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key,consumer_secret)

    #create object 
    api = tweepy.API(auth)

    try:
        # If the authentication was successful, this should print the
        # screen name / username of the account
        print(api.verify_credentials().screen_name)
    except Exception as e:
        print("Authentication failed: ", e)
    

    tweets = api.user_timeline(screen_name=name_user, 
                            # 200 is the maximum allowed count
                            count=count_tweet,
                            include_rts = False,
                            # Necessary to keep full_text 
                            # otherwise only the first 140 words are extracted
                            tweet_mode = tweet_modee
                            )
    return tweets


def run_etl():
    list_tweet=[]
    tweets=connexion('@elonmusk',200,'extended')
    for tweet in tweets:
        tweet_redefinie={
            'user':tweet.user.screen_name,
            'local':tweet.user.location,
            'text':tweet._json['full_text'],
            'retweet_count':tweet.retweet_count,
            'favorite_count':tweet.favorite_count,
            'created_at':tweet.created_at,

            }
        list_tweet.append(tweet_redefinie)

    data_tweet=pd.DataFrame(list_tweet)
    data_tweet.to_csv("list_tweet_musk_2.csv")
    #data_tweet.to_csv("s3://taiki-airflow-twitter-bucket/list_tweet_musk.csv")

run_etl()
        