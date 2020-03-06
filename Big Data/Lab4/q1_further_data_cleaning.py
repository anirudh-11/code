# %%
import pandas as pd
import numpy as np
from pandas import qcut, cut
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
# import statsmodels.api as sm 
import pylab as py 
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder 
# %%
data_frame_to_be_deleted = []
avacado_data = pd.read_excel('/home/anirudh/Big Data/Lab4/avocado.xlsx')
avacado_data = avacado_data.sort_values('Total Volume')
avacado_data['Date'] = pd.to_datetime(avacado_data['Date'])
trail_data = pd.read_csv('/home/anirudh/Big Data/Lab4/Trail.csv')

# %%
modified_avacado_data = avacado_data.drop(columns = ['Unnamed: 0', 'Total Bags', 'Small Bags', 'Large Bags', 'XLarge Bags', 'region', 'Date'])
modified_avacado_data = modified_avacado_data[modified_avacado_data['type'] == 'organic']
print(modified_avacado_data)
# %%
data_frame_to_be_deleted = []
print("Number of records before droping duplicates = ", len(trail_data))
modified_trail_data = trail_data.drop_duplicates()
# modified_trail_data['AveragePrice'] = modified_trail_data['AveragePrice'].replace('Na', 1.25)
modified_trail_data['AveragePrice'].fillna(1.25, inplace = True)
print("Number of records after droping duplicates = ", len(modified_trail_data))
print(modified_trail_data['AveragePrice'])
data_frame_to_be_deleted.append(modified_trail_data)
# %%
del data_frame_to_be_deleted
data_frame_to_be_deleted = []
print(modified_avacado_data)
modified_avacado_data['year'] = modified_avacado_data['year'].map({2015 : 0, 2016 : 0, 2017 : 1, 2018 : 1})
print(modified_avacado_data)
# %%
data_frame_to_be_deleted.append(modified_avacado_data)
del data_frame_to_be_deleted
data_frame_to_be_deleted = []
integer_encoded_avacado_data = avacado_data.copy()
region_encoding = dict()
for ind, ele in enumerate(set(integer_encoded_avacado_data['region'])):
    region_encoding[ele] = ind
integer_encoded_avacado_data['year'] = integer_encoded_avacado_data['year'].map({2015 : 0, 2016 : 2, 2017 : 3, 2018 : 4})
integer_encoded_avacado_data['type'] = integer_encoded_avacado_data['type'].map({'organic' : 0, "conventional" : 1})
integer_encoded_avacado_data['region'] = integer_encoded_avacado_data['region'].map(region_encoding)
print(integer_encoded_avacado_data)
data_frame_to_be_deleted.append(integer_encoded_avacado_data)
# %%
del data_frame_to_be_deleted
data_frame_to_be_deleted = []
one_hot_encoded_avacado_data = avacado_data.copy()
# Get one hot encoding of columns B
one_hot = pd.get_dummies(one_hot_encoded_avacado_data['region'])
# print(one_hot)
# Drop column B as it is now encoded
one_hot_encoded_avacado_data = one_hot_encoded_avacado_data.drop('region',axis = 1)
# print(one_hot_encoded_avacado_data)
# Join the encoded df
one_hot_encoded_avacado_data = one_hot_encoded_avacado_data.join(one_hot)
print(one_hot_encoded_avacado_data)
data_frame_to_be_deleted.append(one_hot_encoded_avacado_data)
print(region_encoding[27])
# %%
del data_frame_to_be_deleted
data_frame_to_be_deleted = []
print(len(avacado_data), len(avacado_data.dropna()))
print(avacado_data.dropna())

# %%
columns = avacado_data.columns
nullity_value_for_each_column = []
for column in columns:
    nullity_value_for_each_column.append(avacado_data[column].isnull().sum())
    print(column, " : ", nullity_value_for_each_column[-1])

print(column[nullity_value_for_each_column.index(max(nullity_value_for_each_column))])

print(avacado_data.drop(columns = [columns[nullity_value_for_each_column.index(max(nullity_value_for_each_column))]], inplace = False))


# %%
print(avacado_data.describe())

# %%
