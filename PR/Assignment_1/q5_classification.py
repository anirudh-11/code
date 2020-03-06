# %%

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    data = pd.read_csv("iris.csv")
    variety = data['variety'].unique()
    column = data.columns

    test_case_1 = data[[column[2], column[3]]][0 : 1].copy()
    test_case_2 = data[[column[2], column[3]]][50 : 51].copy()
    test_case_3 = data[[column[2], column[3]]][100 : 101].copy()

    setosa = data[column][1 : 50].copy()
    versicolor = data[column][51 : 100].copy()
    virginica = data[column][101 : 150].copy()
    
    setosa_petal_length_mean = setosa[column[2]].mean()
    setosa_petal_width_mean = setosa[column[3]].mean()

    versicolor_petal_length_mean = versicolor[column[2]].mean()
    versicolor_petal_width_mean = versicolor[column[3]].mean()

    virginica_petal_length_mean = virginica[column[2]].mean()
    virginica_petal_width_mean = virginica[column[3]].mean()
    
    setosa_z = np.array([list(map((lambda num : num -  setosa_petal_length_mean), setosa[column[2]].tolist())), list(map((lambda num : num -  setosa_petal_width_mean), setosa[column[3]].tolist()))])
    versicolor_z = np.array([list(map((lambda num : num -  versicolor_petal_length_mean), versicolor[column[2]].tolist())), list(map((lambda num : num -  versicolor_petal_width_mean), versicolor[column[3]].tolist()))])
    virginica_z = np.array([list(map((lambda num : num -  virginica_petal_length_mean), virginica[column[2]].tolist())), list(map((lambda num : num -  virginica_petal_width_mean), virginica[column[3]].tolist()))])
    
    setosa_covariance =  (1 / 48) * setosa_z.dot(setosa_z.transpose())
    versicolor_covariance = (1 / 48) * versicolor_z.dot(versicolor_z.transpose())
    virginica_covariance = (1 / 48) * virginica_z.dot(virginica_z.transpose())

    setosa_dist_1 = np.array([test_case_1[column[2]].tolist()[0] - setosa_petal_length_mean, test_case_1[column[3]].tolist()[0] - setosa_petal_width_mean]).transpose().dot(np.linalg.inv(setosa_covariance).dot(np.array([test_case_1[column[2]].tolist()[0] - setosa_petal_length_mean, test_case_1[column[3]].tolist()[0] - setosa_petal_width_mean])))
    versicolor_dist_1 = np.array([test_case_1[column[2]].tolist()[0] - versicolor_petal_length_mean, test_case_1[column[3]].tolist()[0] - versicolor_petal_width_mean]).transpose().dot(np.linalg.inv(versicolor_covariance).dot(np.array([test_case_1[column[2]].tolist()[0] - versicolor_petal_length_mean, test_case_1[column[3]].tolist()[0] - versicolor_petal_width_mean])))
    virginica_dist_1 = np.array([test_case_1[column[2]].tolist()[0] - virginica_petal_length_mean, test_case_1[column[3]].tolist()[0] - virginica_petal_width_mean]).transpose().dot(np.linalg.inv(virginica_covariance).dot(np.array([test_case_1[column[2]].tolist()[0] - virginica_petal_length_mean, test_case_1[column[3]].tolist()[0] - virginica_petal_width_mean])))

    setosa_dist_2 = np.array([test_case_2[column[2]].tolist()[0] - setosa_petal_length_mean, test_case_2[column[3]].tolist()[0] - setosa_petal_width_mean]).transpose().dot(np.linalg.inv(setosa_covariance).dot(np.array([test_case_2[column[2]].tolist()[0] - setosa_petal_length_mean, test_case_2[column[3]].tolist()[0] - setosa_petal_width_mean])))
    versicolor_dist_2 = np.array([test_case_2[column[2]].tolist()[0] - versicolor_petal_length_mean, test_case_2[column[3]].tolist()[0] - versicolor_petal_width_mean]).transpose().dot(np.linalg.inv(versicolor_covariance).dot(np.array([test_case_2[column[2]].tolist()[0] - versicolor_petal_length_mean, test_case_2[column[3]].tolist()[0] - versicolor_petal_width_mean])))
    virginica_dist_2 = np.array([test_case_2[column[2]].tolist()[0] - virginica_petal_length_mean, test_case_2[column[3]].tolist()[0] - virginica_petal_width_mean]).transpose().dot(np.linalg.inv(virginica_covariance).dot(np.array([test_case_2[column[2]].tolist()[0] - virginica_petal_length_mean, test_case_2[column[3]].tolist()[0] - virginica_petal_width_mean])))

    setosa_dist_3 = np.array([test_case_3[column[2]].tolist()[0] - setosa_petal_length_mean, test_case_3[column[3]].tolist()[0] - setosa_petal_width_mean]).transpose().dot(np.linalg.inv(setosa_covariance).dot(np.array([test_case_3[column[2]].tolist()[0] - setosa_petal_length_mean, test_case_3[column[3]].tolist()[0] - setosa_petal_width_mean])))
    versicolor_dist_3 = np.array([test_case_3[column[2]].tolist()[0] - versicolor_petal_length_mean, test_case_3[column[3]].tolist()[0] - versicolor_petal_width_mean]).transpose().dot(np.linalg.inv(versicolor_covariance).dot(np.array([test_case_3[column[2]].tolist()[0] - versicolor_petal_length_mean, test_case_3[column[3]].tolist()[0] - versicolor_petal_width_mean])))
    virginica_dist_3 = np.array([test_case_3[column[2]].tolist()[0] - virginica_petal_length_mean, test_case_3[column[3]].tolist()[0] - virginica_petal_width_mean]).transpose().dot(np.linalg.inv(virginica_covariance).dot(np.array([test_case_3[column[2]].tolist()[0] - virginica_petal_length_mean, test_case_3[column[3]].tolist()[0] - virginica_petal_width_mean])))

    ax = sns.scatterplot(x = setosa[column[2]], y = setosa[column[3]], marker = '+', label = 'setosa')
    sns.scatterplot(x = versicolor[column[2]], y = versicolor[column[3]], marker = 'x', label = 'versicolor')
    sns.scatterplot(x = virginica[column[2]], y = virginica[column[3]], label w= 'virginica')

    sns.scatterplot(x = test_case_1[column[2]], y = test_case_1[column[3]], marker = 'o', color = 'r', label = 'test_case_1')
    sns.scatterplot(x = test_case_2[column[2]], y = test_case_2[column[3]], marker = 'o', color = 'b', label = 'test_case_2')
    sns.scatterplot(x = test_case_3[column[2]], y = test_case_3[column[3]], marker = 'o', color = 'k', label = 'test_case_3')
    

    ax.legend()

    dist_1 = [setosa_dist_1, versicolor_dist_1, virginica_dist_1]
    dist_2 = [setosa_dist_2, versicolor_dist_2, virginica_dist_2] 
    dist_3 = [setosa_dist_3, versicolor_dist_3, virginica_dist_3]

    classes = {0 : 'setosa', 1 : 'versicolor', 2 : 'virginica'}

    print("mean petal length and width of setosa is {}, {}".format(setosa_petal_length_mean, setosa_petal_width_mean))
    print("mean petal length and width of versicolor is {}, {}".format(versicolor_petal_length_mean, versicolor_petal_width_mean))
    print("mean petal length and width of virginica is {}, {}\n".format(virginica_petal_length_mean, virginica_petal_width_mean))

    print("class of testcase 1\n{}\n is : {}\n\nclass of testcase 2\n{}\n is : {}\n\nclass of testcase 3\n{}\n is {}".format(test_case_1, classes[dist_1. index(min(dist_1))], test_case_2, classes[dist_2. index(min(dist_2))], test_case_3, classes[dist_3. index(min(dist_3))]))
    
    print([setosa_dist_1, versicolor_dist_1, virginica_dist_1])
    print([setosa_dist_2, versicolor_dist_2, virginica_dist_2])
    print([setosa_dist_3, versicolor_dist_3, virginica_dist_3])
    
    
    plt.show()
    # print(test_case_1)
    # print(data[[column[2], column[3]]][0 : 1])



if(__name__ == "__main__"):
    main()

# %%
