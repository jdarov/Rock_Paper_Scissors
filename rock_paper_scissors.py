"""
Welcome to Rock Paper Scissors! 

This program takes a user input (rock, paper, scissors)
A random computer input of the same 3 choices 
And determines a winner:rock > scissors, scissors > paper, paper > rock
Print the winner and save it to persistent memory along with choices
Asks user if they would like to play again or load saved data
"""
import random

VALID_CHOICES = ['rock', 'paper', 'scissors']
CONTINUE_PROMPT = "Do you want to play again? ('y' for yes or 'n' for no)"
END_PROGRAM = {'n', 'no', 'stop', 'quit', 'exit', 'end'}
GAME_HISTORY = []

def point_to_prompt(prompt):
    """
    Returns the message with a preceding arrow 
    Helps to distinguish from terminal output and user input
    """
    print(f'==> {prompt}')

def will_continue(message):
    """
    Function to validate user input if they wish to continue
    Repeat until returns a correct user input of 'n' or 'no' 
    param: message, the message printed to the user requesting input
    """
    while True:
        point_to_prompt(message)
        user_choice = input().strip().lower()
        if user_choice in {'y', 'yes'}:
            return True
        if user_choice in END_PROGRAM:
            return False
        point_to_prompt('That was not a valid choice!')

def display_winner(player, computer):
    """
    Display choices and result of game in a clean way
    Return a 'win', 'loss', or 'tie' to save to outside file
    param: player, the player's choice (rock, paper, scissors)
    computer, the computer's choice (rock, paper, scissors)
    """
    #to reduce characters in prompt
    play = player.title()
    comp = computer.title()
    point_to_prompt(f'You chose {play}, computer chose {comp}\n')

    wins_against = {
        'rock':'scissors',
        'scissors':'paper',
        'paper':'rock'
    }
    if player == computer:
        point_to_prompt("It's a tie! That will happen 1/3 times. TRY AGAIN!\n")
        return 'tie'
    if wins_against[player] == computer:
        point_to_prompt('YOU WON! CONGRATULATIONS!\n')
        return 'win'
    point_to_prompt('You are a LOSER! Better luck next time!\n')
    return 'lose'


while True:
    point_to_prompt(f'Choose one: {', '.join(VALID_CHOICES)}')
    choice = input().strip().lower()
    if choice in END_PROGRAM:
        break

    while choice not in VALID_CHOICES:
        point_to_prompt("That's not a valid choice!")
        point_to_prompt("Please pick: rock, paper, scissors")
        choice = input().strip().lower()

    computer_choice = random.choice(VALID_CHOICES)

    WINNER = display_winner(choice, computer_choice)
    GAME_HISTORY.append({
        'user_choice': choice,
        'computer_choice': computer_choice,
        'result': WINNER,
    })

    if not will_continue(CONTINUE_PROMPT):
        point_to_prompt("Game History this round:\n")
        for i, game in enumerate(GAME_HISTORY, 1):
            print(f'Round {i}: You chose {game['user_choice']}, '
                  f'Computer chose {game['computer_choice']}, '
                  f'Result: {game['result'].upper()}')
        break

    #add a way to distinguish the different rounds
    print("\n" + "="*40 + "\n") 