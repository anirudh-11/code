import pandas as pd 
from tqdm import tqdm
from random import seed
from random import random

def getUniqueWords(allWords) :
	uniqueWords = [] 
	for i in allWords:
		if not i in uniqueWords:
			uniqueWords.append(i)
	return uniqueWords

def ListToWords(ListofSent):
	ListofWords = []
	for sentence in ListofSent:
		list1 = sentence.split(' ')
		for word in list1:
			ListofWords.append(word)
	return ListofWords 

def Generating_FV(IP_List,Unique_words):
	ListofFV = []
	for sentence in tqdm(IP_List):
		list1 = sentence.split(' ')
		list2 = [0] * len(Unique_words)
		for word1 in list1:
			i = 0
			for word2 in Unique_words:
				if word1 == word2:
					list2[i] += 1 
				i = i+1 
		ListofFV.append(list2)
	return ListofFV

def Output_Add(FV,Target):
	i = 0
	for fv in FV:
		if Target[i] == "ham":
			fv.append(0)
		else:
			fv.append(1)
		i = i+1
	return FV
Dataset = pd.read_csv('spam.csv')
#print(Dataset)
Emails = Dataset['v2'].tolist()
Target = Dataset['v1']
print(Target[0])
Emails_words = ListToWords(Emails)
print(len(Emails_words))
Unique_words = getUniqueWords(Emails_words)
print(len(Unique_words))
FV = Generating_FV(Emails,Unique_words)
print(len(FV))
FV = Output_Add(FV,Target)
print(FV[0])
