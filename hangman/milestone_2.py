import random 

word_list = ['mango', 'banana', 'papaya', 'orange', 'watermelon']

word = random.choice(word_list)

guess = input("Enter a letter: ")

if len(guess) == 1 and str.isalpha(guess):
    print("Good guess!")
else:
    print("Oops! That's not a valid input.")
    