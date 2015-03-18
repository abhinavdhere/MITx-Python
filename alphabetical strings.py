#PSET2 Problem 3: Alphabetical Strings
#Write a program that prints the longest substring of s in which the 
#letters occur in alphabetical order.
#In the case of ties, print the first substring.
#Algorithm: First generate all substrings, then check each for alphbetical
#order and then find the substring with max length.
s=raw_input('Enter s: ')
def isalpha(s):#function to check if a string is in alphabetical order
    k=0
    if len(s)==1:#since if len=1, k=0==len-1, so doesn't go in while
        return True
    else:
        while k<len(s)-1:#since string splitting counts 0 to n-1
            if s[k]>s[k+1]:#check for alphabetical
                st=False#status boolean
                return (st)
                break
            else:
                st=True
            k+=1
        if st != False:
            return True
def substr(string):#function for finding all substrings
    j=1
    a=[]#defines a new empty list
    while True:
        for i in range(len(string)-j+1):#appends all 1 element substrings
            a.append(string[i:i+j])#then 2 element ones and so on
        if j==len(string):#condition for end of process
            break
        j+=1
    return a
a=substr(s)#calling function to generate substrings
b=[]#defining a new empty list
for elem in a:#checking each element of set a for alphabetical or not
    if isalpha(elem):
        b.append(elem)#adds alphabetical elem to list b
ans=max(b, key=len)#find max based on length
print 'Longest substring in alphabetical order is:'+str(ans)