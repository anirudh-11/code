#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mode

def main():
    data = {'WATER' : [3.2, 3.5, 3.6, 2.5, 2.8, 5.9, 2.9, 3.9, 4.9, 6.9, 7.9, 8.0, 3.3, 6.6, 4.4], 'BEVERAGES' : [2.2, 2.5, 2.6, 1.5, 3.8, 1.9, 0.9, 3.9, 4.9, 6.9, 0.1, 8.0, 0.3, 2.6, 1.4]}
    data = pd.DataFrame(data = data)
    print(data.head())
    f, ax = plt.subplots(2, 2)
    sns.rugplot(data['WATER'], ax = ax[0, 0], height = 0.5)
    sns.kdeplot(data['WATER'], ax = ax[0, 1])
    sns.rugplot(data['BEVERAGES'], ax = ax[1, 0], height = 0.5)
    sns.kdeplot(data['BEVERAGES'], ax = ax[1, 1])
    plt.show()
if(__name__ == '__main__'):
    main()


# %%
