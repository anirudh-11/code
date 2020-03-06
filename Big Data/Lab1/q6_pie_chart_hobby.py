#%%

import matplotlib.pyplot as plt

def main():
    # Data to plot
    labels = 'Study', 'Sleep', 'Play', 'Hobby', 'Family and Friends'
    sizes = [33, 30, 18, 5, 14]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', "#e377c2"]
    explode = (0.1, 0, 0, 0, 0)  # explode 1st slice

    # Plot
    plt.pie(sizes, explode = explode, labels = labels, colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 140)

    plt.axis('equal')
    plt.show()

if(__name__ == '__main__'):
    main()

# %%
