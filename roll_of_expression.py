from is_die import is_die_string
from roll_die_string import roll_die

def roll_of_expression(expression_line):

    expression_line = expression_line.lower()
    
    
    #Delete all the spaces in expression_line
    expression_line = expression_line.replace(' ','')
    
    #Associates signs to dices or to numbers
    
    expression_line = expression_line.replace('+',' +')
    expression_line = expression_line.replace('-',' -')
    
    # Transform the expression-line into a list
    expression_list = expression_line.split()
    
   # Evaluation of the result
    finalresult = [0,0,0]
    resultmin = 0
    result = 0
    resultmax = 0
    
    for expression_item in expression_list:
        
        expression_item2=expression_item
        
        if expression_item.startswith('-') == True or expression_item.startswith('+') == True:
            expression_item2 = expression_item[1:]
            
        if   is_die_string(expression_item2) == False and expression_item2.isdigit() == False :
            finalresult =[0,0.0]
           # break
        if is_die_string(expression_item):
            
            result += roll_die(expression_item)[0]
            resultmin += roll_die(expression_item)[1]
            resultmax += roll_die(expression_item)[2]
        else:
            resultmin += int(expression_item)
            result += int(expression_item)
            resultmax += int(expression_item)
    finalresult = [result,resultmin,resultmax]
    return finalresult      