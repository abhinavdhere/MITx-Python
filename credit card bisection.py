#!/usr/bin/env python
#PSET2, Problem 3:
#Bisection to find min monthly payment
#Algo:Lower bound is if no interest i.e. 1/12th of initial balance
#Upper bound is if paid at end i.e. 1/12th of final balance
balance=float(raw_input('Enter initial balance:'))
annualInterestRate=float(raw_input('Enter ROI: '))
def powern(n,p):
    i=1
    k=1
    while i<=p:
        k=k*n
        i+=1
    return (k)
def balanceyr(balance,annualInterestRate,P):
    monthnum=1
    ub=balance
    while monthnum<=12:
        ub=balance-P
        balance=ub+(annualInterestRate/12)*ub
        monthnum+=1
    return(balance)
monthlyInterest=annualInterestRate/12.0
a=balance/12
b=(balance*powern(1+monthlyInterest,12))/12
c=(a+b)/2.0
epsilon=0.001
while abs((balanceyr(balance,annualInterestRate,c))) >= epsilon:
    if balanceyr(balance,annualInterestRate,c)<0:
        b=c
    else:
        a=c
    c=(a+b)/2.0
c=round(c,2)
print 'Lowest Payment: '+str(c)
