#%%

import seaborn as sns 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.random.randint(low = 25, high = 50, size = 100)
    y = np.random.randint(low = 10, high = 50, size = 100)
    data = {'X' : list(x), 'Y' : list(y)}
    data = pd.DataFrame(data)
    joint_kws=dict(gridsize = 8)
    sns.jointplot(x = 'X', y = 'Y', data = data, kind = 'hex', joint_kws = joint_kws)
    plt.show()

    
if(__name__ == '__main__'):
    main()

# %%
