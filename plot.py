#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import datetime
import numpy as np


# In[3]:


tweets = pd.read_csv('derived_data/trump_sentiment.csv', index_col = False)
tweets = tweets.drop(columns = ['Unnamed: 0','likes','rts'], axis = 1)


# In[4]:


tweets


# In[ ]:


n = pd.Series(tweets.tail(1).iloc[0]).copy(deep=True)
f = pd.Series(tweets.tail(1).iloc[0]).copy(deep=True)
tweet_plot = pd.DataFrame(columns = ['date','text', 'polarity', 'subjectivity'])
for index, row in tweets.iterrows(): 
    m = row
    if m['date'] == n['date']:
        if (pd.notnull(m['text']) and m['text'] != 'rt'):
            i += 1
        n['polarity'] = n['polarity'] + m['polarity']
        n['subjectivity'] = n['subjectivity'] + m['subjectivity']
    else: 
        if f['date'] != n['date']:
            n['polarity'] = n['polarity']/(i)
            n['subjectivity'] = n['subjectivity']/(i)
            tweet_plot = tweet_plot.append(n, ignore_index=True)         
        n = m
        i = 1
        


# In[6]:


tweet_plot


# In[7]:

import matplotlib.pyplot as plt


# In[9]:


tpol = pd.Series(data=tweet_plot['polarity'].values, index=tweet_plot['date'])
tsub = pd.Series(data=tweet_plot['subjectivity'].values, index=tweet_plot['date'])
tpol.plot(figsize=(16,4), label="Polarity", legend=True)
tsub.plot(figsize=(16,4), label="Subjectivity", legend=True);
plt.savefig('image/sentiment.png')

# In[ ]:




