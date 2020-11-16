#!/usr/bin/env python
# coding: utf-8

# In[122]:


import tweepy           # To consume Twitter's API
import pandas as pd     # To handle data
import numpy as np
import re

key = pd.read_csv('key.csv',index_col=0)


# In[123]:


#get the authentiation key
auth = tweepy.OAuthHandler(key['value']['API key'], key['value']['API key secret'])
auth.set_access_token(key['value']['Access token'], key['value']['Access token secret'])
api = tweepy.API(auth, wait_on_rate_limit = True)


# In[124]:


#get Trump's tweets
#tweets = api.user_timeline(screen_name="realDonaldTrump", count=20000, include_rts=False)
tweets = tweepy.Cursor(api.user_timeline,screen_name="realDonaldTrump", count=6000, lang='en', tweet_mode='extended')


# In[125]:


def clean_tweet(tweet):
    return ' '.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', ' ', tweet).split())


# In[126]:


data = pd.DataFrame()
i=0
for tweet in tweets.items():

    tweet_details = {}
    tweet_details['date'] = tweet.created_at.strftime("%d-%b-%Y")
    tweet_details['text']= clean_tweet(tweet.full_text).lower()
    tweet_details['likes'] = tweet.favorite_count
    tweet_details['rts'] = tweet.retweet_count
    
    i+=1
      

    data = data.append(pd.Series(tweet_details), ignore_index=True)
    if i>= 6000:
        break
print(data)


# In[127]:


display(data.head(10))


# In[128]:


#Filter the time 
#tweet = tweet[tweet['date'] >= '2020-02-01']


# In[129]:


from textblob import TextBlob


# In[130]:


data['polarity'] = 0
data['subjectivity'] = 0


# In[131]:


for index, row in data.iterrows():
    ts = TextBlob(row['text']).sentiment
    data.loc[index, 'polarity'] = ts.polarity
    data.loc[index, 'subjectivity'] = ts.subjectivity


# In[132]:


data


# In[134]:


data.to_csv('derived_data/trump_sentiment.csv')


# In[ ]:




