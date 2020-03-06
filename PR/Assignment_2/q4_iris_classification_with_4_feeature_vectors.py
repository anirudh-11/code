#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def discriminant_function(x, covariance, mean):
    g = (0.5) * (-(x - mean).dot(np.linalg.inv(covariance).dot((x - mean).T)) - np.log(np.linalg.det(covariance)))
    return(g)

def main():
    data = pd.read_csv("iris.csv")
    variety = data['variety'].unique()
    column = data.columns
    setosa_train, t1 = train_test_split(data[0 : 50], test_size=0.2)
    versicolor_train, t2 = train_test_split(data[51 : 100], test_size=0.2)
    virginica_train, t3 = train_test_split(data[101 : 150], test_size=0.2)
    frames = [t1, t2, t3]
    test = pd.concat(frames)
    print("setosa train : \n{}\nversicolor : \n{}\nvirginica : \n{}\n, test : \n{}\n".format(setosa_train, versicolor_train, virginica_train, test))
    print(data.describe())
    setosa_mean = np.mean(setosa_train, axis = 0)
    versicolor_mean = np.mean(versicolor_train, axis = 0)
    virginica_mean = np.mean(virginica_train, axis = 0)
    print(column)
    print("setosa_mean : \n{}\nversicolor_mean : \n{}\nvirginica_mean : \n{}\n".format(setosa_mean, virginica_mean, versicolor_mean))
    setosa_z = np.array([list(map((lambda num : num -  setosa_mean[0]), setosa_train[column[0]].tolist())), list(map((lambda num : num -  setosa_mean[1]), setosa_train[column[1]].tolist())), list(map((lambda num : num -  setosa_mean[2]), setosa_train[column[2]].tolist())), list(map((lambda num : num -  setosa_mean[3]), setosa_train[column[3]].tolist()))])
    virginica_z = np.array([list(map((lambda num : num -  virginica_mean[0]), virginica_train[column[0]].tolist())), list(map((lambda num : num -  virginica_mean[1]), virginica_train[column[1]].tolist())), list(map((lambda num : num -  virginica_mean[2]), virginica_train[column[2]].tolist())), list(map((lambda num : num -  virginica_mean[3]), virginica_train[column[3]].tolist()))])
    versicolor_z = np.array([list(map((lambda num : num -  versicolor_mean[0]), versicolor_train[column[0]].tolist())), list(map((lambda num : num -  versicolor_mean[1]), versicolor_train[column[1]].tolist())), list(map((lambda num : num -  versicolor_mean[2]), versicolor_train[column[2]].tolist())), list(map((lambda num : num -  versicolor_mean[3]), versicolor_train[column[3]].tolist()))])
    print("setosa_z : \n{}\nversicolor_z : \n{}\nvirginia_z : \n{}\n".format(setosa_z, versicolor_z, virginica_z))

    setosa_covariance = (1/39) * (setosa_z.dot(setosa_z.T))
    versicolor_covariance = (1/39) * (versicolor_z.dot(versicolor_z.T))
    virginica_covariance = (1/39) * (virginica_z.dot(virginica_z.T))
    print("setosa_covariance : \n{}\nversicolor_covariance : \n{}\nvirginia_covariance : \n{}\n".format(setosa_covariance, versicolor_covariance, virginica_covariance))

    count = 0

    for index, row in test.iterrows():
        test_vector = np.array([row[0], row[1], row[2], row[3]])
        
        g1 = discriminant_function(test_vector, setosa_covariance, setosa_mean)
        g2 = discriminant_function(test_vector, versicolor_covariance, versicolor_mean)
        g3 = discriminant_function(test_vector, virginica_covariance, virginica_mean)

        

        print(g1, g2, g3)
        if(g1 > g2 and g1 > g3):
            if(row[4] == 'Setosa'):
                count = count + 1
            print("setosa")
        elif(g2 > g3):
            if(row[4] == 'Versicolor'):
                count = count + 1

            print("versicolor")
        else:
            if(row[4] == 'Virginica'):
                count = count + 1
            print("virginica")

    print("Accuracy is : ", count / 30)


if(__name__ == "__main__"):
    main()

# %%
