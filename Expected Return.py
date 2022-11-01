#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("Realty_Income_Price.csv")


# In[3]:


def getExpectedReturn(df, price_col_name, annualized=True, annualize_method='sophisticated'):
    """
    Returns the expected return of a stock given price data
    """
    
    # Calculate returns of price
    returns = df[price_col_name].pct_change(1)
    
    #Calculate the expected return using the mean method
    expected_return_daily = returns.mean()
    
    if annualized:
        if annualize_method == 'sophisticated':
            expected_return_annual = ((1 + expected_return_daily) ** 250) - 1
        elif annualize_method == 'crude':
            # Crude Method
            expected_return_annual = expected_return_daily * 250
            
        return expected_return_annual
    
    else:
        return expected_return_daily


# In[4]:


data.head()


# In[5]:


# Annualized Expected Return (sophisticated method)
getExpectedReturn(data, 'Close')


# In[6]:


# Daily expected return
getExpectedReturn(data, 'Close', annualized=False)


# In[7]:


# Annualized Expected Return (Crude Method)
getExpectedReturn(data, 'Close', annualize_method='crude')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[8]:


sp500 = pd.read_csv('sp500_price.csv')


# In[9]:


sp500.head()


# In[10]:


getExpectedReturn(df=sp500, price_col_name='sp500')


# In[11]:


getExpectedReturn(df=sp500, price_col_name='sp500', annualize_method='crude')


# In[ ]:




