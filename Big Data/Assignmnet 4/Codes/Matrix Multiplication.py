#!/usr/bin/env python
# coding: utf-8

# Importing necessary modules

# In[2]:


import findspark
findspark.init()


# In[7]:


import numpy as np
from pyspark.mllib.linalg.distributed import RowMatrix
from pyspark.mllib.linalg.distributed import *

from pyspark import SparkContext
from pyspark.sql.session import SparkSession


# Creating a sparkcontext and sparksession

# In[8]:


sc = SparkContext("local","PySpark Word Count Exmaple")
spark = SparkSession(sc)


# Creating 2 random arrays for multiplication

# In[4]:


A = np.arange(1024 ** 2, dtype=np.float64).reshape(1024, 1024)
B = np.arange(1024 ** 2, dtype=np.float64).reshape(1024, 1024)


# This function converts the np.array into blockmatrix data type
# We need to use blockmatrix datatype to access multiplication

# In[5]:


def as_block_matrix(rdd, rowsPerBlock=1024, colsPerBlock=1024):
    return IndexedRowMatrix(rdd.zipWithIndex().map(lambda xi: IndexedRow(xi[1], xi[0]))).toBlockMatrix(rowsPerBlock, colsPerBlock)


# we are converting the A and B to block matrix and computing the product

# In[9]:


matrixA = as_block_matrix(sc.parallelize(A))
matrixB = as_block_matrix(sc.parallelize(B))
product = matrixA.multiply(matrixB)


# We need to convert a blockmatrix to localmatrix in order to print

# In[13]:


print(product.toLocalMatrix())


# A - matrix

# In[14]:


print(A)


# B - matrix

# In[15]:


print(B)


# The product when computed using np method

# In[16]:


A.dot(B)


# In[ ]:




