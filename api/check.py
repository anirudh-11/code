
import urllib.request
import random

word_url = "https://raw.githubusercontent.com/dominictarr/random-name/master/names.txt"
response = urllib.request.urlopen(word_url)
long_txt = response.read().decode()
words = long_txt.splitlines()

name_words  = [word for word in words]
one_name = ' '.join([name_words[random.randint(0, len(name_words))] for i in range(2)])


def rand_name():
   name = ' '.join([name_words[random.randint(0, len(name_words)-1)] for i in range(2)])
   return name

