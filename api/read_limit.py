
import urllib.request
import random

content = open("first_name",'r')
#head = content.readline(200)
head = content.readlines(22)
print (head)
name_list = content.read().split('\n')
name_list = list(name_list)
#print(name_list)
#name_words  = [word for word in words]
#one_name = ' '.join([name_words[random.randint(0, len(name_words))] for i in range(2)])

def rand_name():
   random_int1 = random.randint(0,len(name_list)-1)
   random_int2 = random.randint(0,len(name_list)-1) 
   while(random_int1 == random_int2):
      random_int2 = random.randint(0,len(name_list)-1)
   name = name_list[random_int1] + ' ' + name_list[random_int2]
   return name

def size():
   return(len(name_list))