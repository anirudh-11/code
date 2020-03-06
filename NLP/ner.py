import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(u'''In the 1927 Chicago mayoral election, Republican candidate William Hale Thompson (campaign poster shown) defeated Democratic incumbent William Emmett Dever. Dever had enforced Prohibition despite his opposition to it, which led to rising violence in the city. Thompson, who had been mayor from 1915 to 1923, was openly backed by the mobster Al Capone. He promised to end the enforcement of Prohibition, bitterly attacked his opponents throughout the campaign, and claimed that the United Kingdom was conspiring to take back control of the United States. Dever's supporters attempted to push back against Thompson's rhetoric and claims; they insisted that Dever had the attitude and policies appropriate for the city. Thompson, the last non-Democrat to win a Chicago mayoral election, damaged Chicago's reputation across the United States, and historians rank him among the most unethical mayors in American history. "The url is www.asdassdasd,com". The email id is asdasd@kffasd.com. there are ten people''')

for ent in doc.ents:
    print(ent.text, ent.label_)

email = []
url = []
number = []

for token in doc:
    if(token.like_email):
        email.append(token)
    elif(token.like_url):
         url.append(token) 
    elif(token.like_num):
         number.append(token)

print('\nThe email ids are : ',email)
print("\nThe urls are : ",url)
print("\nThe numbers are : ",number)

