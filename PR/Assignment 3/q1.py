# import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
# import pandas as pd


def perceptron():
    w1 = np.array([[1, 0, 0], [1, 0, 1], [1, 1, 0]])
    w2 = np.array([[1, 1, 1]])
    data = np.concatenate([w1, -w2], axis = 0)
    print(data)
    w1 = np.array([[0, 0], [0, 1], [1, 0]])
    w2 = np.array([[1, 1]])
    learning_rate = 0
    k = 0
    Q = 0                           #criterian theta
    a = np.array([0, 0, 0])            #weights
    missclasified_vectors = True
    epoch = 1
    while((missclasified_vectors) or not(k == 0)):
        if(k == 0):
            print("\n\n\nEpoch : ", epoch)
            epoch = epoch + 1
            missclasified_vectors = False
        print("Data index : ", k)
        print("weights : ", a)
        print("Data point : ", np.array(data[k]))
        dot_product = np.dot(a, data[k])
        print("The dot product is : ", dot_product)
        print(dot_product)
        if(dot_product <= 0):
            f, ax = plt.subplots(figsize=(7, 7))
            c1, c2 = "#3366AA", "#AA3333"
            ax.scatter(*w1.T, c=c1,s = 10, label = "w1")
            ax.legend()
            ax.scatter(*w2.T, c=c2, marker="D", label = "w2")
            ax.legend()
            a = a + data[k]
            x_vec = np.linspace(-0.5, 2, 5)
            y_vec = ((a[1] * x_vec) + a[0])/a[2]
            # print(y_vec)
            y_vec = -y_vec   
            plt.plot(x_vec, y_vec, 'r--')

            missclasified_vectors = True
        k = (k + 1) % (len(data))

    print("The final weight vector is : ", a)
    x_vec = np.linspace(-0.5, 2, 5)
    y_vec = ((a[1] * x_vec) + a[0])/a[2]
    # print(y_vec)
    y_vec = -y_vec   
    plt.plot(x_vec, y_vec, 'r--')
    plt.show()

z = []
data = []
alpha = []

def func(alpha):
    alpha = np.array(alpha)
    value = np.sum(alpha)
    for i in range(len(alpha)):
        for j in range(len(alpha)):
            if(i == j):
                pass
            value -= 0.5 * (alpha[i] * alpha[j] * z[i] * z[j] * (data[i].T.dot(data[j])))
    return (-value)

def constraint(alpha):
    global z
    sum = 0
    for alpha_i, z_i in zip(alpha, z):
        sum += alpha_i * z_i
    return(sum)

def abs(num):
    if(num < 0):
        return(-num)
    else:
        return(num)

def svm():
    global z
    global data
    global alpha
    z = np.array([1, 1, 1, -1])
    w1 = np.array([[0, 0], [1, 0], [0, 1]])
    w2 = np.array([[1, 1]])
    data = np.concatenate([w1, w2], axis = 0)
    print("data : ", data)
    max_solution = 0
    consrt = {'type' : 'eq', 'fun' : constraint}
    alpha = np.zeros(len(data))
    b = (0.0000000000, None)
    bound = [b, b, b, b] 
    sol = minimize(func, alpha, method = 'SLSQP', constraints = consrt, bounds = bound)
    print(sol)
    alpha = sol.x

    print("lagrange multiplier are : ", alpha)

    a = np.zeros(len(data[0]))
    for i in range(len(data)):
        a += alpha[i]*z[i]*data[i]
    
    bias = []                                          #finding the points that pass through the w.x + b = +/- 1
    for i in range(len(alpha)):
        for j in range(len(alpha)):
            if(i == j):
                pass
            else:
                if(abs(0.5 * (alpha[i] * alpha[j] * z[i] * z[j] * (data[i].T.dot(data[j])))) > 0.05):
                    bias.append(1/z[i] - a.T.dot(data[i]))
                    
    bias = np.array(bias).mean()
    print("bias is ", bias)
    print("weight vector is : ", a)
    a = [bias, a[0] , a[1]] 
    f, ax = plt.subplots(figsize=(7, 7))
    c1, c2 = "#3366AA", "#AA3333"

    x_vec = np.linspace(-0.5, 2, 5)
    y_vec = ((a[1] * x_vec) + a[0])/a[2]
    y_vec = -y_vec
    plt.plot(x_vec, y_vec, 'r--')
    y_vec = y_vec + (1 / a[2])
    plt.plot(x_vec, y_vec, 'g--')
    y_vec = y_vec - (2/ a[2])
    plt.plot(x_vec, y_vec, 'g--')
    
    ax.scatter(*w1.T, c=c1,s = 10, label = "w1")
    ax.legend()
    ax.scatter(*w2.T, c=c2,s = 10, marker="D", label = "w2")
    ax.legend()

    plt.show()
    

if(__name__ == '__main__'):
    perceptron()
    svm()