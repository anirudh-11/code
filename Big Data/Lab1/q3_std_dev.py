import pandas as pd
import numpy as np

def main():
    x = np.random.randint(low = 5, high = 500, size  = 20)
    print("x = ", x, "\nstd(x) = ", x.std())

    y = list(map(lambda var : ((var * 2) + 3), x))
    y = np.array(y)
    print("y = ", y, "\nstd(y) = ", y.std())

if __name__ == "__main__":
    main()