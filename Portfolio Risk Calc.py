#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('10stocks_price.csv')


# In[3]:


df.head()


# In[4]:


type(df['date_gsheets'][0])


# In[5]:


df['date_gsheets'] = pd.to_datetime(df['date_gsheets'])


# In[6]:


df['date_gsheets'].describe()


# In[7]:


df.describe()


# In[8]:


df.info()


# In[9]:


df.set_index('date_gsheets', inplace=True)


# In[10]:


df.head()


# In[11]:


returns_df = df.pct_change(1)


# In[12]:


returns_df


# In[13]:


num_stocks = 10
weights = [1 / num_stocks] * num_stocks


# In[14]:


weights


# In[15]:


vcv_matrix = returns_df.cov()


# In[16]:


vcv_matrix


# In[17]:


var_p = np.dot(np.transpose(weights), np.dot(vcv_matrix, weights))


# In[18]:


var_p


# In[19]:


sd_p = np.sqrt(var_p)


# In[20]:


sd_p


# In[21]:


sd_p_annual = sd_p * np.sqrt(250)


# In[22]:


sd_p_annual


# In[23]:


individual_risks = np.std(returns_df) * np.sqrt(250)


# In[24]:


individual_risks


# In[ ]:




