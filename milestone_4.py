import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list).lower()  # The word to be guessed, picked randomly from the word_list
        self.word_guessed = ['_'] * len(self.word)  # List of the letters of the word with _ for each letter not yet guessed
        self.num_letters = len(set(self.word))  # Number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives  # Number of lives the player has at the start of the game
        self.word_list = word_list  # List of words
        self.list_of_guesses = []  # List of guesses that have already been tried

    def check_guess(self, guess):
        """
        This method checks if the guessed letter is in the word.
        """
        # Convert the guessed letter to lower case
        guess = guess.lower()

        # Check if the guess is in the word
        if guess in self.word:
            # If the guess is in the word, print a success message
            print(f"Good guess! '{guess}' is in the word.")
            # Create a for-loop that will loop through each letter in the word
            for index, letter in enumerate(self.word):
                # If the letter is equal to the guess, replace the corresponding "_" in word_guessed
                if letter == guess:
                    self.word_guessed[index] = guess
            # Decrease the number of unique letters by 1
            self.num_letters -= 1
        else:
            # If the guess is not in the word, reduce num_lives by 1
            self.num_lives -= 1
            # Print a message indicating the guess is not in the word
            print(f"Sorry, '{guess}' is not in the word.")
            # Print the number of lives left
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        This method continuously asks the user for a valid guess and checks it.
        """
        while True:
            # Ask the user to guess a letter and assign this to a variable called guess
            guess = input("Please enter a single letter: ")

            # Check that the guess is a single alphabetical character
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                # Append the guess to the list_of_guesses
                self.list_of_guesses.append(guess)
                # Call the check_guess method to check if the guess is in the word
                self.check_guess(guess)
                break

# Example word list for testing
word_list = ['Apple', 'Oranges', 'Mango', 'Pineapple', 'Strawberry']

# Create an instance of the Hangman class
hangman_game = Hangman(word_list)

# Call the ask_for_input method to test your code
hangman_game.ask_for_input()

# Print the current state of the word_guessed
print(f"Word guessed so far: {' '.join(hangman_game.word_guessed)}")
print(f"Number of lives remaining: {hangman_game.num_lives}")
print(f"List of guesses: {hangman_game.list_of_guesses}")