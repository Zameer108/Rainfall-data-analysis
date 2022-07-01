#!/usr/bin/env python
# coding: utf-8

# ### GROUP A2

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df =pd.read_csv("C:/Users/Zammer Ahmed/python programme/MAIN PROJECT/District Rainfall Normal (in mm) Monthly, Seasonal And Annual  Data Period 1951-2000.csv")


# In[3]:


df


# In[4]:


df1=df.groupby('STATE/UT').sum()


# In[5]:


df1


# In[6]:


df1.shape


# In[7]:


df.shape


# In[8]:


df1.corr()


# In[9]:


plt.figure(figsize=(20,8),dpi=450)
p=sns.heatmap(df1.corr(),data=df1)
plt.title("Correlation")
p.tick_params(axis='x',labelrotation=0)


# In[10]:


plt.figure(figsize=(20,10),dpi=450)
p=sns.barplot(x=df1.index,y='ANNUAL',data=df1)
plt.title("ANNUAL RAINFALL STATE WISE")
p.tick_params(axis='x',labelrotation=90)
plt.ylabel("rainfall in mm");


# In[11]:


plt.figure(figsize=(30,10))
plt.pie(df1["ANNUAL"],labels=df1.index,autopct='%1.0f%%',rotatelabels=True)

plt.legend(loc=(1.5,0))


# In[12]:


# rainfall data state wise in rainy season(RAINY SEASON IN INDIA IS FROM JUNE TO SEPTEMBER)
df1["RAINY_SEASON"] =df1[["JUN","JUL","AUG","SEP"]].sum(axis=1,numeric_only=True)
df1[["RAINY_SEASON"]]


# In[13]:


#rainy season
plt.figure(figsize=(20,10))
sns.barplot(x=df1.index,y="RAINY_SEASON", data=df1)
plt.title('Rainfall in Rainy Season')
plt.xticks(rotation=90);


# In[14]:


#rainfall in january
plt.figure(figsize=(20,10))
sns.barplot(x=df1.index,y='JAN', data=df1)
plt.title('Rainfall in January')
plt.xticks(rotation=90);


# ### Seasonal data

# In[15]:


df_seas = df[['STATE/UT','DISTRICT','JAN+FEB', 'MAM','JJAS','OND']]


# In[16]:


df_seas


# In[17]:


df_seas=df_seas.groupby("STATE/UT").sum()


# In[18]:


df_seas


# ### Annual data

# In[19]:


df_ann=df[['STATE/UT','ANNUAL']]


# In[20]:


df_ann


# In[21]:


df_ann=df_ann.groupby("STATE/UT").sum()
df_ann


# In[22]:


column = df_ann["ANNUAL"]


# In[23]:


max_rain = column.idxmax()


# In[24]:


#max rainfall in state annually
max_rain


# In[25]:


#min rainfall in state annually
min_rain =column.idxmin()


# In[26]:


min_rain


# ###  Rainfall data of delhi

# In[27]:


#rainfall data of delhi
del_df =df[df['STATE/UT']== "DELHI"]


# In[28]:


del_df


# In[29]:


del_df.sort_values("ANNUAL",axis=0)


# ###  UP rainy season analysis

# In[30]:


#rainfall data of up
UP_df =df[df['STATE/UT']== "UTTAR PRADESH"]
UP_df


# In[31]:


UP_df[['DISTRICT',"JUN","JUL","AUG","SEP"]]


# In[32]:


plt.figure(figsize=(20,8),dpi=450)
p=sns.barplot(x='DISTRICT',y='ANNUAL',data=UP_df)
plt.title("UP ANNUAL RAINFALL DISTRICT WISE")
p.tick_params(axis='x',labelrotation=90)
plt.ylabel("rainfall in mm");


# In[33]:


# top 10 district with lowesr rainfall in up
UP_df.sort_values("ANNUAL",axis=0, ascending=False).tail(10)


# In[34]:


# top 10 district with highes rainfall in up
UP_df.sort_values("ANNUAL",axis=0, ascending=False).head(10)


# In[35]:


#LETS ADD ALL RAINY SEASON DATA OF UP
UP_df["RAINY_SEASON"] =UP_df[["DISTRICT","JUN","JUL","AUG","SEP"]].sum(axis=1,numeric_only=True)
UP_df


# In[36]:


UP_df[["DISTRICT","RAINY_SEASON"]]


# In[37]:


#top 10 district with highest rainfall in rainy season
UP_df.sort_values("RAINY_SEASON",axis=0).head(10)


# In[ ]:





# In[38]:


UP_df.sort_values('ANNUAL',axis=0)


# ###  Rainfall data of Arunachal Pradesh

# In[39]:


Arunachal_df=df[df['STATE/UT']=='ARUNACHAL PRADESH']
Arunachal_df


# In[44]:


Arunachal_df["RAINY_SEASON"] =Arunachal_df[["JUN","JUL","AUG","SEP"]].sum(axis=1,numeric_only=True)
Arunachal_df[["RAINY_SEASON"]]


# In[40]:


plt.figure(figsize=(20,10))
sns.barplot(x='DISTRICT',y='ANNUAL', data=Arunachal_df)
plt.title('Annual Rainfall in AP')
plt.xticks(rotation=90);


# In[45]:


#Arunachal pradesh rainfall in rainy season;
plt.figure(figsize=(20,10),dpi=450)
sns.barplot(data=Arunachal_df, x="RAINY_SEASON",y='DISTRICT')


# In[ ]:




