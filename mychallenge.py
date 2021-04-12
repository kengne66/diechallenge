#! /usr/bin/python3


import json
import os
from os import path
from roll_of_expression import roll_of_expression
import sys

#def myprogram():

filerequest=input("type the file name please:  ")
    
if path.exists(filerequest) == False:
     print("file does not exist")
    sys.exit() 
        
    
f = open(filerequest, "r")
f.seek(0,0)

#expression_line=""
    
# data = {}
data = []
#data['line'] = []
    
for expression_line in f.readlines():
    #print(roll_of_expression(expression_line))   
        
    data.append({
        'roll-result' : roll_of_expression(expression_line)[0],
        'roll-min': roll_of_expression(expression_line)[1],
        'roll-max': roll_of_expression(expression_line)[2],
    })
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
print("finish")
