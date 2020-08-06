import pandas as pd 
from sklearn.naive_bayes import GaussianNB 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import numpy as np
import itertools


def read_data():
    data = pd.read_csv(r'F:\Docs\Big data\Data_Sets\adult.csv')
    print(data.head())
    return(data)

def pre_processing(data):
    categorical_att = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'gender', 'native-country', 'income']
    for att in categorical_att:
        mode = data[att].mode()[0]
        data[att].replace(['?'], mode, inplace = True)

    for att in categorical_att:
        if(att == 'income'):
            pass 
        else:   
            one_hot = pd.get_dummies(data[att])
            data = data.drop(att, axis = 1)
            data = data.join(one_hot)

    print(data.head())
    return(data)

def gaussian_nb(data_train, data_test, target_train, target_test):
    print("fitting with gaussian naive bayes ... ")
    gnb = GaussianNB().fit(data_train, target_train) 
    gnb_predictions = gnb.predict(data_test) 
    
    accuracy = gnb.score(data_test, target_test) 
    print("The accuracy of the model is : ", accuracy) 
    cm = confusion_matrix(target_test, gnb_predictions) 
    print("The confusion matrix is : ")
    print(cm)

def decision_tree(data_train, data_test, target_train, target_test):
    print("fitting with decision tree of depth 2 ... ")
    dtree_model = DecisionTreeClassifier(max_depth = 5).fit(data_train, target_train) 
    dtree_predictions = dtree_model.predict(data_test) 

    accuracy = dtree_model.score(data_test, target_test) 
    print("The accuracy of the model is : ", accuracy) 
    cm = confusion_matrix(target_test, dtree_predictions) 
    print("The confusion matrix is : ")
    print(cm)

def main():
    data = read_data()
    processed_data = pre_processing(data)
    features = list(set(processed_data.columns) - {'income'})
    target = 'income'
    
    data_train, data_test, target_train, target_test = train_test_split(processed_data[features], processed_data[target], test_size = 0.66)
    gaussian_nb(data_train, data_test, target_train, target_test)
    decision_tree(data_train, data_test, target_train, target_test)

if(__name__ == '__main__'):
    main()