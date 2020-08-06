#!/usr/bin/env python
# coding: utf-8

# Importing essential modules

# In[1]:


import findspark
findspark.init()


# In[2]:


from pyspark.sql.functions import split


# In[3]:


from pyspark.ml.fpm import FPGrowth
from pyspark import SparkContext, since


# In[4]:


from pyspark.sql import SQLContext as sc


# In[5]:


from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession


# Creating a spark context and starting a session

# In[6]:


sc = SparkContext.getOrCreate()
spark = SparkSession(sc)


# Reading the input data

# In[7]:


lines = sc.textFile("F:\Docs\Big data\Assignment\Assignmnet 4\Dataset\kosarak.dat")


# Converting the input data into id and transactions as a list

# In[8]:


data = []
i = 0
for line in lines.collect():
    data.append((i,list(set(map(lambda x : int(x) ,str(line).split())))))    
    i = i + 1
print("The total number of transactions are : ",len(data))


# Creating a sparks dataframe

# In[17]:


df = spark.createDataFrame(data, ["id", "items"])


# In[18]:


print(df.show())


# Aliasing the inbuild FPGrowth function as fpgrwoth and setting the minimumsupport to be 0.05 (that is around 50000) and min confidence as 0.75

# In[19]:


fpGrowth = FPGrowth(itemsCol="items", minSupport=0.05, minConfidence=0.75)


# Fitting our model

# In[20]:


model = fpGrowth.fit(df)


# Printing frequent item list

# In[21]:


print("The frequent Item set is : ")
model.freqItemsets.show()


# Printing association rules

# In[22]:


print("The Association rule is : ")
model.associationRules.show()


# Showing the predicted consequents if any for each transaction

# In[23]:


print("Examining the input items against all the association rules and summarize the consequents as prediction")
model.transform(df).show()


# In[ ]:




