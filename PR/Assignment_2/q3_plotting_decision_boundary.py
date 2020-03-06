#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

def decision_boundary(x, W, w, x0):
    return(x.dot(W.dot(x.transpose())) + w.dot(x.transpose()) + x0)

def main():
    w1 = np.array([[2, 6], [3, 4], [3, 8], [4, 6]])
    w2 = np.array([[3, 0], [1, -2], [3, -4], [5, -2]])
    w1_mean = np.mean(w1, axis = 0)
    w2_mean = np.mean(w2, axis = 0)

    z1 = np.array([list(map((lambda num : num - w1_mean[0]), w1[:, 0].tolist())), list(map((lambda num : num - w1_mean[1]), w1[:, 1].tolist()))])
    z2 = np.array([list(map((lambda num : num - w2_mean[0]), w2[:, 0].tolist())), list(map((lambda num : num - w2_mean[1]), w2[:, 1].tolist()))])

    w1_covariance = (1 / 3) * z1.dot(z1.transpose())
    w2_covariance = (1 / 3) * z2.dot(z2.transpose())

    print(w1_covariance, "\n", w2_covariance)

    print("Since covariance(w1) = covariance(w2) = k.I, the decision boundary falls in the first case")

    sigma_sq = 8/3
    
    print("When p(w1) = p(w2) :")
    w10 = -(0.5) * ((w1_mean.transpose().dot(np.linalg.inv(w1_covariance).dot(w1_mean))) - np.log(np.linalg.det(w1_covariance)))
    W1 = -(0.5) * np.linalg.inv(w1_covariance)
    w20 = -(0.5) * ((w2_mean.transpose().dot(np.linalg.inv(w2_covariance).dot(w2_mean))) - np.log(np.linalg.det(w2_covariance)))
    W2 = -(0.5) * np.linalg.inv(w2_covariance)
    w11 = (w1_mean).dot(np.linalg.inv(w1_covariance))
    w22 = (w2_mean).dot(np.linalg.inv(w2_covariance))
    W = W1 - W2
    w = w11 - w22
    x0 = w10 - w20
    
    print("When p(w1) = p(w2) :")
    print(np.array([w1_mean]).transpose())
    print("x0", x0)
    print([decision_boundary(ele, W, w, x0) for ele in w1])
    print([decision_boundary(ele, W, w, x0) for ele in w2])

    f, ax = plt.subplots(figsize=(7, 7))
    c1, c2 = "#3366AA", "#AA3333"
    ax.scatter(*w1.T, c=c1, s=40, label = "w1")
    ax.scatter(*w2.T, c=c2, marker="D", s=40, label = "w2")
    ax.legend()
    y, x = np.ogrid[-10 : 10 : 1000j, -10 : 10 : 1000j]
    plt.contour(x.ravel(), y.ravel(), W[0][0] * x ** 2 + x*y*(W[0][1] + W[1][0]) + W[1][1] * y ** 2 + x0 + w[0] * x + w[1] * y, [0])

    # print(y_vec)   
    # plt.plot(x_vec, y_vec, 'r--')
    plt.show()

    print("w22", w22)



if __name__ == "__main__":
    main()

# %%
