import pandas as pd
import numpy as np
import fim
# from mlxtend.preprocessing import TransactionEncoder
# from mlxtend.frequent_patterns import apriori, association_rules  

data = pd.read_csv(r'cleaned_data.csv')
print(data.head())
print(data.shape)
data_list = data.values
print(data.values)

def mfi(data):
    print("Using relim for mfi : ")
    freq_list = fim.relim(tracts = data, target = 'm', supp = 5)
    print("The frequent item list is : ")
    print(freq_list)

    print("Using ista for mfi : ")
    freq_list = fim.ista(tracts = data, target = 'm', mode = 'z', algo = 'p',supp = 5)
    print("The frequent item list is : ")
    print(freq_list)

def cfi(data):
    print("Using relim for cfi : ")
    freq_list = fim.relim(tracts = data, target = 'c', supp = 5)
    print("The frequent item list is : ")
    print(freq_list)

    print("Using ista for cfi : ")
    freq_list = fim.ista(tracts = data, target = 'c', algo = 'p',supp = 5)
    print("The frequent item list is : ")
    print(freq_list)

def fi(data):
    print("Using apriori for fim : ")
    freq_list = fim.apriori(tracts = data, supp = 5)
    print("The frequent item list is : ")
    print(freq_list)
    rules = fim.apriori(tracts = data, target = 'r', eval = 'c', report = 'c')
    print("The rules are : ")
    print(rules)
    rules = fim.apriori(tracts = data, target = 'r', eval = 'l', report = 'l')
    print("The rules are (evaluated with lift): ")
    print(rules)
    print("lfi using apriori : ")
    lfi(freq_list)



    print("Using fp-growth for fim : ")
    freq_list = fim.fpgrowth(tracts = data, supp = 5)
    print("The frequent item list is : ")
    print(freq_list)
    rules = fim.fpgrowth(tracts = data, target = 'r', eval = 'c', report = 'c', conf = 60)
    print("The rules are (evaluated with confidence): ")
    print(rules)
    rules = fim.fpgrowth(tracts = data, target = 'r', eval = 'l', report = 'l',  conf = 60)
    print("The rules are (evaluated with lift): ")
    print(rules)

    print("lfi using fpgrowth is : ")
    lfi(freq_list)



def lfi(freq_list):
    len_of_freq_list = [len(ele) for ele in freq_list]
    lfi = freq_list[len_of_freq_list.index(max(len_of_freq_list))]
    print("lfi is : ")
    print(lfi)
    

mfi(data_list)
cfi(data_list)
fi(data_list)