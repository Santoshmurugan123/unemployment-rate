#!/usr/bin/env python
# coding: utf-8

# # importing packages

# In[ ]:


import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


# # reading csv

# In[3]:


data = pd.read_csv("C:\\Users\\SANTH\\OneDrive\\Documents\\Unemployment_Rate_upto_11_2020.csv")
print(data)


# # unemployment rate depends on the region

# In[4]:


data.columns= ["States","Date","Frequency",
               "Estimated Unemployment Rate",
               "Estimated Employed",
               "Estimated Labour Participation Rate",
               "Region","longitude","latitude"]
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Employed", hue="Region", data=data)
plt.show()


# # by using sunburst

# In[5]:


unemploment = data[["States", "Region", "Estimated Unemployment Rate"]]
figure = px.sunburst(unemploment, path=["Region", "States"], 
                     values="Estimated Unemployment Rate", 
                     width=700, height=700, color_continuous_scale="RdY1Gn", 
                     title="Unemployment Rate in India")
figure.show()


# In[ ]:





# In[ ]:




