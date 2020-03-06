
import random
import names
import string
import namegenerator
import check1
import namegenerator
from flask import Flask, jsonify, request
import time
app = Flask(__name__)

rsdetails = []
name = []
department = ['CSE', 'ECE', 'Mech', 'EEE', 'IT']
sid=[]


@app.route('/',methods=['POST'])
def home():
   start = time.time()
   number = {'num' : request.json['num']}
   num = int(number['num'])
   rsdetails = []
   name = set()
   sid = set()
   if(num > ((check1.size())*(check1.size()-1))):
     return jsonify({"Sorry" : "Out of Bound"})
   while(num):
    flag = 0
    num = num-1
    while((flag==0)):
     a = random.choice(string.ascii_uppercase)
     b = random.choice(string.ascii_uppercase)
     n = random.randint(00,99)
     if(n<10):
      n = '0' + str(n)
     n = str(n)
     rsdetail = {'name' : check1.rand_name(), 'department' : department[random.randint(0,4)], 'sid' : a + b + n}
     sid.add(rsdetail['sid'])
     flag = len(sid) == (int(number['num'])-num)
     if(flag == 0):
       flag = 0
     if(flag != 0):
       name.add(rsdetail['name'])
       flag = len(name) == (int(number['num'])-num)
       if(flag == 0):
         sid.remove(rsdetail['sid'])
    rsdetails.append(rsdetail)
   end = time.time()
   print(end - start)
   return jsonify({'rsdetails' : rsdetails})


if __name__ == '__main__':
 app.run(debug = True)
