import pandas as pd
import numpy as np


def main():
    data = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
    pos = data.index(25)
    data = np.array(data)
    max_min_normalisaion = list(map(lambda num : (num - data.min()) / (data.max() - data.min()), data))
    std = 12.94
    z_transform_normalisation = list(map(lambda num : (num - data.mean()) / std, data))
    decimal_scale_transformation = list(map(lambda num : (num / (10 ** (len(str(data.max()))))), data))
    print("max_min_normalisation of the above data is : \n{}\n and the value of 25 is {}\n".format(max_min_normalisaion, max_min_normalisaion[pos]))
    print("z_transform_normalisation of the above data is : \n{}\n and the value of 25 is {}\n".format(z_transform_normalisation, z_transform_normalisation[pos]))
    print("decimal_normalisation of the above data is : \n{}\n and the value of 25 is {}\n".format(decimal_scale_transformation, decimal_scale_transformation[pos]))

if(__name__ == '__main__'):
    main()