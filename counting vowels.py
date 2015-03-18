s=raw_input('Enter s: ')
vowel='aeiou'
count=0
for letter in vowel:
    for char in s:
        if char==letter:
            count+=1
print('Number of vowels: '+str(count))