import pandas as pd
from collections import Counter
from itertools import repeat
pd.set_option('display.max_columns', 400)

def main():
    with open("text_data.txt", 'r') as fptr:
        content = fptr.read()
        # print(content)

    content = content.lower().split()
    fr_table = dict(Counter(i for i in content))
    
    # printing result 
    # print("The list frequency of elements is : " + str(fr_table)) 
    # for key in fr_table.keys():
    #     print("{} : {}".format(key, fr_table[key]))

    df = pd.DataFrame(data = None, columns = ['Frequency', 'Tally'], index = set(content))

    tally_val = {1 : '|', 2 : '||', 3 : '|||', 4 : '||||', 5 : '||||\\'}

    for word in content:
        df['Frequency'][word] = fr_table[word]
        fr = fr_table[word]
        df['Tally'][word] = str()
        while(fr > 5):
            df['Tally'][word] = df['Tally'][word] + tally_val[5] + ' '   
            fr = fr - 5
        if(fr == 0):
            pass
        else:
            df['Tally'][word] = df['Tally'][word] + tally_val[fr]

    print(df.to_string())

if(__name__ == '__main__'):
    main()