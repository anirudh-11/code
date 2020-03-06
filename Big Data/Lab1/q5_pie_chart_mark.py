#%%

import matplotlib.pyplot as plt

def main():
    # Data to plot
    labels = 'S (100 - 85)', 'A (85 - 70)', 'B (70 - 55)', 'C (55 - 40)'
    sizes = [31, 29, 25, 15]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0, 0)  # explode 1st slice

    # Plot
    plt.pie(sizes, explode = explode, labels = labels, colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 140)

    plt.axis('equal')
    plt.show()

if(__name__ == '__main__'):
    main()

# %%
