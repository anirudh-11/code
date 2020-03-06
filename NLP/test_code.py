import spacy
#from spacy.symbols import compound, appos, mummod, ROOT
from spacy import displacy
import string

nlp = spacy.load("en_core_web_sm")
doc = nlp('''Vardar was the eventual name of a Sava-class river monitor, originally built for the Austro-Hungarian Navy as SMS Bosna, that went into service on 9 July 1915. During World War I she fought the Serbian Army, the Romanian Navy and Army, and the French Army. After briefly serving with the Hungarian People's Republic at the end of the war, she was transferred to the newly created Kingdom of Serbs, Croats and Slovenes (later Yugoslavia), and renamed Vardar. She remained in service throughout the interwar period. During the first few days of the German-led Axis invasion of Yugoslavia in April 1941, she laid mines in the Danube near the Romanian border as the flagship of the 1st Monitor Division. She fought off several attacks by the Luftwaffe, but was forced to withdraw to Belgrade. Due to high river levels and low bridges, navigation became difficult, and she was scuttled on 11 April by her crew, who were later killed or captured. roll_no st_name st_age father_age st_depart COE17B019 Anirudh 19 50 Compscience COE17B018 Kavin 19 55 Compscience This is the most beautiful day of my life. The world is full of surprises. COE17B001 Arvind 22 55 Mechanical Chesma (Russian: Чесма, also transliterated Tchésma) was the second ship of the Ekaterina II-class battleships built for the Imperial Russian Navy in the 1880s. Named after the Russian victory at the Battle of Chesma in 1770, she was built by the Russian Steam Navigation Company at Sevastopol. When the ship was completed, she proved to be very overweight, which meant that much of her waterline armor belt was submerged. She served in the Black Sea Fleet until she was turned over to the Sevastopol port authorities and decommissioned in 1907. This picture is a chromolithograph print of Chesma, dated 1892; it is now in the collection of the Bibliothèque nationale de France. Company Contact Country Alfredsfutterkiste Mariaanders Germany Centromoctezuma Francisc Mexico Ernsthandel Rolandmendel Austria The world is beautiful.''')
#doc = nlp('roll_no st_name st_no coe17b019 Anirudh 925632145 coe17b018 Kavin 9203827384')
#doc = nlp('roll_no st_name st_no coe17b019 Anirudh 925632145 coe17b018 Kavin 9203827384 coe17b043 Arvind 9203928237 coe17b012 Baeax 9302932023 coe29b048 Harax 9847382938')
doc = nlp('roll_no st_name st_no COE17B019 Anirudh 925632145 COE17B018 Kavin 9203827384 COE17B043 Arvind 9203928237 COE17B012 Baeax COE17B022 Harax 9847382938')
doc = nlp("""
Investments_in_securities, at_fair_value Accounts_receivable Prepaid_expenses Income_tax_receivable Total_current_assets
$	217,185
73,875 32,319,410 3,194,242 511,773
36,316,485
$	217,185
73,875 32,319,410 3,194,242 511,773
36,316,485
$	217,185
73,875 32,319,410 3,194,242 511,773
36,316,485
$	217,185
73,875 32,319,410 3,194,242 511,773
36,316,485
$	217,185
73,875 32,319,410 3,194,242 511,773
36,316,485

Investments_in_joint_ventures, equipment_software_and_leasehold_improvements, net_Other_assets Total_assets
921,206
1,682,676
745,226
$ 39,665,593
921,206
1,682,676
745,226
$ 39,665,593

921,206
1,682,676
745,226
$ 39,665,593
921,206
1,682,676
745,226
$ 39,665,593
921,206
1,682,676
745,226
$ 39,665,593

Liabilities and stockholders’ equity
Current liabilities:
Accounts_payable_and_accrued_expenses Income_tax_payable Deferred_tax_liability Total_current_liabilities
$ 5,085,280 150,568 6,951,267
12,187,115
$ 5,085,280 150,568 6,951,267
12,187,115

$ 5,085,280 150,568 6,951,267
12,187,115

$ 5,085,280 150,568 6,951,267
12,187,115

$ 5,085,280 150,568 6,951,267
12,187,115

Other_liabilities Total_liabilities
471,507
12,658,622
471,507
12,658,622
471,507
12,658,622
471,507
12,658,622

Stockholders’ equity:
Common stock, at $1.00 par value; authorized, 2,000,000 shares;
issued and outstanding, 88,303 shares Additional_paid_in_capital Retained_earnings
Accumulated_other_comprehensive_gain Total_stockholders’_equity Total_liabilities_and_stockholders’_equity
88,303
703,699
26,039,138
175,831
27,006,971
$ 39,665,593
88,303
703,699
26,039,138
175,831
27,006,971
$ 39,665,593
88,303
703,699
26,039,138
175,831
27,006,971
$ 39,665,593
88,303
703,699
26,039,138
175,831
27,006,971
$ 39,665,593
 """)

# doc = nlp(""" Assets 2016 2017
# Current assets:
# Cash
# Investments in securities, at fair value Accounts receivable Prepaid expenses Income tax receivable Total current assets
# $	217,185
# 73,875 32,319,410 3,194,242 511,773
# 36,316,485
# Investments in joint ventures, equity method Property, equipment, software, and leasehold improvements, net Other assets Total assets
# 921,206
# 1,682,676
# 745,226
# $ 39,665,593
# Liabilities and stockholders’ equity
# Current liabilities:
# Accounts payable and accrued expenses Income tax payable Deferred tax liability Total current liabilities
# $ 5,085,280 150,568 6,951,267
# 12,187,115
# Other liabilities Total liabilities
# 471,507
# 12,658,622
# Stockholders’ equity:
# Common stock, at $1.00 par value; authorized, 2,000,000 shares;
# issued and outstanding, 88,303 shares Additional paid-in capital Retained earnings
# Accumulated other comprehensive gain Total stockholders’ equity Total liabilities and stockholders’ equity
# 88,303
# 703,699
# 26,039,138
# 175,831
# 27,006,971
# $ 39,665,593
# """)

# doc = nlp('roll_no st_name st_no COE17B019 Anirudh 925632145 COE17B018 Kavin 9203827384 COE17B043 Arvind 9203928237 COE17B012 Baeax COE17B022 Harax 9847382938')
# doc = nlp('''Vardar was the eventual name of a Sava-class river monitor, originally built for the Austro-Hungarian Navy as SMS Bosna, that went into service on 9 July 1915. During World War I she fought the Serbian Army, the Romanian Navy and Army, and the French Army. After briefly serving with the Hungarian People's Republic at the end of the war, she was transferred to the newly created Kingdom of Serbs, Croats and Slovenes (later Yugoslavia), and renamed Vardar. She remained in service throughout the interwar period. During the first few days of the German-led Axis invasion of Yugoslavia in April 1941, she laid mines in the Danube near the Romanian border as the flagship of the 1st Monitor Division. She fought off several attacks by the Luftwaffe, but was forced to withdraw to Belgrade. Due to high river levels and low bridges, navigation became difficult, and she was scuttled on 11 April by her crew, who were later killed or captured. roll_no st_name st_age father_age st_depart COE17B019 Anirudh 19 50 Compscience COE17B018 Kavin 19 55 Compscience This is the most beautiful day of my life. The world is full of surprises. COE17B001 Arvind 22 55 Mechanical Chesma (Russian: Чесма, also transliterated Tchésma) was the second ship of the Ekaterina II-class battleships built for the Imperial Russian Navy in the 1880s. Named after the Russian victory at the Battle of Chesma in 1770, she was built by the Russian Steam Navigation Company at Sevastopol. When the ship was completed, she proved to be very overweight, which meant that much of her waterline armor belt was submerged. She served in the Black Sea Fleet until she was turned over to the Sevastopol port authorities and decommissioned in 1907. This picture is a chromolithograph print of Chesma, dated 1892; it is now in the collection of the Bibliothèque nationale de France. Company Contact Country Alfredsfutterkiste Mariaanders Germany Centromoctezuma Francisc Mexico Ernsthandel Rolandmendel Austria The world is beautiful.''') 
text = str()
sent = list(doc.sents)
for ele in sent:    
    for token in ele:    
        if(token.pos_ in ['SPACE', 'SYM'] or token.text in [':', ',']):
            pass
        else:
            if(text == ''):
                text = token.text
            else:
                text = text + ' ' + token.text

doc = nlp(text)
sentences = list(doc.sents)  
required_relation = [7037928807040764755, 403, 8206900633647566924, 12837356684637874264, 439, 440, 402, 416, 426, 428, 410, 446, 14792705179330092273, 439, 429]
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

print("1235677s")
flag = 0
for sentence in sentences:
    for ele in sentence:
        #print(ele, ele.dep, ele.dep_)
        if(ele.dep in required_relation):
            pass
        elif(len(ele.text) == 1):
            pass
        else:
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

sentences = []

for dat in data:
    print(dat)
    sentences.append(dat)

heading = []
def counting(txt):                                                         #checking for spaces
    count = 0
    for a in txt:
        if(a == ' '):
            count = count + 1
            break
    return(count)

if(counting(data[0].text) != 0):
    for token in data[0]:
        heading.append(token)
else:
    heading.append(data[0])
    if(counting(data[1].text) != 0):
        heading.append(data[1][0])
    else:
        heading.append(data[1])
    del data[0]

if(len(heading) == 1):
    heading.append(sentences[1][0])
   
print(heading)
sentences = data
a = sentences

i = 1
single_token = []


def ner(text):                                                              #checking for ner
    txt = nlp(text)
    if(len(txt.ents) == 0):
        return (0)    
    else:
        for ent in txt.ents:
            return(ent.label_)

def name(text):                                                             #checking for name
    first_char = text[0]
    rest = text[1:len(text)]
    if(first_char.isupper() and rest.islower()):
        return(1)
    else:
        return(0)            

while(i < len(sentences)):
    space = counting(sentences[i].text)
    if(space > 0):    
        for token in sentences[i]:
            single_token.append(token)
    else:
        single_token.append(sentences[i])
    i = i + 1

print(single_token) 

def value_alter(heading, single_token):
    while(len(single_token) < 3*len(heading)):
        l1 = len(heading)
        i = int(l1/2)
        for i in range(int(l1 -1), int((l1/2) -1), -1):
            single_token.insert(0, heading[i])
        del heading[int(l1/2) : l1]

value_alter(heading, single_token)

def check(data1, data2):                                                          #checking if two datas are of the same type
    flag = 0
    flag1 = 0
    try:
        data1.is_alpha
        data2.is_alpha
    except:
        flag1 = 1

    if(flag1 != 1):    
        if((data1.is_alpha == data2.is_alpha == True) and flag1 == 0):
            if(ner(data1.text) == ner(data2.text) != False):
                flag = 2
            elif(name(data1.text) == name(data2.text) == True and (ner(data1.text) == ner(data2.text))):
                flag = 1
    try:
        data1.like_num 
        data2.like_num

    except:
        flag1 = 2
    
    if(flag1 != 2 and flag == 0):                
        if(data1.like_num == data2.like_num == True):
            flag = 3

    try:
        data1.shape_ 
        data2.shape_
    
    except:
        flag1 = 3

    if(flag1 != 3 and flag == 0):
        if(data1.shape_ == data2.shape_):
            flag = 4
    return(flag)

def check_decrease(heading, single_token):                                       #whether to increase the heading or decrease it
    a = heading[-1]
    i = len(heading) - 2
    pos = []
    while(i > -1):
        j = check(a, single_token[i])
        if(j != 0):
            pos.append(i)
        i = i - 1
    return(pos)        




def finding_heading(heading, single_token):                                       #finding the heading
    l1 = len(heading)
    j = 0
    while(j < l1 and len(single_token) > 3*l1 -1):
        if(check(single_token[j], single_token[j + l1]) == check(single_token[j], single_token[j + l1 + l1]) != 0):
            j = j + 1
        else:
            break
        
    if(j == l1 and l1 != 0 ):
        return       
        
    

    else:
        pos = check_decrease(heading, single_token)
        while(len(pos) != 0):
            iter_value = pos[0] + 1
            del pos[0]
            j = 0
            while(j < iter_value and iter_value != 1):
                if(check(single_token[j], single_token[j + iter_value]) == check(single_token[j], single_token[j + iter_value + iter_value]) != 0):
                    j = j + 1
                else:
                    break
            if(iter_value == 1):
                if(check(single_token[j], single_token[j + iter_value]) == check(single_token[j], single_token[j + iter_value + iter_value]) == check(single_token[j], single_token[j + 3]) == check(single_token[j], single_token[j + 4]) != 0):
                    j = j + 1
                else:
                    break

            if(j == iter_value):
                for i in range(iter_value, len(heading)):
                    single_token.insert(0, heading[i])
                del heading[iter_value : int(len(heading))]
                return
            

        heading.append(single_token[0])
        if(len(single_token) < 3* len(heading)):
            return
        else:
            del single_token[0]
            finding_heading(heading, single_token)


def finding_tables(heading, single_token):                                       #finding the table
    finding_heading(heading, single_token)    
    value_alter(heading, single_token)
    print(heading)
    l1 = len(heading)
    i = 0
    values = [] 
    while(i < 2 * l1):
        values.append({heading[i % l1] : single_token[i]})
        i = i + 1

    
    print(values)
    check_value = single_token[0 : l1]   
    del single_token[0 : ((2 * l1))]



    i = 0
    l1 = len(heading)
    itera = 0

    for token in single_token:
        itera = 0
        if(i == l1):
            i = 0
        while(itera < l1 and i < l1):
            if(check(token, check_value[i]) > 0):
                values.append({heading[i] : token})
                itera = itera + 1
                i = i + 1
                break
            else:
                values.append({heading[i] : None} )
                itera = itera + 1
                i = i + 1
            if(i == l1):
                i = 0
    return(values)


def check_for_another_table(table, heading):                                   #checking for the second table
    l1 = len(heading)
    l2 = len(table)
    none = 0
    pos = -1
    for i in range(l2):
        if(i % l1 == 0):
            pos = i
            none = 0

        if(table[i][heading[i%l1]] == None):
            none = none + 1

        if(none > l1/2):
            break
    if(none <= l1/2):
        pos = l2
    return(pos)

pos = -1
table = []
while(pos != len(table)):
    table = finding_tables(heading, single_token)
    pos = check_for_another_table(table, heading)
    print("\n\nThe table is : ")
    i = 0
    print("\nThe heading fot the table is : \n\n", heading)
    for i in range(pos):
        print(table[i])
    print("\n\n")
    l1 = len(heading)
    del single_token[0 : pos - 2 * l1]
    head = heading
    heading = []
    count = 0
    for i in range(pos,len(head)):
        if(table[i][head[i % len(head)]] != None):
            heading.append(table[i][head[i % len(head)]])
            count = count + 1
        if(len(heading) == 2):
            break
    if(count == 0 and len(single_token) > 1):
        heading.append(single_token[0])
        heading.append(single_token[1])
    value_alter(heading, single_token)
    
    if(heading == [] and len(single_token) > 5):
        heading.append(single_token[0])
        heading.append(single_token[1])
    elif(heading == []):
        pos = len(table)
print(single_token)





