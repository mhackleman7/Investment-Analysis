#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy.stats import linregress


# In[2]:


df = pd.read_csv("googl_sp500_price.csv")


# In[3]:


df.head()


# In[4]:


df.set_index('date_gsheets', inplace=True)


# In[5]:


df.head()


# In[6]:


returns_df = df.pct_change(1)


# In[7]:


returns_df.head()


# In[8]:


returns_df.dropna(inplace=True)


# In[9]:


returns_df.head()


# In[10]:


new_col_names = ['r_googl', 'r_sp500']
returns_df.columns = new_col_names


# In[11]:


returns_df.head()


# In[12]:


deviations = returns_df - returns_df.mean()


# In[13]:


deviations.head()


# In[14]:


returns_df['r_googl'].iloc[0] - returns_df['r_googl'].mean()


# In[15]:


new_col_names =['deviations_googl' , 'deviations_sp500']
deviations.columns = new_col_names


# In[16]:


deviations.head()


# In[17]:


product_deviations = deviations['deviations_googl'] * deviations['deviations_sp500']


# In[18]:


product_deviations.head()


# In[19]:


type(product_deviations)


# In[20]:


type(deviations)


# In[21]:


cov_googl_sp500 = product_deviations.sum() / (len(product_deviations) - 1)


# In[22]:


cov_googl_sp500


# In[23]:


var_sp500 = np.var(returns_df['r_sp500'], ddof=1)


# In[24]:


var_sp500


# In[25]:


beta_googl = cov_googl_sp500 / var_sp500


# In[26]:


beta_googl


# In[27]:


np.cov(returns_df['r_sp500'], returns_df['r_googl'])[0][1]


# In[28]:


linregress(y=returns_df['r_googl'], x=returns_df['r_sp500'])


# In[ ]:




