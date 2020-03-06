
# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mode

# run cell
def main():
    x = np.array([167.65, 167, 172, 175, 165, 167, 168, 167, 167.3, 170, 167.5, 170, 167, 169, 172])
    mde = mode(x)
    data = pd.DataFrame(data = x)
    mean = data.mean()
    median = data.median()
    std = data.std()
    skew = ((mean - mde) / std)
    ax = sns.distplot(data, kde = True, bins = 13)
    plt.axvline(np.mean(x), color='b', linestyle='--')
    plt.axvline(np.median(x), color='r', linestyle='--')
    plt.axvline(np.array(mde), color='g', linestyle='--')
    # plt.axvline(np.std(x), color='y', linestyle='--')
    # plt.axvline(np.array(skew), color='gray', linestyle='--')
    
    plt.legend({'Mean' : mean, 'Median' : median, 'Mode' : mode})
    plt.show()

    print("Mean = {}, Median = {}, Mode = {}, Standard Deviation = {}, Skewness = {}".format(mead, median, mde, std, skew))



if __name__ == "__main__":
    main()

# %%
