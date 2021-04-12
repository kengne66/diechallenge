import math
import random
from is_die import is_die_string

def roll_die(die_string):
    die_string = die_string.lower()
    if is_die_string(die_string) == False:
        return [0,0,0,]
    else:
        d_position = die_string.find('d')
        number_of_faces = int(die_string[d_position+1:])
        #mylist =range(number_of_faces)
        
        if d_position == 0:
            number_of_rolls = 1
        else:
            number_of_rolls = int(die_string[:d_position])
            number_of_rolls_abs = abs(number_of_rolls)
            
        #print(number_of_rolls)
        
        list_of_rolls_result = random.choices(population=list(range(1,number_of_faces+1)), k = number_of_rolls_abs)
        
        if number_of_rolls < 0:
            rollmax = number_of_rolls 
            result = -sum(list_of_rolls_result)
            rollmin = number_of_rolls*number_of_faces
            
        else:
            rollmin = number_of_rolls 
            result = sum(list_of_rolls_result)
            rollmax = number_of_rolls*number_of_faces
        finalresult = [result,rollmin,rollmax]
        
        return finalresult
