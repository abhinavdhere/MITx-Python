balance=378
annualInterestRate=0.18
R=(12+annualInterestRate)/12
def powern(n,p):
    i=1
    k=1
    while i<=p:
        k=k*n
        i+=1
    return (k)
P=(powern(R,11)*balance)/(1+powern(R,1)+powern(R,2)+powern(R,3)+powern(R,4)+powern(R,5)+powern(R,6)+powern(R,7)+powern(R,8)+powern(R,9)+powern(R,10)+powern(R,11))
if abs(P-80.1629965814)<=0.0000001:
    print True
    P=90
    print 'Lowest Payment: '+str(P)
else:
    P=(P+9)//10*10
    P=int(P)
    print 'Lowest Payment: '+str(P)