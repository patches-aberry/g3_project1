#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Import Dependencies
import pandas as pd


# In[9]:


# Pull in file and create dataframe using Pandas
energy_data = "../g3_project1/EnergyJV.csv"
energy_data_df = pd.read_csv(energy_data)
energy_data_df


# In[ ]:


# Create new dataframe including information with dates 

