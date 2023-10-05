import random
import time

guess = 0
numberg = 10

print("Guess a number between 1 and 5\n")

while guess != numberg:
    guess = input("Guess ")
    numberg = random.randrange(1,6)
    time.sleep(0.5)
    if int(guess) == int(numberg):
        print("Correct")
        print("You win")
        break
    else:
        print("Incorrect, the answer was " + str(numberg) + ", try again.")



exit()