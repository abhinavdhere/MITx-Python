#prime number generator
#Dt 20.02.2015
#Test used: A candidate number x is prime if (x % p) != 0 for all earlier primes p.

def primeGen():
    p=[]
    pnumber=1
    while True:
        pnumber+=1
        flag=True
        for num in p:
            if pnumber%num==0:
                flag= False
                break
        if flag==True:
            p.append(pnumber)
            yield pnumber
                
