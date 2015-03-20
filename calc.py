#--------------------------------------------------------------
#Name: Calculator
#Purpose: Calculator with a simple MATLAB like interface
#
#Author: Abhinav Dhere 
#
#Created: 19 March 2015
#
#License: This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#         See http://creativecommons.org/licenses/by-nc-sa/4.0/ for details
#--------------------------------------------------------------

import math
def parse(expression):
    """
    Takes an expression as a string
    Returns a list of strings which are numbers and operation
    """
    operations=['+','*','/','-']
    expression1=expression
    if expression1[0]=='-':
        expression1=expression1.split('-',1)
        for operation in operations:
            if operation in expression1[1]:
                operands=expression1[1].split(operation)
                operands.append(operation)
                break
        operands[0]='-'+operands[0]
    else:
        for operation in operations:
            if operation in expression1:
                operands=expression1.split(operation)
                operands.append(operation)
                break
    return operands

def strToNum(n):
    """
    Takes a number in string form
    Returns it in int/float form
    """
    numbers={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    n1=n
    if '-' in n:
        n1=n[1:]
    if '.' in n1:
        nParts=n1.split('.')
        i=len(nParts[0])-1
        number1=0
        number2=0
        for digit in nParts[0]:
            if digit=='-':
                pass
            else:
                num=numbers[digit]
                number1+=num*pow(10,i)
                i-=1
        j=1
        for digit in nParts[1]:
            if digit=='-':
                pass
            else:
                num=numbers[digit]
                number2+=num*pow(10,-j)
                j+=1
        number=number1+number2

    elif '.' not in n1:
        i=len(n1)-1
        number=0
        for digit in n1:
            if digit=='-':
                pass
            else:
                num=numbers[digit]
                number+=num*pow(10,i)
                i-=1

    if '-' in n: 
        return number*-1
    else:
        return number

def calc():
    expression=raw_input()
    if expression=="exit":
        run=False
        return run
    else:
        operands=parse(expression)
        operand1=strToNum(operands[0])
        operand2=strToNum(operands[1])
        if operands[2]=="+":
            result=operand1+operand2
        elif operands[2]=="-":
            result=operand1-operand2
        elif operands[2]=="*":
            result=operand1*operand2
        elif operands[2]=="/":
            result=operand1/operand2

        print "ans= "+str(result)
        print ""
        run=True
        return run

print "                       The Calculator"
print "                                 - By Abhinav Dhere"
run=True
while run:
    try:
        run=calc()
    except:
        print "Invalid Expression"
        print ""
