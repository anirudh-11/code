import regex as re
import spacy
from spacy.tokenizer import Tokenizer



nlp = spacy.load('en')
msg = nlp('https://www.youtube.com/watch?v=9qz1yEQlVhg')

for i, token in enumerate(nlp(msg)):
    if(token.like_url):
        print(token)

#print("hi")