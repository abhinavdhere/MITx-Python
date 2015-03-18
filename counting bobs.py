#PSET1, Problem 2
#counting bobs
#Write a program that prints the number of times 
#the string 'bob' occurs in s
s=raw_input('Enter s: ')#For testing.Delete before submission
k=0;#initialize string order variable
count=0
while (k<=len(s)):
    if s[k:k+3]=='bob':#splits string in subsets of 3
        count+=1
    k+=1
print('Number of times bob occurs is: '+str(count))