from os.path import abspath, join, dirname
import random
import names
import string
import check
from flask import Flask, jsonify, request
app = Flask(__name__)

rsdetails = []
name = []
department = ['CSE', 'ECE', 'Mech', 'EEE', 'IT']
sid=[]


@app.route('/',methods=['POST'])
def home():
   number = {'num' : request.json['num']}
   num = int(number['num'])
   rsdetails = []
   name = set()
   sid = set()
   names.get_full_name()
   while(num):
     flag = 0
     num = num-1
     while(flag == 0):
       a = random.choice(string.ascii_uppercase)
       b = random.choice(string.ascii_uppercase)
       n = random.randint(00,99)
       if(n<10):
        n = '0' + str(n)
       n = str(n)
       rsdetail = {'name' : names.get_full_name(), 'department' : department[random.randint(0,4)], 'sid' : a + b + n}
       sid.add(rsdetail['sid'])
       name.add(rsdetail['name'])
       flag = len(sid) == len(name) == (int(number['num'])-num)
     rsdetails.append(rsdetail)
   return jsonify({'rsdetails' : rsdetails})


if __name__ == '__main__':
 app.run(debug = True)
