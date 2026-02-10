#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df=pd.read_csv("https://raw.githubusercontent.com/freeCodeCamp/boilerplate-demographic-data-analyzer/refs/heads/main/adult.data.csv")


# How many people of each race are represented in this dataset
# 
# 

# In[4]:


race=df["race"].value_counts()


# In[5]:


print(race)


# What is the Average of age of men`

# In[6]:


Average_age=round(df[df["sex"]=="Male"]["age"].mean(),1)


# In[7]:


print(Average_age)


# What is the percentage ofpeople who have a bachelors degree

# In[8]:


Bachelors=round((df["education"]=="Bachelors").mean()*100,1)


# In[9]:


print(Bachelors)


# What percentage of people with advanced Education(Bachelors, Masters or Doctrade) Make more than 50K

# In[25]:


Advanced= round((df[df["education"].isin(["Bachelors","Masters","Doctorate"])]["salary"]==">50K").mean()*100,1)


# In[26]:


print(Advanced)


# What percentage of people without advanced education make more than 50K

# In[31]:


lower=round((df[~df["education"].isin(["Bachelors","Masters","Doctorate"])]["salary"]==">50K").mean()*100,1)


# In[32]:


print(lower)


# What is the minimum number of hours a person works per week

# In[10]:


minimum=df["hours-per-week"].min()


# In[11]:


print(minimum)


# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K 

# In[15]:


rich=(df[df["hours-per-week"]==minimum]["salary"]==">50K").mean()*100


# In[16]:


print(rich)


# What country has the highest percentage of people that earn > 50K and what is the percentage

# In[62]:


country=(df["salary"]==">50K").mean()*100


# In[63]:


print(country)


# In[76]:


country_percentage=df.groupby("native-country")["salary"].apply(lambda x : (x==">50K").mean()*100)

top_country=country_percentage.idxmax()
top_percentage= country_percentage.max()
print(top_country)
print(round(top_percentage,1))


# In[ ]:





# Identify the most popular occupatoin for those who earn > 50K in india

# In[53]:


occupation=df[(df["salary"]==">50K") & (df["native-country"]=="India")]["occupation"].value_counts().idxmax()


# In[54]:


print(occupation)


# In[ ]:




