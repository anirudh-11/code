#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

def decision_boundary(x, w, x0):
    return(w.dot((x - x0).transpose()))


def main():
    w1 = np.array([[1, -1], [2, -5], [3, -6], [4, -10], [5, -12], [6, -15]])
    w2 = (-1)*w1
    w1_mean = np.mean(w1, axis = 0)
    w2_mean = np.mean(w2, axis = 0)

    z1 = np.array([list(map((lambda num : num - w1_mean[0]), w1[:, 0].tolist())), list(map((lambda num : num - w1_mean[1]), w1[:, 1].tolist()))])
    z2 = np.array([list(map((lambda num : num - w2_mean[0]), w2[:, 0].tolist())), list(map((lambda num : num - w2_mean[1]), w2[:, 1].tolist()))])

    w1_covariance = (1 / 5) * z1.dot(z1.transpose())
    w2_covariance = (1 / 5) * z2.dot(z2.transpose())

    print(w1_covariance, "\n", w2_covariance)

    print("Since covariance(w1) = covariance(w2) , the decision boundary falls under the first case")

    sigma_sq = 8/3

    print("When p(w1) = 0.8 and p(w2) = 0.2 :")
    x0 = 0.5 * (w1_mean + w2_mean) - sigma_sq * np.log(0.3 / 0.7) * (w1_mean - w2_mean) / (((w1_mean - w2_mean).transpose().dot(np.linalg.inv(w1_covariance).dot(w1_mean - w2_mean))))
    print("x0 : ", x0)
    w = np.linalg.inv(w1_covariance).dot(w1_mean - w2_mean)
    print("w : ", w)

    print([decision_boundary(ele, w, x0) for ele in w1])
    print([decision_boundary(ele, w, x0) for ele in w2])


    x_vec = np.linspace(-5, 5, 10)
    y_vec = (w[1]*x0[1] - w[0]*(x_vec - x0[0]))/w[1]
    print(x_vec)
    print(y_vec)
    f, ax = plt.subplots(figsize=(7, 7))
    c1, c2 = "#3366AA", "#AA3333"
    ax.scatter(*w1.T, c=c1, s=40, label  = "w1")
    ax.scatter(*w2.T, c=c2, marker="D", s=40, label = "w2")
    ax.legend()
    plt.plot(x_vec, y_vec, 'r--')

if __name__ == "__main__":
    main()

# %%
