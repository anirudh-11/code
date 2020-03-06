#%%

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
def f(x, y):
   return np.array(np.sqrt(x ** 2 + y ** 2))

def main():
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.contour3D(X, Y, Z, 50)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('3D contour')
    plt.show()

if(__name__ == '__main__'):
    main()
# %%
