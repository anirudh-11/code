#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

def main():
    data = dict()
    data['Fuel'] = [3.6, 6.7, 9.8, 11.2, 14.7]
    data['Mass'] = [0.45, 0.91, 1.36, 1.81, 2.27]
    sns.scatterplot(x = data['Fuel'], y = data['Mass'])
    plt.show()


if(__name__ == '__main__'):
    main()


# %%
