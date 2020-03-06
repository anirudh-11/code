#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    x = np.array([7, 9, 27, 28, 55, 45, 34, 65, 54, 67, 34, 23, 24, 66, 53, 45, 44, 88, 22, 33, 55, 35, 33, 37, 47, 41, 31, 30, 29, 12])
    data = pd.DataFrame(data = x)
    mean = data.mean()
    f, ax = plt.subplots(2, 4, sharex = False)
    sns.distplot(data, kde = False, rug = True, bins = 5, ax = ax[0, 0])
    sns.distplot(data, kde = False, rug = True, bins = 10, ax = ax[0, 1])
    sns.distplot(data, kde = False, rug = True, bins = 15, ax = ax[0, 2])
    sns.distplot(data, kde = False, rug = True, bins = 20, ax = ax[0, 3])
    sns.distplot(data, kde = False, rug = True, bins = 25, ax = ax[1, 0])
    sns.distplot(data, kde = False, rug = True, bins = 30, ax = ax[1, 1])
    sns.distplot(data, kde = False, rug = True, bins = 35, ax = ax[1, 2])
    sns.distplot(data, kde = False, rug = True, bins = 40, ax = ax[1, 3])

    plt.show()

if(__name__ == '__main__'):
    main()


# %%
