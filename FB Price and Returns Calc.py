#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# In[2]:


df = pd.read_csv("fb_price.csv")


# In[3]:


df.head()


# In[4]:


df = df[['Date', 'Adj Close']]


# In[5]:


df.head()


# In[6]:


df.rename(columns={'Date' : 'date', 'Adj Close' : 'price_t'}, inplace=True)


# In[7]:


df.head()


# In[8]:


df['returns'] = (df['price_t']/df['price_t'].shift(1))-1


# In[9]:


df.head()


# In[10]:


df.set_index('date', inplace=True)


# In[11]:


df.head()


# In[12]:


df['price_t'].plot(figsize=(12,8))


# In[13]:


df['returns'].plot(figsize=(12,8))


# In[14]:


expected_return_fb = df['returns'].mean()


# In[15]:


expected_return_fb


# In[16]:


len(df['returns'].dropna())


# In[17]:


df['expected_return_fb'] = expected_return_fb


# In[18]:


df.head()


# In[19]:


df[['returns', 'expected_return_fb']].plot(figsize=(12,8))


# In[20]:


df.head()


# In[21]:


df['expected_return_ma_30d'] = df['returns'].rolling(30).mean()


# In[22]:


df.head()


# In[23]:


df.iloc[30:61]


# In[24]:


df[['returns', 'expected_return_fb','expected_return_ma_30d']].plot(figsize=(12,8))


# In[25]:


df['expected_return_ma_7d'] = df['returns'].rolling(7).mean()


# In[26]:


df[['returns', 'expected_return_fb','expected_return_ma_30d','expected_return_ma_7d']].plot(figsize=(12,8))


# In[27]:


df.head()


# In[28]:


var_fb = np.var(df['returns'], ddof=1)


# In[29]:


var_fb


# In[30]:


sd_fb = np.sqrt(var_fb)


# In[31]:


sd_fb


# In[32]:


np.std(df['returns'], ddof=1)


# In[33]:


df.head()


# In[34]:


df['deviations'] = df['returns'] - df['returns'].mean()


# In[35]:


df.head()


# In[36]:


df['squared_deviations'] = df['deviations'] ** 2


# In[37]:


df.head()


# In[38]:


sum(df['squared_deviations'].dropna())


# In[39]:


np.sum(df['squared_deviations'])


# In[40]:


sum_squared_deviations = np.sum(df['squared_deviations'])


# In[41]:


var_fb_manual = sum_squared_deviations / (len(df['squared_deviations'].dropna()) - 1)


# In[42]:


var_fb_manual


# In[43]:


var_fb


# In[44]:


np.sqrt(var_fb_manual)


# In[45]:


sd_fb


# In[46]:


sd_fb_annual = sd_fb * np.sqrt(250)


# In[47]:


sd_fb_annual


# In[48]:


(df['returns'].mean()) * 250


# In[49]:


(1 + df['returns'].mean()) ** 250 - 1


# In[ ]:




