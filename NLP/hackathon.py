import spacy
import requests
import json


nlp = spacy.load('en_core_web_lg')
doc = nlp('''This one's a gritty drama, with Scorsese creating some marvellous set pieces where the past intervenes with the present and Leonardo creates a compelling picture of brooding disarray.''')
doc = nlp('''Shutter Island. A film that won't make you question your own sanity. A film that will leave you breathless. A film that has re-ignited the thriller genre. A film that will leave you, and the main character, searching for answers.''')
sentences = list(doc.sents)
doc2=nlp("""comedy action music movie romance thriller""")


rating = []
overall_rating = 0

for sentence in sentences:   
    comedy = []
    value = []
    music = []
    action = []
    thriller = []
    crew = []
    romance = []
    movie = []
    if(sentence.text[-1] == '?'):
        pass
    else:
        data = {
                'text' : sentence.text
               }

        r = requests.post(url = "http://text-processing.com/api/sentiment/", data = data) 
        s = r.content.decode('ASCII')  
        json_acceptable_string = s.replace("'", "\"")
        d = json.loads(json_acceptable_string)
    
        non_stop = ''
        for token in sentence:
            if(token.is_stop == False and token.dep == 402):
                value = []
                if(non_stop == ''):
                    a = token.head
                    non_stop = token.text + '-' + a.text
                else:
                    a = token.head
                    non_stop = non_stop + ' ' + token.text + '-' + a.text
                for token2 in doc2:
                    value.append(token.similarity(token2))
                if(max(value)<0.35):
                    value = []
                    for token2 in doc2:
                        a = token.head
                        value.append(a.similarity(token2))
                if(max(value) > 0.35):
                    if(doc2[value.index(max(value))].text == 'music'):
                        music.append(d['probability'][d['label']])
                    elif(doc2[value.index(max(value))].text == 'comedy'):
                        comedy.append(d['probability'][d['label']])
                    elif(doc2[value.index(max(value))].text == 'action'):
                        action.append(d['probability'][d['label']])
                    elif(doc2[value.index(max(value))].text == 'romance'):
                        romance.append(d['probability'][d['label']])
                    elif(doc2[value.index(max(value))].text == 'thriller'):
                        thriller.append(d['probability'][d['label']])
                    elif(doc2[value.index(max(value))].text == 'movie'):
                        movie.append(d['probability'][d['label']])
        print(music, comedy, action, romance, thriller, movie)

                    