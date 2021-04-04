import random
print ("Welcome to guess the number game.\n")
guess = int (input ("Please enter your guess: "))

number = random.randint(1, 6)

while guess != number:
    print("Please try again")
    guess = int (input("Enter your next guess: "))

print ("You have guessed correctly! Congratulations! \n")
