import spacy 
import re
import string
nlp = spacy.load('en')
#nlp1 = spacy.load('en_core_web_lg')
txt = 'Roll no Student name Age Father age coe17b019 Anirudh 19 55 coe17b020 Ravi 20 61'
doc = nlp("roll_no st_name st_age father_age st_depart. COE17B019 AnirudhSrinivasan 19 50 Comp_Science. COE17B018 KavinRaaj 19 55 Comp_Science. This is the most beautiful day of my life. The world is full of surprises. COE17B001 Arvind 22 55 Mechanical.")

sentences = list(doc.sents)
print(sentences)
tokens = []

i = 0
for sentence in sentences:
   for token in sentence:  
     if(token.pos_ == 'VERB' or token.pos_ == 'AUX' or token.pos_ == 'ADV'):
        del sentences[i]
   i = i + 1
i=0
print(sentences)

#doc1 = nlp1(txt)
#for token in doc1:
#    for token1 in doc1:
#       print(token.text, token1.text, token.similarity(token1))

heading = []
for token in sentences[0]:
    if(not token.is_punct):
        heading.append(token.text)
    i = i + 1
   
print(heading)
a = sentences
sentences = []
i = 0
n = []
for sentence in a:
    for token in sentence:
        if(not (token.is_punct and len(token.text) == 1)):
            n.append(token)
    sentences.append(n)
    n = []



#for sentence in sentences:
#    for token in sentence:
#        if((token.pos_ == 'PROPN' and sentence[i + 1].pos_ == 'PROPN') or (token.pos_ == 'NOUN' and sentence[i + 1].pos_ == 'NOUN')):
#            token.text = token.text + sentence[i+1].text
#            print(token.text, token.pos_)
#            sentence[i + 1].text = " "
#        print(token.text, token.ent_type_, token.pos_)
#    i = i + 1

values = []
value = []
i = 1
print(len(sentences))
l1 = len(heading)

def ner(text):
    txt = nlp(text)
    return(txt.ents.label_)

def name(text):
    first_char = text[0]
    rest = text[1:len(text)]
    if(first_char.isupper and rest.islower):
            return(1)
    else:
        return(0)

skip = 0
val = []
while(i < len(sentences)):
    skip = 0    
    if(len(sentences[i]) == len(heading)):
        for token in sentences[i]:
            value.append(token)
        values.append(value)

    elif(len(sentence) < len(heading)):
        if(values != []):
            l2 = len(sentences[i])
            j = 0
            for token in sentences[i]:
                k = j - 5
                if(skip == l1 - l2):
                        value = {heading[k]  : token}
                        val.append(value)
                        j = j + 1
                
                else:
                    j = 0
                    while(j < l1):
                        value = {}
                        if(token.is_alpha == values[0][j].is_alpha == True):
                         if(name(token.text) == name(values[0][j].text) == True):
                             value = {heading[j] : token}
                         elif(ner(token.text) == ner(values[0][j].text)):
                             value = {heading[j] : token}
                    
                        elif(token.like_num == values[0][j].like_num == True):
                            value = {heading[j]  : token}

                        elif(token.shape_ == values[0][j].shape_):
                            value = {heading[j]  : token}

                        if(value == {}):
                            skip = skip + 1
                        else:
                            val.append(value)
                            j = j + 5
                        j = j + 1
    values.append(val)
    val = []
    i = i + 1
#for token in sentences[1]:
#     print(values)
print(values)