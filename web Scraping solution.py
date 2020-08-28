#!/usr/bin/env python
# coding: utf-8

# In[12]:


import requests
link="https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area"
link=requests.get(link).text


# In[13]:


from bs4 import BeautifulSoup
soup=BeautifulSoup(link,"lxml")


# In[14]:


print(soup.prettify())


# In[15]:


all_link=soup.find_all("a")


# In[16]:


for link in all_link:
    print(link.get("href"))


# In[19]:


all_tables=soup.find_all("table")
all_tables


# In[20]:


required=soup.find("table",class_="wikitable sortable")
required


# In[21]:


country_links=required.find_all("a")
country_links


# In[22]:


country=[]
for links in country_links:
    country.append(links.get("title"))
country 


# In[23]:


import pandas as pd


# In[24]:


data=pd.DataFrame()
data["Country"]=country


# In[26]:


data.to_csv("C:/Users/RAGHAVENDRA/Desktop/country_obtained_through_webscraping.csv")


# In[27]:


data.head()

