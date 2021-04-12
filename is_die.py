import string
def is_die_string(die_string):
    # List of possible dice
    list_of_dice = [4,6,8,10,12,20]
    
    if die_string.startswith('-') == True or die_string.startswith('+') == True  :
        die_string = die_string[1:]
    
    d_position= die_string.find('d')
    
    # position of the letter 'd' in the die string
    if d_position == -1:
        return False
    else:     
        if (d_position != 0 and  die_string[:d_position].isdigit() == False) or die_string[d_position+1:].isdigit() == False:
            return False
        else:
            if int(die_string[d_position+1:]) not in list_of_dice:
                return False
            else:
                return True