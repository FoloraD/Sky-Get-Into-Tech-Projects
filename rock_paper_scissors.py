# Import random module import random


# Function for user input
def allocate_user_input(user_input_letter):
    if user_input_letter == 'R':
        return 'Rock'
    elif user_input_letter == 'S':
        return 'Scissors'
    elif user_input_letter == 'P':
        return 'Paper'
    else:
        return 'You have selected an invalid character. Please choose R (rock), P (paper) or S (scissors) to play!'