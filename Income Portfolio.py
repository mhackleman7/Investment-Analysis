#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import numpy as np


# In[22]:


df = pd.read_csv('Income Portfolio.csv')


# In[23]:


df.head()


# In[24]:


type(df['Date'][0])


# In[25]:


df['Date'] = pd.to_datetime(df['Date'])


# In[26]:


type(df['Date'][0])


# In[27]:


df.set_index('Date', inplace=True)


# In[28]:


returns_df = df.pct_change(1)


# In[29]:


returns_df


# In[36]:


num_stocks = 4
weights = [1 / num_stocks] * num_stocks


# In[37]:


weights


# In[38]:


vcv_matrix = returns_df.cov()


# In[39]:


vcv_matrix


# In[40]:


var_p = np.dot(np.transpose(weights), np.dot(vcv_matrix, weights))


# In[41]:


var_p


# In[42]:


sd_p = np.sqrt(var_p)


# In[43]:


sd_p


# In[44]:


sd_p_annual = sd_p * np.sqrt(250)


# In[46]:


sd_p_annual


# In[47]:


individual_risks = np.std(returns_df) * np.sqrt(250)


# In[48]:


individual_risks


# In[ ]:





# In[ ]:





# In[ ]:




