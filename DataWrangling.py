#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing Libraries

import pandas as pd
import numpy as np


# # Data Acquisition 

# In[2]:


#loading data set1

dataset1 = pd.read_excel("C:/Users/vipin/OneDrive/Documents/Desktop/Project2/dataset_1.xlsx")


# In[3]:


#printing dataset 1

dataset1


# In[4]:


#printing top 10 Entries

dataset1.head(10)


# In[5]:


#printing last 10 Entries

dataset1.tail(10)


# In[6]:


#Getting DataType Info

dataset1.info()


# In[7]:


#Generate descriptive statistics

dataset1.describe()


# In[8]:


#Finding Null Value

dataset1.isnull()


# In[9]:


#Summing of Null Value

dataset1.isnull().sum()


# In[10]:


#load dataset 2

dataset2 = pd.read_excel("C:/Users/vipin/OneDrive/Documents/Desktop/Project2/dataset_2.xlsx") 


# In[11]:


#printing dataset 2

dataset2


# In[12]:


#printing top 5 Entries

dataset2.head()


# In[13]:


#printing last 5 Entries

dataset2.tail()


# In[14]:


#Getting DataType Info

dataset2.info()


# In[15]:


#Generate descriptive statistics

dataset2.describe()


# In[16]:


#Finding Null Value

dataset2.isnull()


# In[17]:


#Summing of Null Value

dataset2.isnull().sum()


# In[18]:


# Join the datasets using the merge function

Final = pd.merge(dataset1, dataset2, how='inner')


# In[19]:


# Save the final dataframe as a CSV file
Final.to_csv('Final.csv', index=False)

# Display the final dataframe
Final


# In[20]:


# Drop Unnamed columns

columns_to_drop = ['Unnamed: 0']
Final1 = Final.drop(columns=columns_to_drop, axis=1)

Final1


# In[21]:


#final column name

Final1.columns


# In[22]:


#dimensions of data 
Final1.shape


# # Data Wrangling

# Finding Unique Value

# In[23]:


unique_instant = Final1['instant'].unique()
unique_instant


# In[24]:


unique_dteday = Final1['dteday'].unique()
unique_dteday


# In[25]:


unique_seasons = Final1['season'].unique()
unique_seasons


# In[26]:


unique_year = Final1['yr'].unique()
unique_year


# In[27]:


unique_mnth = Final1['mnth'].unique()
unique_mnth


# In[28]:


unique_hr = Final1['hr'].unique()
unique_hr


# In[29]:


unique_holidays = Final1['holiday'].unique()
unique_holidays


# In[30]:


unique_weekday = Final1['weekday'].unique()
unique_weekday


# In[31]:


unique_weathersit = Final1['weathersit'].unique()
unique_weathersit


# In[32]:


unique_temp = Final1['temp'].unique()
unique_temp


# In[33]:


unique_atemp = Final1['atemp'].unique()
unique_atemp


# In[34]:


unique_hum = Final1['hum'].unique()
unique_hum


# In[35]:


unique_ws = Final1['windspeed'].unique()
unique_ws


# In[36]:


unique_casual = Final1['casual'].unique()
unique_casual


# In[37]:


unique_registered = Final1['registered'].unique()
unique_registered


# In[38]:


unique_cnt = Final1['cnt'].unique()
unique_cnt


# In[39]:


#second way to find the unique values of multiple column

# List of columns
count = ['instant', 'dteday', 'season', 'yr', 'mnth', 'hr', 'holiday', 'weekday',
                    'weathersit', 'temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']

# Dictionary for storing counts
unique_counts = {}

# Counting unique values for each column
for column in count:
    unique_counts[column] = Final1[column].nunique()

# Print counts
for column, count in unique_counts.items():
    print(f"Column '{column}': {count} unique values")


# In[40]:


#checking datatype

Final1.dtypes


# In[41]:


#checking missing values 

Final1.isnull().sum()


# #Finding missing values

# In[42]:


Final1.fillna(Final1.mean(numeric_only=True), inplace=True)


# In[43]:


Final1.fillna(Final1.median(numeric_only=True), inplace=True)


# In[44]:


Final1.fillna(Final1.mode(), inplace=True)


# In[45]:


#Checking final Missing values if any 

Final1.isnull().sum()


# In[46]:


#summary statistics

Final1.describe()


# In[47]:


# Calculate mean
mean_values = Final1.mean(numeric_only=True)

(mean_values)


# In[48]:


# Calculate median
median_values = Final1.median(numeric_only=True)

(median_values)


# In[49]:


# Calculate mode
mode_values = Final1.mode(numeric_only=True)
mode_values


# In[50]:


print("The dataset appears to be relatively clean and well-structured, with no missing values after filling them.")

print("The unique values for each column seem reasonable, indicating no obvious inconsistencies or errors.")

print("Summary statistics provide insights into the distribution and range of values for numerical columns.")

print("Further analysis and modeling can be performed on the cleaned dataset for insights and predictions.")


# In[51]:


dataset3 = pd.read_excel("C:/Users/vipin/OneDrive/Documents/Desktop/Project2/dataset_3.xlsx")


# In[52]:


dataset3


# In[53]:


#printing top 10 Entries

dataset3.head(10)


# In[54]:


#printing last 10 Entries

dataset3.tail(10)


# In[55]:


#Getting DataType Info

dataset3.info()


# In[56]:


#Generate descriptive statistics

dataset3.describe()


# In[57]:


#Finding Null Value

dataset3.isnull()


# In[58]:


#Summing of Null Value

dataset3.isnull().sum()


# In[59]:


combined_data = pd.concat([Final, dataset3], ignore_index=True)


# In[60]:


combined_data 


# In[61]:


# Drop Unnamed columns

columns_to_drop = ['Unnamed: 0']
combined_data1 = combined_data.drop(columns=columns_to_drop, axis=1)

combined_data1


# In[62]:


combined_data1.isnull().sum()


# In[63]:


combined_data1.fillna(combined_data1.mean(numeric_only=True), inplace=True)


# In[64]:


combined_data1.fillna(combined_data1.median(numeric_only=True), inplace=True)


# In[65]:


combined_data1.fillna(combined_data1.mode(), inplace=True)


# In[66]:


combined_data1.isnull().sum()


# In[67]:


skewness = combined_data1.skew()

skewness


# In[68]:


correlation = combined_data1.corr()
correlation


# In[69]:


combined_data1.describe()


# In[70]:


#second way to find the unique values of multiple column

# List of columns
count = ['instant', 'dteday', 'season', 'yr', 'mnth', 'hr', 'holiday', 'weekday',
                    'weathersit', 'temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']

# Dictionary for storing counts
unique_counts = {}

# Counting unique values for each column
for column in count:
    unique_counts[column] = combined_data1[column].nunique()

# Print counts
for column, count in unique_counts.items():
    print(f"Column '{column}': {count} unique values")


# In[71]:


combined_data1.dtypes


# In[72]:


# Calculate median
median_values = combined_data1.median(numeric_only=True)

(median_values)


# In[73]:


# Calculate median
mean_values = combined_data1.mean(numeric_only=True)

(mean_values)


# In[74]:


# Calculate mode
mode_values = combined_data1.mode(numeric_only=True)
mode_values


# In[113]:


combined_data1.to_csv('combined_dataset.csv', index=False)


# In[114]:


combined_data1


# In[82]:


import seaborn as sns
sns.boxplot(combined_data1['temp'])


# In[85]:


sns.boxplot(combined_data1['atemp'])


# In[88]:


sns.boxplot(combined_data1['casual'])


# In[89]:


sns.boxplot(combined_data1['registered'])


# In[90]:


sns.boxplot(combined_data1['cnt'])


# In[101]:


# IQR
Q1 = np.percentile(combined_data1['temp'], 25, method='midpoint')
Q3 = np.percentile(combined_data1['temp'], 75, method='midpoint')
IQR = Q3 - Q1
print(IQR)
lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR


# In[102]:


# IQR
Q1 = np.percentile(combined_data1['atemp'], 25, method='midpoint')
Q3 = np.percentile(combined_data1['atemp'], 75, method='midpoint')
IQR = Q3 - Q1
print(IQR)
lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR


# In[103]:


# IQR
Q1 = np.percentile(combined_data1['casual'], 25, method='midpoint')
Q3 = np.percentile(combined_data1['casual'], 75, method='midpoint')
IQR = Q3 - Q1
print(IQR)
lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR


# In[104]:


# IQR
Q1 = np.percentile(combined_data1['registered'], 25, method='midpoint')
Q3 = np.percentile(combined_data1['registered'], 75, method='midpoint')
IQR = Q3 - Q1
print(IQR)
lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR


# In[107]:


# IQR
Q1 = np.percentile(combined_data1['cnt'], 25, method='midpoint')
Q3 = np.percentile(combined_data1['cnt'], 75, method='midpoint')
IQR = Q3 - Q1
print(IQR)
lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR


# In[111]:


upper_array = np.where(combined_data1['temp'] >= upper)[0]
lower_array = np.where(combined_data1['temp'] <= lower)[0]
# Removing the outliers
combined_data1.drop(index=upper_array, inplace=True)
combined_data1.drop(index=lower_array, inplace=True)

# Print the new shape of the DataFrame
print("New Shape: ", combined_data1.shape)


# In[ ]:





# In[ ]:




