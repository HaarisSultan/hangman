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
        """ Confirm if the guessed letter is in the word. 
        
            Updates the game state and gives the player feedback based on if their guess is correct or not. 

            Args:
                guess (str): the single letter guessed by the player
        """
        
        # convert the letter to lowercase 
        guess = guess.lower()
        
        if guess in self.word:
            
            print(f"\nGood guess! {guess} is in the word.")
            
            print(f"You have {self.num_lives} guesses left.\n")
        
            self.update_word_guessed(guess)
            
            print(f"{self.word_guessed}\n")
                    
        else:
            self.num_lives -= 1
            
            print(f"\nSorry, {guess} is not in the word.")
            
            print(f"You have {self.num_lives} guesses left.\n")
            
            print(f"{self.word_guessed}\n")

    def update_word_guessed(self, guess):
        """ Change the underscore list to reflect the correctly guessed letters 

            After each guess the user is shown a list e.g. ['t', '_', 'a', '_'] which shows their progress. This method updates that list based on the previous guess. 
        
            Args:
                guess (str): the (correct) guess the player just input 
        """
        
        for index, letter in enumerate(self.word):
            if letter == guess:
                # replace '_' with 'guess' to show user their progress 
                self.word_guessed[index] = guess 
                
        # update no. of letters still to be guessed, since game is over if this == 0 
        self.num_letters -= 1 
             
    def ask_for_input(self):
        
        while True:
            guess = input("Enter a letter: ")
            
            if len(guess) != 1 or not str.isalpha(guess):
                print("Invalid letter. Please, enter a single alphabetical character.\n")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!\n")
            else:
                # check if correct to update game state
                self.check_guess(guess)
                
                # store guessed letters in case the user tries it again 
                self.list_of_guesses.append(guess)
                
                # return to main game loop within play_game()
                break
    
                
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if num_lives == 0:
            print(f"You lost! The word was {game.word}")
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations! You won the game!")
            break

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
