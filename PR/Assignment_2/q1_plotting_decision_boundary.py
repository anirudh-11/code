#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 


def decision_boundary(x, w, x0):
    return(w.dot((x - x0).transpose()))


def main():
    w1 = np.array([[1, 6], [3, 4], [3, 8], [5, 6]])
    w2 = np.array([[3, 0], [1, -2], [3, -4], [5, -2]])
    
    print("w1 = \n", w1, "\nw2 = \n", w2)

    w1_mean = np.mean(w1, axis = 0)
    w2_mean = np.mean(w2, axis = 0)
    
    print("w1_mean = \n", w1, "\nw2_mean = \n", w2)
    
    z1 = w1 - w1_mean
    z2 = w2 - w2_mean
    w1_covariance = (1 / 3) * z1.transpose().dot(z1)
    w2_covariance = (1 / 3) * z2.transpose().dot(z2)

    print("w1_covariance = \n", w1_covariance, "\nw2_covariance = \n", w2_covariance)

    print("Since covariance(w1) = covariance(w2) = k.I, the decision boundary falls in the first case")

    sigma_sq = 8/3
    
    print("When p(w1) = 0.8 and p(w2) = 0.2 :")
    print(np.array([w1_mean]).transpose())
    x0 = 0.5 * (w1_mean + w2_mean) - sigma_sq * np.log(0.8 / 0.2) * (w1_mean - w2_mean) / ((w1_mean - w2_mean).transpose().dot(w1_mean - w2_mean))
    w = (w1_mean - w2_mean)
    print("x0 ", x0)
    print("w ", w)
    print([decision_boundary(ele, w, x0) for ele in w1])
    print([decision_boundary(ele, w, x0) for ele in w2])

    f, ax = plt.subplots(figsize=(7, 7))
    c1, c2 = "#3366AA", "#AA3333"
    ax.scatter(*w1.T, c=c1, s=40)
    ax.scatter(*w2.T, c=c2, marker="D", s=40)
    x_vec = np.linspace(-10, 10, 5)
    y_vec = ((w1_mean[0] - w2_mean[0])*x_vec - (w1_mean[0] - w2_mean[0])* x0[0] + (w1_mean[1] - w2_mean[1])*x0[1]) / (w1_mean[1] - w2_mean[1])
    print(y_vec)   
    plt.plot(x_vec, y_vec)
    
    print("When p(w1) = p(w2) :")
    print(np.array([w1_mean]).transpose())
    x0 = 0.5 * (w1_mean + w2_mean) - sigma_sq * np.log(1) * (w1_mean - w2_mean) / ((w1_mean - w2_mean).transpose().dot(w1_mean - w2_mean))
    w = (w1_mean - w2_mean)
    print("x0", x0)
    print([decision_boundary(ele, w, x0) for ele in w1])
    print([decision_boundary(ele, w, x0) for ele in w2])

    f, ax = plt.subplots(figsize=(7, 7))
    c1, c2 = "#3366AA", "#AA3333"
    ax.scatter(*w1.T, c=c1, s=40, label = "w1")
    ax.legend()
    ax.scatter(*w2.T, c=c2, marker="D", s=40, label = "w2")
    ax.legend()
    x_vec = np.linspace(-10, 10, 5)
    y_vec = (w[1]*x0[1] - w[0]*(x_vec - x0[0]))/w[1]
    print(y_vec)   
    plt.plot(x_vec, y_vec, 'r--')
    plt.show()



if __name__ == "__main__":
    main()

# %%
