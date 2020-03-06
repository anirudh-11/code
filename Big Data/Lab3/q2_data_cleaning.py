# %%
import pandas as pd
import numpy as np
from pandas import qcut, cut
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import statsmodels.api as sm 
import pylab as py 
# %%
def fr_based_smoothing(data, fr, column_name, mode):
    i  = 0
    while(i + fr < data[column_name].count()):
        bin_data = np.array(data[column_name][i : i + fr].copy())
        
        if(mode == 1):
            data[column_name][i : i + fr] = np.repeat(bin_data.mean(), fr)
        elif(mode == 2):
            # print(bin_data.mean())
            data[column_name][i : i + fr] = np.repeat(np.median(bin_data), fr)
        elif(mode == 3):
            for j in range(i, i + fr):
                if(data[column_name][j] <= bin_data.mean()):
                    data[column_name][j] = bin_data.min()
                else:
                    data[column_name][j] = bin_data.max()
        i = i + fr
    if(i - fr < data[column_name].count()):
        bin_data = np.array(data[column_name][i - fr : data[column_name].count()])
        if(mode == 1):
            data[column_name][i - fr : data[column_name].count()] = np.repeat(bin_data.mean(), data[column_name].count() - i + fr)
        elif(mode == 2):
            data[column_name][i - fr : data[column_name].count()] = np.repeat(np.median(bin_data), data[column_name].count() - i + fr)
        elif(mode == 3):  
            for j in range(i, data[column_name].count()):
                if(data[column_name][j] <= bin_data.mean()):
                    data[column_name][j] = bin_data.min()
                else:
                    data[column_name][j] = bin_data.max()  
    return data

# %%
# def main():
data = pd.read_excel('/home/anirudh/Big Data/Lab3/avocado.xlsx')
data = data.sort_values('Total Volume')
data['Date'] = pd.to_datetime(data['Date'])


#%%
num_of_bins = int(data['Total Volume'].count() / 50)
data = data.reset_index(drop=True)
Total_volume_50_mean = fr_based_smoothing(data, 50, 'Total Volume', 1)                           # fr based smoothing for mean
Total_volume_50_median = fr_based_smoothing(data, 50, 'Total Volume', 2)
Total_volume_250_mean = fr_based_smoothing(data, 250, 'Total Volume', 1)
Total_volume_250_median = fr_based_smoothing(data, 250, 'Total Volume', 2)
count = data['Total Volume'].count()
count = int(count / 100)
Total_volume_boundaries = data[2 * count : data['Total Volume'].count() - (2 * count)].copy()
Total_volume_boundaries = Total_volume_boundaries.reset_index(drop = True)
# print(Total_volume_50_boundaries['Total Volume'][337])
Total_volume_50_boundaries = fr_based_smoothing(Total_volume_boundaries, 50, 'Total Volume', 3)
Total_volume_250_boundaries = fr_based_smoothing(Total_volume_boundaries, 250, 'Total Volume', 3)



#%%
data['Date'] = pd.to_datetime(data['Date'])
data_with_date_as_index = data.copy()
data_with_date_as_index.set_index(data_with_date_as_index["Date"],inplace=True)
data_month = data_with_date_as_index.groupby(pd.Grouper(freq = 'M'))
data_year = data_with_date_as_index.groupby(pd.Grouper(freq="Y"))
print("Data aggregated to month : ")
print(data_month['Total Volume'].sum())
print("Data aggregated to year : ")
print(data_year['Total Volume'].sum())

#%%
print(data.isnull().sum())

#%%
data["AveragePrice"] = data["AveragePrice"].replace('NAN', "0")
data["AveragePrice"] = data["AveragePrice"].replace('na', "0")
data['AveragePrice'] = pd.to_numeric(data['AveragePrice'])
mean_of_avg_price = data.groupby(['region']).mean()
Coutries = mean_of_avg_price.index
filter =  data['AveragePrice'] == 0
for ind in data.where(filter).dropna().index:
    data['AveragePrice'][ind] = mean_of_avg_price['AveragePrice'][data['region'][ind]]

#%%
data['Index'] = np.array(range(0, data['Total Volume'].count()))
data.set_index(data['Index'], inplace = True)
# print(data)
for ind in data.index:
    if(data['year'][ind] < 2017):
        data['Date'][ind] = 'Old'
    elif(data['year'][ind] == 2017):
        data['Date'][ind] = 'New'
    else:
        data['Date'][ind] = 'Recent'

print(data)

# %%
f, ax = plt.subplots(4, 1)
sns.kdeplot(data = data['Total Volume'], ax = ax[0])
sns.kdeplot(data = Total_volume_50_mean['Total Volume'], ax = ax[1])
sns.kdeplot(data = Total_volume_50_median['Total Volume'], ax = ax[2])
sns.kdeplot(data = Total_volume_50_boundaries['Total Volume'], ax = ax[3])
sm.qqplot(data = data['Total Volume'], line = '45')

plt.show()
#%%
# if(__name__ == '__main__'):
#     main()

# %%
