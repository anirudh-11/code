#%%

import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
from math import pi


def make_spider( row, title, color, df):
 
# number of variable
    categories=list(df)[1:]
    N = len(categories)
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
 
# Initialise the spider plot
    ax = plt.subplot(2,2,row+1, polar=True, )
 
# If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
 
# Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=8)
 
# Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
    plt.ylim(0,40)
 
# Ind1
    values=df.loc[row].drop('Shop Category').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, values, color=color, alpha=0.4)
 
# Add a title
    plt.title(title, size=11, color=color, y=1.1)




def main():
    x = {'Shop Category' : ['Textile', 'Jewellery', 'Cleaning Essentials', 'Cosmetics'], 'Quarter 1' : [10, 5, 15, 14], 'Quarter 2' : [6, 5, 20, 10], 'Quarter 3' : [8, 2, 16, 21], 'Quarter 4' : [13, 4, 15, 11]}
    data = pd.DataFrame(x)
    my_dpi=96
    plt.figure(figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)
 
# Create a color palette:
    my_palette = plt.cm.get_cmap("Set2", len(data.index))
 
# Loop to plot
    for row in range(0, len(data.index)):
        make_spider( row=row, title=data['Shop Category'][row], color=my_palette(row), df = data)
    print(data)
    

if(__name__ == '__main__'):
    main()

# %%
