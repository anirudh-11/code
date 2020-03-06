#%%

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    x = np.array([35, 54, 60, 65, 66, 67, 69, 70, 72, 73, 75, 76, 54, 25, 15, 60, 65, 66, 67, 69, 70, 72, 130, 73, 75, 76])
    data = pd.DataFrame(x)
    f, ax = plt.subplots(3, 1)
    sns.boxplot(x = data[0], data = data, ax = ax[0], whis = np.inf)
    sns.swarmplot(x = data[0], data = data, ax = ax[1])
    sns.boxplot(x = data[0], data = data, ax = ax[2], whis = np.inf)
    sns.swarmplot(x = data[0], data = data, ax = ax[2], color = "0.2")
    plt.show()
if(__name__ == '__main__'):
    main()

# %%
