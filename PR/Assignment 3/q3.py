import cv2
import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from scipy.optimize import minimize

w1 = []
w2 = []

def main():
    global w1
    global w2
    data = []
    for i in range(1, 15):
        img = cv2.imread('poly{}.png'.format(i))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
        img[thresh == 255] = 0                                              #converting black pixels to white
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))       
        myimg = cv2.erode(img, kernel, iterations = 1)
        avg_color_per_row = np.average(myimg, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        cv2.imshow("poly{}.png, {}".format(i, avg_color), myimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        if(i < 8):
            w1.append([avg_color[1], avg_color[2]])
            data.append([1, avg_color[1], avg_color[2]])
        else:
            w2.append([avg_color[1], avg_color[2]])
            data.append([-1, -avg_color[1], -avg_color[2]])
        print(avg_color)
    w1 = np.array(w1)
    w2 = np.array(w2)
    data = np.array(data)
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
        print("Data point : ", np.array(data[k]))
        dot_product = np.dot(a, data[k])
        print("The dot product is : ", dot_product)
        if(dot_product <= 0):            
            a = a + learning_rate * data[k]
            missclasified_vectors = True
        k = (k + 1) % (len(data))
    print("weights are : ", a)
    f, ax = plt.subplots(figsize=(7, 7))
    c1, c2, c3 = "#3366AA", "#AA3333", 'm'
    ax.scatter(*w1.T, c=c1,s = 10, label = "w1")
    ax.legend()
    ax.scatter(*w2.T, c=c2, marker="D", label = "w2")
    ax.legend()

    x_vec = np.linspace(0, 20, 5)
    y_vec = ((a[1] * x_vec) + a[0])/a[2]
    y_vec = -y_vec   
    plt.plot(x_vec, y_vec, 'g--')
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
    global w1
    global w2
    z = np.array([1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1])
    data = np.concatenate([w1, w2], axis = 0)
    print("data : ", data)
    max_solution = 0
    consrt = {'type' : 'eq', 'fun' : constraint}
    alpha = np.zeros(len(data))
    b = (0.0000000000, None)
    bound = [b, b, b, b, b, b, b, b, b, b, b, b, b, b] 
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
                if(abs(0.5 * (alpha[i] * alpha[j] * z[i] * z[j] * (data[i].T.dot(data[j])))) > 0.0001):
                    bias.append(1/z[i] - a.T.dot(data[i]))
                    
    bias = np.array(bias).mean()
    print("bias is ", bias)
    print("weight vector is : ", a)
    a = [bias, a[0] , a[1]] 
    f, ax = plt.subplots(figsize=(7, 7))
    c1, c2 = "#3366AA", "#AA3333"

    x_vec = np.linspace(0, 20, 5)
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
   

if(__name__ == "__main__"):
    main()
    svm()