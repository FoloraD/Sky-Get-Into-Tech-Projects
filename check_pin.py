# Write a Python program that emulates the high-street bank mechanism for checking a
# PIN. Keep taking input from the keyboard (see below) until it is identical to a password
# number which is hard-coded by you in the program.
# Restrict the number of attempts to 3 (be sure to use a variable for that, we may wish to
# change it later), and output a suitable message for success and failure. Be sure to
# include the number of attempts in the message.

# SOLUTION: Use loop control statement (see pg 11 of conditionals handout.)
correct_pin = '1234'
count = 0   # assigning the variable to count PIN attempts

while count < 3:        # This loop will go 3 times.
    supplied_pin = input("Enter your PIN: ")   # supplied PIN variable will capture the PIN that is typed by the user.
    if supplied_pin == correct_pin:                 # If the CORRECT PIN is entered, print 'Correct PIN entered'
        print('Correct PIN entered')
        break                                               # exit the loop closes(breaks) if the correct PIN is entered
    #elif count <= 1 and count <= 3:       #look at counter                  # if incorrect and this is either the 1st or 2nd attempt
        count += 1                                           # an attempt is added to count
        print('Invalid PIN entered. Please try again. You have', {3 - count}, 'attempt(s) left') #improve hard code
        # error message gets printed which shows how many attempts remaining
    else:       # at the third attempt the message below gets printed
        print("Attempts exhausted. This account is locked.")
        break
