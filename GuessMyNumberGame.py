import random
print ("Welcome to guess the number game.\n")
guess = int (input ("Please enter your guess: "))
# TODO: Think of using break and continue
number = random.randint(1, 6)

while guess != number:
    print("Please try again")
    guess = int (input("Enter your next guess: "))

print ("You have guessed correctly! Congratulations! \n")


message = input("Enter a message: ")
new_message = ""
VOWELS = "aeiou"

print()
for letter in message:
        if letter.lower() not in VOWELS:
            new_message += letter
            print ("A new string has been created: ", new_message)
print ("\n Your message without vowels: ", new_message)

input("Enter a key to exit.")