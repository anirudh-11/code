import spacy 
import re
import string
nlp = spacy.load('en')
#nlp1 = spacy.load('en_core_web_lg')
txt = 'Roll no Student name Age Father age coe17b019 Anirudh 19 55 coe17b020 Ravi 20 61'
doc = nlp("roll_no st_name st_age father_age st_depart. COE17B019 Anirudh Srinivasan 19 50 Comp_Science.  COE17B012 Kavin Raaj 19 55 Comp_Science. This is the most beautiful day of my life. The world is full of surprises.  COE17B001 Arvind 22 55 Mechanical.")

for token in doc:
    print(token)


tokens = []

for token in doc:
    if(not token.is_punct and token.pos_ != 'VERB'):
        tokens.append(token.text)

i=0
for a in tokens:
    if(not a.isalnum() and len(a) == 1):
        del(tokens[i])
    i=i+1

#doc1 = nlp1(txt)
#for token in doc1:
#    for token1 in doc1:
#       print(token.text, token1.text, token.similarity(token1))

 
i = 0 
sum = 0
frequency_list = []
for a in tokens:
    for b in tokens:
        if(a == b):
            sum = sum + 1
    frequency_list.append(sum)
    sum = 0
    i = i + 1

print(tokens)
print(frequency_list)

i = 0
heading = []
for a in frequency_list:
    if(a > max(frequency_list) - 2):
        heading.append(tokens[i])
    i = i + 1
   
print(set(heading))

heading = list(set(heading))

i = 0
values = []
for a in tokens:
    if(a in heading):
        values.append(tokens[i])
    i = i + 1

for chunk in doc.noun_chunks:
    print(chunk.text, chunk.root.text, chunk.root.dep_,
            chunk.root.head.text)

print(values)