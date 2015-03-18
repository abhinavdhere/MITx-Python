def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    ''' 
    i=int(len(aStr)/2)   
    if len(aStr)==0:
        return False
    elif aStr[i]==char:
        return True
    elif i==0:
        return False
    elif char<aStr[i]:
        return isIn(char,aStr[0:i])
    elif char>aStr[i]:
        return isIn(char,aStr[i+1:])