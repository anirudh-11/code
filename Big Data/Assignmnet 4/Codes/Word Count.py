#!/usr/bin/env python
# coding: utf-8

# Importing necessary modules

# In[1]:


import findspark
findspark.init()


# In[2]:


import pyspark
import sys
 
from pyspark import SparkContext, SparkConf


# Creating a spark context

# In[3]:


sc = SparkContext("local","PySpark Word Count Exmaple")


# Reading the inputfile and storing each word in the file as words

# In[4]:


words = sc.textFile("F:\Docs\Big data\Assignment\Assignmnet 4\Dataset\input.txt").flatMap(lambda line: line.split(" "))


# We are counting the occurance of each word

# In[5]:


wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)


# Saving it as a text file

# In[6]:


wordCounts.saveAsTextFile("F:\Docs\Big data\Assignment\Assignmnet 4\Dataset\output")


# Printing the counts

# In[7]:


print(wordCounts.collect())


# In[ ]:




