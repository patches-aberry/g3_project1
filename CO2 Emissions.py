#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Import Dependencies
import pandas as pd


# In[9]:


# Pull in file and create dataframe using Pandas
co2_data = "../g3_project1/CO2_by_countries.csv"
co2_data_df = pd.read_csv(co2_data, encoding="ISO-8859-1")
co2_data_df


# In[ ]:




