"""
Welcome to Rock Paper Scissors! 

This program takes a user input (rock, paper, scissors)
A random computer input of the same 3 choices 
And determines a winner:
Rock beats paper, paper beats rock, scissors beats paper

Print the winner and save it to persistent memory along with choices
Asks user if they would like to play again or load saved data
First to 5 wins is the Grand Winner!
"""
import random
from rps_save_config import (
    clear_saves,
    save_data,
    return_saved_data
)

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
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
    PARAM: message, the message printed to the user requesting input
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
    PARAM: player, the player's choice (rock, paper, scissors)
    computer, the computer's choice (rock, paper, scissors)
    """
    #to reduce characters in prompt
    play = player.upper()
    comp = computer.upper()
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

    RESULT = display_winner(choice, computer_choice)
    GAME_HISTORY.append({
        'user_choice': choice,
        'computer_choice': computer_choice,
        'result': RESULT,
    })
    save_data(choice, computer_choice, RESULT)

    if not will_continue(CONTINUE_PROMPT):
        point_to_prompt("Game History this round:")
        for i, game in enumerate(GAME_HISTORY, 1):
            print(f'Round {i}: You chose {game['user_choice'].upper()}, '
                  f'Computer chose {game['computer_choice'].upper()}, '
                  f'Result: {game['result'].upper()}\n')

        point_to_prompt('Please type: ')
        point_to_prompt('1 to view your saved game history')
        point_to_prompt('2 to clear out all your saves')
        point_to_prompt('or n to quit? ')
        save_choice = input()

        while save_choice not in END_PROGRAM:
            match save_choice:
                case '1':
                    print(return_saved_data())
                    break
                case '2':
                    clear_saves()
                    break
                case _:
                    print('That was not a valid option.')
                    save_choice = input('Please pick 1, 2 or n to quit: ')
        break

    #add a way to distinguish the different rounds
    print("\n" + "="*40 + "\n") 