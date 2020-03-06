# %%

import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def main():
    print(1)
    x = np.random.normal(0.0, 1.0, 100)
    normal_data = pd.DataFrame(data = x)
    x = np.random.lognormal(0, 1, 5)
    log_normal_data = pd.DataFrame(x)
    f, ax = plt.subplots(1, 2)
    # print(x)
    sns.violinplot(data = normal_data, ax = ax[0])
    sns.violinplot(data = log_normal_data, ax = ax[1])
    plt.show()

if(__name__ == '__main__'):
    main()

# %%
