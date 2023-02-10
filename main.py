import random


choices = ['Rock', 'Paper', 'Scissors']  # Options for rock paper scissors game
userWin = None                           # whether user wins or not
draw = None                              # whether user draws or not

displayDraw = "It's a Draw!"             # display that user draws
displayWin = 'You Win!'                  # display that user wins
displayLose = 'You Lose!'                # display that user loses
playAgain = 'y'                          # to play game again

userInput = input('Rock, Paper, or Scissors?\n')  # ask player for input

while userInput.capitalize() not in choices:     # check if player input an existing option
    if userInput != 'q':
        userInput = input('That was not an option. Please try again.\n')
    else:
        exit()

compChoice = random.choice(choices)  # have computer choose a random option

while playAgain != 'n':
    print('\nYou played: ' + userInput.capitalize())  # display player input
    print('The computer played: ' + compChoice)  # display computer choice

    if compChoice == 'Rock' and userInput.capitalize() == 'Rock':  # check draw conditions
        draw = True
    elif compChoice == 'Paper' and userInput.capitalize() == 'Paper':
        draw = True
    elif compChoice == 'Scissors' and userInput.capitalize() == 'Scissors':
        draw = True

    if compChoice == 'Rock' and userInput.capitalize() == 'Paper':  # check win conditions
        userWin = True
    elif compChoice == 'Rock' and userInput.capitalize() == 'Scissors':
        userWin = False
    elif compChoice == 'Paper' and userInput.capitalize() == 'Rock':
        userWin = False
    elif compChoice == 'Paper' and userInput.capitalize() == 'Scissors':
        userWin = True
    elif compChoice == 'Scissors' and userInput.capitalize() == 'Rock':
        userWin = True
    elif compChoice == 'Scissors' and userInput.capitalize() == 'Paper':
        userWin = False

    if userWin is True:                # display win, lose, or draw
        print('\n' + displayWin)
    elif userWin is False:
        print('\n' + displayLose)
    if draw:
        print('\n' + displayDraw)

    playAgain = input('\nWould you like to play again? (y/n)\n')  # ask if player wants to play again

    while playAgain not in ('y', 'n', 'Y', 'N'):  # check if player input an existing option
        playAgain = input('That was not an option. Type y to play again or n to quit.\n')

    if playAgain in ('y', 'Y'):
        userInput = input('Rock, Paper, or Scissors?\n')  # ask player for input
        while userInput.capitalize() not in choices:                      # check if player input an existing option
            userInput = input('That was not an option. Please try again.\n')

        compChoice = random.choice(choices)  # have computer choose a random option
        draw = None
        userWin = None
    elif playAgain in ('n', 'N'):
        exit()

