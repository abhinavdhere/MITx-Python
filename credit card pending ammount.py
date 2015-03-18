#PSET2 Prob 2: Minimum pending ammount in credit card (balance) after 1 yr
#Credit card companies charge interest monthly on unpaid ammount.
balance=float(raw_input('Enter initial balance:'))
annualInterestRate=float(raw_input('Enter ROI: '))
monthlyPaymentRate=float(raw_input('Enter P: '))
monthnum=1
ub=balance
Pf=0
while monthnum<=12:
    print 'Month: '+str(monthnum)
    P=balance*monthlyPaymentRate
    P=round(P,2)
    ub=balance-P
    ub=round(ub,2)
    balance=ub+(annualInterestRate/12)*ub
    balance=round(balance,2)
    print 'Minimum monthly payment: '+str(P)
    print 'Remaining balance: '+str(balance)
    Pf=Pf+P
    monthnum+=1
print 'Total paid: '+str(Pf)
print 'Remaining balance: '+str(balance)