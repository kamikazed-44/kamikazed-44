# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 07:33:08 2021

@author: ONG-OPS-1
"""
"""Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
 View this code at https://nostarch.com/big-book-small-python-projects
 A version of this game is featured in the book "Invent Your Own
 Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle"""

import random
NUM_DIGITS=3 #(!) Try setting this to 1 to 10
MAX_GUESSES=10  # (!) try setting this to 1 to 100
def main():
    print('''Bagels, a deductive logic game.
 By Al Sweigart al@inventwithpython.com
 
 I am thinking of a {}- digit number with no repeated digits.
 Try to guess what it is. Here are some clues:
     When i say :         That means:
         Pico            One digit i correct but in the wrong position
         fermi           One digit is correct and in the right position
         Bagels          No digit is correct
         
For example, if the secret number is 248 and your guess is 843, the clues would be Fermi Pico.'''. format (NUM_DIGITS))
    
while True: # Main game loop.
    #This stores the secret number the player needs to guess:
    secretNum = getSecretNum()
    print('I have thought up a number.')
    print('You have {} guesses to get it.'.format(MAX_GUESSES))
    
    numGuesses =1
    while numGuesses <= MAX_GUESSES:
        guess = ''
        
    #keep looping until you enter a valid guess:
        while len(guess)!=NUM_DIGITS or not guess.isdecimal():
            print('Guess#{}:'.format(numGuesses))
            guess = input('>')
            clues= getClues (guess,secretNum)
            print(clues)
            numguesses+=1
            
            if guess == secretNum:
                break # they're  correct, so break out of this loop.
                if numGuesses >MAX_GUESSES:
                    print ('You ran out of guesses.')
                    print ('The answer was {}.'.format(secretNum))
                    
                    #ask player if they want to play again.
                    print ('Do you want to play again?(yes or no)')
                    if not input ('>').lower().startswith('y'):
                        break
                    print('thanks for playing')
    def getSecretNum():
           """Returns a string made up of NUM_DIGITS unique random digits """                
           numbers= list ('0123456789') # create a list of digits 0 to 9
           random.shuffle(numbers) # shuffle numbers in random order.
        # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in  range(NUM_DIGITS):
        secretNum +=str(numbers[i])
    return secretNum
            
def getClues(guess,secretNum):
                """Returns a string with the pico, fermi,bagels clues for a guess and secret number pair."""
                if guess == secretNum:
                    return 'You got it !'
                
                clues = []
for i in range (len(guess)):
            if guess [i] == secretNum[i]:
    # a correct digit is in the correct place.
                 clues.append('Fermi')
            elif guess [i] in secretNum:
                    # a correct digit is in the incorrect place
                    clues.append('pico')
                   
                    
if lens (clues)== 0:
                        return 'Bagels' # There are nocorrect digits at all.
else:
                        # sort the clues into alphabetical order so their original order
                        #does  not give information away
                        clues.sort()
                        # Make a single string from the list of string clues
                        return''.join(clues)
                        
                        
                #if the program is run (instead of imported), run the game:
                   
if __name__ =='__main__':
                        main()
                        
            
            
        
        