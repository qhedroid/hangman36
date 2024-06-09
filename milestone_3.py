def check_guess(guess, word):
    """
    This function checks if the guessed letter is in the word.
    """
    # Convert the guess to lower case
    guess = guess.lower()

    # Check if the guess is in the word
    if guess in word:
        # If the guess is in the word, print a success message
        print(f"Good guess! '{guess}' is in the word.")
    else:
        # If the guess is not in the word, print an error message
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input(word):
    """
    This function continuously asks the user for a valid guess and checks it.
    """
    while True:
        # Ask the user to guess a letter and assign this to a variable called guess
        guess = input("Please enter a single letter: ")

        # Check that the guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            # If the guess passes the checks, break out of the loop
            print("Good guess!")
            break
        else:
            # If the guess does not pass the checks, print a message
            print("Invalid letter. Please, enter a single alphabetical character.")

    # Call the check_guess function to check if the guess is in the word
    check_guess(guess, word)

# Example word for testing
word = 'apple'

# Call the ask_for_input function to test your code
ask_for_input(word)