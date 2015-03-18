from ps4a import *
import time

#
#
# Problem #6: Computer chooses a word
#
#
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
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    def selectplayer():
        decide_player=raw_input('Enter u to have yourself play, c to have the computer play: ')            
        if (decide_player!='u' and decide_player!='c'):
                print 'Invalid input.'
                decide_player=selectplayer() 
        return decide_player
            
    def play(decide_player):
        if decide_player=='u':
                playHand(hand, wordList, HAND_SIZE)
        elif decide_player=='c':
                compPlayHand(hand, wordList, HAND_SIZE) 
    while True:
        decide_round=raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        try:          
            if decide_round=='n':
                hand=dealHand(HAND_SIZE)
                decide_player=selectplayer()
                play(decide_player)
            elif decide_round=='r':
                testvar=hand
                decide_player=selectplayer()
                play(decide_player)
            elif decide_round=='e':
                return
            else:
                print 'Invalid command.'
        except NameError:
              print 'You have not played a hand yet. Please play a new hand first!'

# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)

