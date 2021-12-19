from words import word_list
from picture import display_hangman
import random

#driver from here on down
def main():
    playAgain = True

    while playAgain:
        print()
        print()
        print()
        print()

        play(word = getWord().upper())

        print()

        again = input("Would you like to play again? Y/N: ").upper()
        
        while len(again) != 1 and not(again.isalpha()) and (again != "Y" or again != "N"):
            again = input("Would you like to play again? Y/N: ").upper()

        if again == "N":
            playAgain = False
        else:
            playAgain = True

        if playAgain == False:
            print("Thanks for playing")


def getWord():
    return random.choice(word_list)

def play(word):
    tries = 6
    underScore = "_ " * len(word)
    printWord = [" "] * len(word)

    userLetter = []
    userWord = []
    found = False

    while tries > 0:
        print(display_hangman(tries))
        
        for val in printWord:
            print(val, end = " ")
        
        print()
        print(underScore)
        print()
        print("Number of tries left: ", tries)
        print()
        userInput = input("Guess a letter in the word or the word: ").upper()
        print()

        if len(userInput) == len(word):

            if userInput in userWord:
                print("Word has already been used")

            elif userInput.isalpha():
                userWord.append(userInput)

                if userInput == word:
                    for i in range(0, len(word)):
                        print(word[i], end = " ")
                
                    print()
                    print(underScore)
                    found = True
                    break

            else:
                print("Input contains invalid letters")

        elif len(userInput) == 1:

            if userInput in userLetter:
                print("Letter has already been used")

            elif userInput.isalpha():
                userLetter.append(userInput)

                if userInput in word:
                    for i in range(0, len(word)):
                        if word[i] == userInput:
                            printWord[i] = userInput

                for val in printWord:
                    print(val, end = " ")

                print()
                print(underScore)  

            else:
                print("Input contains invalid letters")

        else:
            print("Invalid input. Input must be either a letter or a word with the same number of letters as the number of underscores")

        if printWord == list(word):
            found = True
            break

        print()
        print()
        print()
        print()

        tries -= 1

    print()

    if found == True:
        print("Good job, you've escaped certain death!")
    else:
        print("R.I.P. The word was: ", word)

main()