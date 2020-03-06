import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mode

def main():
    data = [22, 21, 24, 19, 27, 28, 24, 25, 29, 28, 26, 31, 28, 27, 22, 39, 20, 10, 26, 24, 27, 28, 26, 28, 18, 32, 29, 25, 31, 27]
    data.sort()
    stem = 0
    stem_leaf = dict()
    i = 0
    while(i < len(data)):
        if(int(data[i] / 10) == stem):
            stem_leaf[stem].append(data[i] % 10)
            i += 1
        else:
            stem += 1
            stem_leaf[stem] = []
    
    for key in stem_leaf.keys():
        print("{} : {}".format(key, stem_leaf[key]))
if(__name__ == "__main__"):
    main()