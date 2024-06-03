import random

# Create a list containing the names of your 5 favorite fruits
favorite_fruits = ['Apple', 'Oranges', 'Mango', 'Pineapple', 'Strawberry']

# Assign this list to a variable called word_list
word_list = favorite_fruits

# Print out the newly created list to the standard output (screen)
print(word_list)

# Create the random.choice method and pass the word_list variable into the choice method.
word = random.choice(favorite_fruits)

# Print out word to the standard output. Run the code several times and observe the words printed out after each run.
print(word)

# Using the input function, ask the user to enter a single letter.
guess = input("Please enter a single letter: ")

# Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")