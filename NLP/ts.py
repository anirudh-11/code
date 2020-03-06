import spacy
import requests
from flask import jsonify
import json
#nlp = spacy.load('en_core_web_lg')
#doc = nlp('''This one's a gritty drama, with Scorsese creating some marvellous set pieces where the past intervenes with the present and Leonardo creates a compelling picture of brooding disarray.''')
#doc = nlp('''Shutter Island. A film that won't make you question your own sanity. A film that will leave you breathless. A film that has re-ignited the thriller genre. A film that will leave you, and the main character, searching for answers.''')
#doc = nlp("""Cameron clearly inspired challenge reproducing event physical verisimilitude impact inconceivable numerous previous film TV versions event""")
#doc2=nlp("""comedy action music movie romance""")
#sentences = list(doc.sents)
#for sentence in sentences:   
"""for t1 in sentence:
        for t2 in doc2:
            if(t1.pos_ == 'NOUN'):
                print(t1, t2, t1.similarity(t2))
  """

data = {
         'text' : "The movie was amazing"
        }

r = requests.post(url = "http://text-processing.com/api/sentiment/", data = data) 
print(r.content.decode('ASCII'))
a = r.content.decode('ASCII')
s = a
json_acceptable_string = s.replace("'", "\"")
d = json.loads(json_acceptable_string)
print(d['probability']['neg'])