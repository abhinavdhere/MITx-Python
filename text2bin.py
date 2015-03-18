#This is a program to convert text string into binary ASCII values
#Written by Abhinav Dhere on 19/02/2015.

class text2bin(object):
    def __init__(self,text):
        assert type(text)==str
        self.text=text

    def convert(self):
        bina=''
        for letter in self.text:
            bina=bina+str('{0:b}'.format(ord(letter)))+' '
        return bina

    def __str__(self):
        return text2bin.convert(self)

class bin2text(object):

    def __init__(self,binary):
        assert type(binary)==str
        self.bina=binary    
            
    def convert(self):
        text=''
        binary_list=self.bina.split()
        for num in binary_list:
            text=text+chr(int(num,2))
        return text

    def __str__(self):
        return bin2text.convert(self)

def choose():
            try:
                choice=raw_input('Run again?(y/n)')
                if choice=='n':
                    flag=False
                elif choice=='y':
                    flag=True
                else:
                    raise ValueError
            except ValueError:
                print 'Invalid Input'
                flag=choose()
            return flag

def converter():
    try:
        flag=True
        while flag==True:
            print '1. Text to Binary'
            print '2. Binary to Text'
            select=int(raw_input('Select Conversion no.: '))
            assert type(select)==int and (select==1 or select==2)
            if select==1:
                text=raw_input('Enter text: ')
                print text2bin(text)
            if select==2:
                binary=raw_input('Enter binary: ')
                print bin2text(binary)
            elif (select!=1 and select!=2):
                raise ZeroDivisionError
            flag=choose()
    except AssertionError:
        print 'Invalid Input'
        converter()

print 'Welcome to TB-BT Converter'
converter()
        
