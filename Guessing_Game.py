import math #importing math module
import random # importing the random module
#announcement
print("Guess the secret number\n") # prints the statement
nmax=int(input("enter the maximum number in the range:"))# reads the input
print(f'Try to guess a secret number from 1 to {nmax}.\n\n')# print the statement
sec_num=random.randrange(0,nmax)# using randrange() for holding a random number
nGuess = int(math.log2(nmax)+1)  # caluculating the number of guesses
print(f'you have {nGuess} guesses available.')# prints the statement
while nGuess: #while loop
        nGuess-=1 # caluculates the nGuess
        guess=int(input("Enter your guess:"))
        if (sec_num>guess and nGuess>1): # nested if loop
            print(f'The seceret number is greater than {guess}.')#using f-string to print the statement
            print(f'you have {nGuess} guesses available.')
        elif sec_num<guess and nGuess>1:
            print(f'The seceret number is less than {guess}.')
            print(f'you have {nGuess} guesses available.')
        elif guess==sec_num:
            print(f'Correct.  well done!')
            break   # loop exists here 
        if (nGuess==1 and sec_num>guess)or (nGuess==1 and sec_num<guess):
            print(f'you have {nGuess} guess available.')
            

else:
     print(f'\n\nsorry.  No more guesses are allowed.\n The secert number was {sec_num}') # prints the statement
       