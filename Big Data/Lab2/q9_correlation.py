#%%

import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

def main():
    data = {'Temperature' : [98, 87, 90, 85, 95, 75], 'Number of Customers' : [15, 12, 10, 10, 16, 7]}
    data = pd.DataFrame(data)
    data_corr = data.corr()
    sns.heatmap(data_corr, annot = True)
    plt.plot()

if(__name__ == '__main__'):
    main()

# %%
