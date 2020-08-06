#!/usr/bin/env python
# coding: utf-8

# Importing Modules

# In[2]:


import findspark
findspark.init()


# In[3]:


from pyspark.sql.functions import split


# In[4]:


from pyspark.ml.clustering import KMeans
from pyspark import SparkContext, since


# In[5]:


from pyspark.sql import SQLContext as sc


# In[6]:


from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.ml.feature import VectorAssembler


# Creating spark context and starting a session

# In[7]:


sc = SparkContext.getOrCreate()
spark = SparkSession(sc)


# Reading the data

# In[8]:


lines = sc.textFile("F:\Docs\Big data\Assignment\Assignmnet 4\Dataset\pumsb.dat")


# creating a 2d list from the data read. We are skipping the first attribute.

# In[48]:


data = []
for line in lines.collect():
    l = str(line)
    feature_list = line.split()
    feature_list = feature_list[1 : :]
    data.append(list(map(lambda x : int(x), feature_list)))
print("The total number of data points are : ",len(data))


# Creating a columnname for all the attributes

# In[11]:


colname = []
for i in range(len(data[0])):
    colname.append("A_" + str(i))


# In[61]:


print(colname)


# Creating a dataframe out of the 2d list we created

# In[49]:


df = spark.createDataFrame(data, colname)


# In[50]:


print(df.show())


# Aliasing the inbuild KMeans function as kmeans with number of clusters 5 and seed as 1 (random initial points)

# In[51]:


kmeans = KMeans(k = 5, seed = 1) 


# To make the data readable by the module, we need to transform them. So we are transforming them using the below code.
# Transformation is nothing but making  afeature vector of all the input attribute and storing it as an attribute

# In[52]:


vecAssembler = VectorAssembler(inputCols=colname, outputCol="features")


# In[53]:


new_df = vecAssembler.transform(df)
new_df.show()


# Now we are fitting the model.

# In[54]:


model = kmeans.fit(new_df.select('features'))


# We are dropping all the initial columns and showing the only the feature vector of each row with its cluster

# In[55]:


transformed = model.transform(new_df)
# for name in colname:
#     transformed.drop(name).collect()
    
transformed = transformed.drop(*colname)
transformed.show()    


# Printing the centers of the clusters

# In[58]:


print("The Centres are : ")
for centre in model.clusterCenters(): 
    print(centre)


# In[ ]:




