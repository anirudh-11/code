import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize


w1 = []
w2 = []
w3 = []
setosa = []  
virginica = []
versicolor = []

def data_processing():
    global w1
    global w2
    global w3
    global setosa
    global virginica
    global versicolor
    data = pd.read_csv("iris.csv")
    print(data.head())
    # print(data.loc('51'))
    column = ['petal.length', 'sepal.width']
    setosa = data[column][0 : 50].copy()
    versicolor = data[column][50 : 100].copy()
    virginica = data[column][100 : 150].copy()
    print(setosa.to_string())
    print(versicolor.head())
    print(virginica.head())
    w1 = []
    for index, row in setosa.iterrows():
        w1.append([row[0], row[1]])
    w1 = np.array(w1)

    w2 = []
    for index, row in versicolor.iterrows():
        w2.append([row[0], row[1]])
    w2 = np.array(w2)

    w3 = []
    for index, row in virginica.iterrows():
        w3.append([row[0], row[1]])
    w3 = np.array(w3)



def perceptron():
    global w1
    global w2
    global w3
    global setosa
    global virginica
    global versicolor

    # print(data.loc('51'))
    f, ax = plt.subplots(figsize=(7, 7))
    c1, c2, c3 = "#3366AA", "#AA3333", 'm'

    ax.scatter(*w1.T, c=c1,s = 10, label = "w1")
    ax.legend()
    ax.scatter(*w2.T, c=c2, marker="D", label = "w2")
    ax.legend()
    ax.scatter(*w3.T, c=c3, marker="X", label = "w2")
    ax.legend()



    data1 = []
    for i in range(len(w1)):
        data1.append([1, w1[i][0], w1[i][1]])
        data1.append([-1, -w2[i][0], -w2[i][1]])
        data1.append([-1, -w3[i][0], -w3[i][1]])
    data1 = np.array(data1)

    data2 = []
    for i in range(len(w2)):
        data2.append([1, w2[i][0], w2[i][1]])
        data2.append([-1, -w3[i][0], -w3[i][1]])
        data2.append([-1, -w1[i][0], -w1[i][1]])
    data2 = np.array(data2)
    
    data3 = []
    for i in range(len(w3)):
        data3.append([1, w3[i][0], w3[i][1]])
        data3.append([-1, -w1[i][0], -w1[i][1]])
        data3.append([-1, -w2[i][0], -w2[i][1]])
    data3 = np.array(data3)

    learning_rate = 0.01
    k = 0
    Q = 0                           #criterian theta
    a = np.array([0, 0, 0])            #weights
    missclasified_vectors = True
    epoch = 1
    while(((missclasified_vectors) or (not(k == 0))) and (epoch < 10)):
        if(k == 0):
            print("\n\n\nEpoch : ", epoch)
            epoch = epoch + 1
            missclasified_vectors = False
        print("Data index : ", k)
        print("weights : ", a)
        print("Data point : ", np.array(data1[k]))
        dot_product = np.dot(a, data1[k])
        print("The dot product is : ", dot_product)
        if(dot_product <= 0):            
            a = a + learning_rate * data1[k]
            missclasified_vectors = True
        k = (k + 1) % (len(data1))
    print("weights are : ", a)
    print(data1)
    x_vec = np.linspace(0, 10, 5)
    y_vec = ((a[1] * x_vec) + a[0])/a[2]
    y_vec = -y_vec   
    plt.plot(x_vec, y_vec, 'g--')



    # a = np.array([0, 0, 0])            #weights
    # missclasified_vectors = True
    # epoch = 1
    # while(((missclasified_vectors) or (not(k == 0))) and (epoch < 100)):
    #     if(k == 0):
    #         print("\n\n\nEpoch : ", epoch)
    #         epoch = epoch + 1
    #         missclasified_vectors = False
    #     print("Data index : ", k)
    #     print("weights : ", a)
    #     print("Data point : ", np.array(data2[k]))
    #     dot_product = np.dot(a, data2[k])
    #     print("The dot product is : ", dot_product)
    #     if(dot_product <= 0):            
    #         a = a + learning_rate * data2[k]
    #         missclasified_vectors = True
    #     k = (k + 1) % (len(data1))
    # print("weights are : ", a)
    # x_vec = np.linspace(0, 10, 5)
    # y_vec = ((a[1] * x_vec) + a[0])/a[2]
    # y_vec = -y_vec   
    # # plt.plot(x_vec, y_vec, 'r--')

    a = np.array([0, 0, 0])            #weights
    missclasified_vectors = True
    epoch = 1
    while(((missclasified_vectors) or (not(k == 0))) and (epoch < 100)):
        if(k == 0):
            print("\n\n\nEpoch : ", epoch)
            epoch = epoch + 1
            missclasified_vectors = False
        print("Data index : ", k)
        print("weights : ", a)
        print("Data point : ", np.array(data3[k]))
        dot_product = np.dot(a, data3[k])
        print("The dot product is : ", dot_product)
        if(dot_product <= 0):            
            a = a + learning_rate * data3[k]
            missclasified_vectors = True
        k = (k + 1) % (len(data1))
    print("weights are : ", a)
    x_vec = np.linspace(0, 10, 5)
    y_vec = ((a[1] * x_vec) + a[0])/a[2]
    y_vec = -y_vec   
    plt.plot(x_vec, y_vec, 'b--')


    plt.show()

z = []
data = []
alpha = []
c = 10
# def non_linearly_seperable_func(alpha):
#     global c
#     value = -func(alpha)
#     for i in range(len(alpha)):
#         value -= (1/(2 * c)) * (alpha[i] ** 2)
#     return (-value)



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
    global alpha
    global w1
    global w2
    global data
    z = np.concatenate([np.ones(50), -np.ones(100)], axis = 0)
    print(len(z))
    data1 = np.concatenate([w1, w2, w3], axis = 0)
    data2 = np.concatenate([w3, w1, w2])
    # print("data : ", data1)
    max_solution = 0
    f, ax = plt.subplots(figsize=(7, 7))
    c1, c2 = "#3366AA", "#AA3333"
    for j in range(2):
        if(j == 0):
            data = data1
        else:
            data = data2
        consrt = {'type' : 'eq', 'fun' : constraint}
        alpha = np.zeros(len(data))
        print(len(alpha))
        if(j == 0):
            c = None
        else:
            c = 100
        b = (0.0000000000, c)
        bound = [b] * len(data)
        print(len(bound))
        sol = minimize(func, alpha, method = 'SLSQP', constraints = consrt, bounds = bound)
        print(sol)
        alpha = sol.x

        print("lagrange multiplier are : ", alpha)

        a = np.zeros(len(data[0]))
        for i in range(len(data)):
            a += alpha[i]*z[i]*data[i]
        if(j == 1):
            error = alpha / c
        else:
            error = np.zeros(len(alpha)) 
        bias = []                                          #finding the points that pass through the w.x + b = +/- 1
        for i in range(len(alpha)):
            for k in range(len(alpha)):
                if(i == k):
                    pass
                else:
                    if(abs(0.5 * (alpha[i] * alpha[k] * z[i] * z[k] * (data[i].T.dot(data[k])))) > 0.0001):
                        bias.append((1 - error[i])/z[i] - a.T.dot(data[i]))
                        
        bias = np.array(bias).mean()
        print("bias is ", bias)
        print("weight vector is : ", a)
        a = [bias, a[0] , a[1]] 
        if(j == 0):
            x_vec = np.linspace(1, 8, 5)
        else:
            x_vec = np.linspace(3, 8, 5)

        y_vec = ((a[1] * x_vec) + a[0])/a[2]
        y_vec = -y_vec
        if(j == 0):
            plt.plot(x_vec, y_vec, 'r--')
        else:
            plt.plot(x_vec, y_vec, 'b--')
        y_vec = y_vec + (1 / a[2])
        plt.plot(x_vec, y_vec, 'g--')
        y_vec = y_vec - (2/ a[2])
        plt.plot(x_vec, y_vec, 'g--')
        
    ax.scatter(*w1.T, c=c1,s = 10, label = "w1")
    ax.legend()
    ax.scatter(*w2.T, c=c2,s = 10, marker="D", label = "w2")
    ax.legend()
    ax.scatter(*w3.T, c='m',s = 10, marker="x", label = "w3")
    ax.legend()

    plt.show()


#  [ 3.33329562 -0.9517713 ]


if(__name__ == "__main__"):
    data_processing()
    perceptron()()
    svm()