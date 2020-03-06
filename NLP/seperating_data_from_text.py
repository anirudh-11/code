import spacy
from spacy.symbols import appos
#from spacy.symbols import compound, appos, mummod, ROOT
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp('''Vardar was the eventual name of a Sava-class river monitor, originally built for the Austro-Hungarian Navy as SMS Bosna, that went into service on 9 July 1915. During World War I she fought the Serbian Army, the Romanian Navy and Army, and the French Army. After briefly serving with the Hungarian People's Republic at the end of the war, she was transferred to the newly created Kingdom of Serbs, Croats and Slovenes (later Yugoslavia), and renamed Vardar. She remained in service throughout the interwar period. During the first few days of the German-led Axis invasion of Yugoslavia in April 1941, she laid mines in the Danube near the Romanian border as the flagship of the 1st Monitor Division. She fought off several attacks by the Luftwaffe, but was forced to withdraw to Belgrade. Due to high river levels and low bridges, navigation became difficult, and she was scuttled on 11 April by her crew, who were later killed or captured. roll number student name student age father age student depart COE17B019 Anirudh Srinivasan 19 50 Comp_Science COE17B018 Kavin Raaj 19 55 Comp_Science This is the most beautiful day of my life The world is full of surprises COE17B001 Arvind 22 55 Mechanical Chesma (Russian: Чесма, also transliterated Tchésma) was the second ship of the Ekaterina II-class battleships built for the Imperial Russian Navy in the 1880s. Named after the Russian victory at the Battle of Chesma in 1770, she was built by the Russian Steam Navigation Company at Sevastopol. When the ship was completed, she proved to be very overweight, which meant that much of her waterline armor belt was submerged. She served in the Black Sea Fleet until she was turned over to the Sevastopol port authorities and decommissioned in 1907. This picture is a chromolithograph print of Chesma, dated 1892; it is now in the collection of the Bibliothèque nationale de France. Company Contact Country Alfreds Futterkiste Maria Anders Germany Centro comercial Moctezuma Francisco Chang Mexico Ernst Handel Roland Mendel Austria''')
#doc = nlp('Aniuddh Srinivasan')
sentences = list(doc.sents)
for ele in sentences:    
  print(ele)
  
required_relation = [7037928807040764755, 403, 8206900633647566924, 12837356684637874264, 439, 440, 402, 416]
flag = 0
data = []

def ret_cont_data(sent):
    start = -1
    end = 0
    i = 0
    while(i < len(sent)):
        if(start == -1 and sent[i].dep in required_relation):
            start = i
            end = i
        elif(sent[i].dep in required_relation and end == i - 1 ):
            end = end + 1
        i = i + 1
    start, end = data_check(start, end, sent)
    return(start, end)

def data_check(start, end, sent):
    flag = 0
    i = start - 1
    while(i > -1):
        j = end + 1
        while(j < len(sent)):
            if((not (sent[i].dep in required_relation and sent[i].head == sent[j]) or (sent[j].head == sent[i] and sent[j].dep in required_relation))):
                flag = 1
                break
            j = j + 1
        i = i - 1
        if(flag == 1):
            break
    if(flag != 0):
        start = end + 1
    return(start, end)



for sentence in sentences:
    for ele in sentence:
        #print(ele, ele.dep, ele.dep_)
        if(not ele.dep in required_relation):
            flag = 1 
            break 
    if(flag == 0):
        data.append(sentence)
    else:
        start, end = ret_cont_data(sentence)
        i = start
        while(i <= end):
            data.append(sentence[i])
            i = i + 1
        flag = 0

   
print("\nThe data sentences are : ")

for dat in data:
    print(dat)