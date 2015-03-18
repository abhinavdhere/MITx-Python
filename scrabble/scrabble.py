#MITx 6.00.1x Wordgame
#Developed with the help of template created by: Kevin Luu <luuk> 
#and Jenna Wiens <jwiens>, modified by: Sarina Canelake <sarina>

import random
import getpass

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	
#http://stackoverflow.com/questions/2068349/understanding-get-method-in-python
# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score=0#initialize score variable
    for i in word:
        score=score+(SCRABBLE_LETTER_VALUES[i])
    score=score*len(word)
    if len(word)==n:#gives bonus if all letters used
        score=score+50
    assert type(score)==int and score>=0#to ascertain the condition on return
    return score
#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]#randrange generates a random number in range 0,len(VOWELS)
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    hand=hand.copy()#to generate a copy of dict. hand
    for i in word:
        hand[i]=hand.get(i,0)-1#inserts 0 if i not in word else decrements
    return hand
#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    hand=hand.copy()
    wordList=wordList[:]#to generate copy of list wordList
    if word in wordList:
        try:
            for i in word:
                hand[i]-=1
                if hand[i]<0:#raises exception if letter not available
                    raise Exception()
            return True
        except Exception:
            return False
    else:
        return False            
#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    length=0
    for i in hand.keys():#iterate in list of all keys
        length=length+hand[i]
    return length

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    
    score=0# Keep track of the total score
    
    while calculateHandlen(hand)!=0:# As long as there are still letters left in the hand:
    
        print 'Current Hand: ',
        displayHand(hand)# Display the hand
        word=getpass.getpass('Enter word, or a "." to indicate that you are finished: ')# Ask user for input
        
        if word=='.':# If the input is a single period:
        
            print 'Total Score: '+str(score)+' points.'
            return score# End the game (break out of the loop)

            
        else:# Otherwise (the input is not a single period):
        
            if isValidWord(word, hand, wordList)==False:# If the word is not valid:
            
                print 'That is not a valid word. Please choose another word'# Reject invalid word (print a message followed by a blank line)
                
                print
            
            elif isValidWord(word, hand, wordList)==True:# Otherwise (the word is valid):

                scorep=getWordScore(word,n)
                print 'word earned '+str(scorep)+' points.',# Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score=score+scorep
                print 'Total: '+str(score)+' points'
                hand=updateHand(hand,word)# Update the hand 

    print 'Run out of letters. Total score: '+str(score)+' points.'# Game is over (user entered a '.' or ran out of letters), so tell user the total score
    return score
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """    
    maxscore=0# Create a new variable to store the maximum score seen so far (initially 0)

    bestword=None# Create a new variable to store the best word seen so far (initially None)  
    def isFromHand(word, hand):
        hand=hand.copy()
        try:    
            for i in word:
                hand[i]-=1
                if hand[i]<0:
                    raise Exception()
            return True
        except Exception:
            return False       
    for word in wordList:#for word in wordList:# For each word in the wordList
        
        if isFromHand(word, hand):# If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
            score=getWordScore(word,n)# Find out how much making that word is worth
            if score>maxscore:# If the score for that word is higher than your best score

                maxscore=score# Update your best score, and best word accordingly
                bestword=word

    return bestword# return the best word you found.

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    score=0
    def ishandzero(hand):
        try:
            for word in hand.keys():
                if hand[word]!=0:
                    raise Exception
            return True 
        except Exception:
                return False
    while True:
        print 'Current Hand: ',
        displayHand(hand)
        word=compChooseWord(hand, wordList, n)
        if word==None:
            break
        else:
            maxscore=getWordScore(word,n)
            score=score+maxscore
            print '"'+word+'"'+' earned '+str(maxscore)+' points.',
            print 'Total: '+str(score)+' points'
            hand=updateHand(hand,word)# Update the hand
            if ishandzero(hand):
                break
    print 'Total score: '+str(score)+' points.'
    return score
#
# Problem #8: Playing a game
#
#
def playGameuu(wordList):
    """
    wordList: list (string)
    """
    #def selectplayer():
     #   decide_player=raw_input('Enter u to have yourself play, c to have the computer play: ')            
      #  if (decide_player!='u' and decide_player!='c'):
       #         print 'Invalid input.'
        #        decide_player=selectplayer() 
        #return decide_player
            
  #  def play(decide_player):
   #     if decide_player=='u':
    #            playHand(hand, wordList, HAND_SIZE)
     #   elif decide_player=='c':
      #          compPlayHand(hand, wordList, HAND_SIZE) 
    rounds=int (raw_input ('Select no. of rounds: '))
    name1=raw_input('Enter name of player 1: ')
    name2=raw_input('Enter name of player 2: ')
    score1=0
    score2=0
    wins1=0
    wins2=0    
    for trial in range(1,rounds+1):         
            print 'Round no. :'+str(trial)
            hand=dealHand(HAND_SIZE)
            print name1+':'
            print
            score1+=playHand(hand,wordList, HAND_SIZE)
            print name2+':'
            print
            score2+=playHand(hand,wordList, HAND_SIZE)
            if score1>score2:
                print name1+' wins the round'
                wins1+=1
            elif score2>score1:
                print name2+' wins the round'
                wins2+=1
            elif score1==score2:
                print 'Tie!'
    print 'Stats: '
    print name1+' won '+str(wins1)+' rounds'
    print name2+' won '+str(wins2)+' rounds'
    if wins1>wins2:
        print 'Hence '+name1+' wins the game'
    elif wins2>wins1:
        print 'Hence '+name2+' wins the game'
    elif wins1==wins2:
        print 'The game was a tie!'
             
def playGameuc(wordList):
    rounds=int (raw_input ('Select no. of rounds: '))
    if rounds>0:    
        score1=0
        score2=0
        wins1=0
        wins2=0
        for trial in range(1,rounds+1):
            print 'Round no. :'+str(trial)
            hand=dealHand(HAND_SIZE)
            print 'Player: '
            print
            score1+=playHand(hand,wordList, HAND_SIZE)
            print 'CPU:'
            print
            score2+=compPlayHand(hand, wordList, HAND_SIZE)
            if score1>score2:
                print 'Player wins the round'
                wins1+=1
            elif score2>score1:
                print 'CPU wins the round'
                wins2+=1
            else:
                print 'Tie!'
        print 'Stats: '
        print 'Player won '+str(wins1)+' rounds'
        print 'CPU won '+str(wins2)+' rounds'
        if wins1>wins2:
            print 'Hence Player wins the game'
        elif wins2>wins1:
            print 'Hence CPU wins the game'
        elif wins1==wins2:
            print 'The game was a tie!'
    else:
        print 'Error! No of Rounds must be greater than 0'
        playGameuc(wordList)
        
def ask1():
    try:
        op=int(raw_input('Select option number: '))
    except:
        print 'Invalid input.'
        op=ask1()
    return op

def ask2():    
    try:
        op1=int(raw_input('Select option number: '))
    except:
        print 'Invalid input.'
        op1=ask2()
    return op1

def game():
    print 'Welcome to MITx 6.00.1x Wordgame v2.0!'
    print '1. New Game'
    print '2. About'
    print '3. Exit'
    op=ask1()
    if op==1:
        print '1. Player vs. CPU'
        print '2. Player vs. Player'
        op1=ask2()
        if op1==1:
            playGameuc(wordList)
        elif op1==2:
            playGameuu(wordList)
    if op==2:
        print 'This game was originally built on a template designed & modified' 
        print 'by Kevin Luu <luuk>, Jenna Wiens <jwiens> & Sarina Canelake <sarina>'                  
        print 'I built an original version with the help of the template for a course '
        print 'assignment for MITx 6.00.1x and then made this v2.0 which gives choice '
        print ' between p vs p or p vs cpu.'
        print '                                                     -Abhinav Dhere'
    if op==3:
        return

def play():
    pa='y'
    while pa=='y':
        game()
        pa=raw_input('Run again?(y/n): ')
    
#Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    play()
