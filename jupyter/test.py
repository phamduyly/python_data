#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import matplotlib.pyplot as plt


# In[2]:


path = "Metro_Interstate_Traffic_Volume.csv"
data = pd.read_csv(path)

print(type(data))


# In[3]:


data


# In[4]:


data.shape


# In[5]:


data.ndim


# In[6]:


data.head(3)


# In[7]:


data.tail(10)


# In[9]:


#data.dtypes()


# In[10]:


data['temp'].describe()


# In[11]:


data.describe()


# In[12]:


data.clouds_all.head()


# In[13]:


data.clouds_all.sum()


# In[14]:


data.clouds_all.count()


# In[15]:


data.clouds_all.sum()/data.clouds_all.count()


# In[16]:


data['clouds_all'].describe()


# In[17]:


data['clouds_all'].plot()


# In[18]:


data.to_csv("output_filename.csv", index=False, encoding='utf8')


# In[ ]:




