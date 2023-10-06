import random 

class Hangman():
    def __init__(self, word_list, num_lives=5):
        # the words from which the game will select the target word 
        self.word_list = word_list 
        self.num_lives = num_lives
        
        # select a word to guess randomly 
        self.word = random.choice(word_list)
        
        # generate a list of underscores to represent progress 
        self.word_guessed = ['_' for i in self.word]
        
        # list of unique letters still to be guessed 
        self.num_letters = len(set(self.word))
        
        # letters the player has tried
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        """Confirm if the guessed letter is in the word 
        
        Updates the game state and gives the player feedback based on if their guess is correct or not. 

        Args:
            guess (str): the single letter guessed by the player
        """
        
        # convert the letter to lowercase 
        guess = guess.lower()
        
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess 
            self.num_letters -= 1
                    
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} left.")
            
    def ask_for_input(self):
        while True:
            guess = input("Enter a letter: ")
            
            if len(guess) != 1 or not str.isalpha(guess):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                
game = Hangman(['mango', 'banana', 'papaya', 'orange', 'watermelon'])
game.ask_for_input()