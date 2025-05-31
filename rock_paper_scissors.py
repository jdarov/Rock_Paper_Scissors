"""
Rock Paper Scissors Lizard Spock - Terminal Game
------------------------------------------------

This Python program is a command-line implementation of the extended 
Rock Paper Scissors game made famous by "The Big Bang Theory." It includes 
support for five choices: rock, paper, scissors, lizard, and spock.

Features:
- Accepts both full and short-form user input ('r' for rock, etc)
- Tracks and displays player vs. computer results
- Declares a Grand Winner when a player reaches 5 wins
- Persists round history to a JSON file for long-term game tracking
- Offers options to view or clear saved game data
- Fully modular and lint-compliant, suitable for Launch School submissions

Author: Joshua Darovitz
"""

import random
from rps_save_config import (
    clear_saves,
    save_data,
    return_saved_data
)

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

#Short form mappings:
# r=rock, p=paper, sc=scissors, l=lizard, sp=spock, s=clarify
SHORT_CHOICES = {'r', 'p', 'sc', 'l', 'sp', 's'}

CONTINUE_PROMPT = "Do you want to play again? ('y' for yes or 'n' for no)"

END_PROGRAM = {'n', 'no', 'stop', 'quit', 'exit', 'end'}

GRAND_WINNER = 'GRAND WINNER: PLAYER....CONGRATULATIONS!'
GRAND_LOSER = 'GRAND WINNER: COMPUTER....How hard is it to beat a computer?'

WIN_LIMIT = 5

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

def return_long_from_short(play_choice):
    """
    Checks if player chose a short answer from SHORT_CHOICES
    r: rock, l: lizard, p:paper, sp:spock, sc:scissors
    s: Asks user to clarify spock or scissors, repeats invalid choices
    If user's choice was already valid, returns that choice
    PARAM: play_choice: the players choice from the game
    
    """
    if play_choice in SHORT_CHOICES:
        while play_choice == 's':
            play_choice = input('Did you mean spock(sp) or scissors(sc)? ')
            if play_choice not in {'spock', 'scissors', 'sp', 'sc'}:
                print("That wasn't a valid clarification")
                play_choice = 's'
        for choice in VALID_CHOICES:
            if choice.startswith(play_choice):
                return choice.lower()
    return play_choice.lower()

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
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard' : ['spock', 'paper'],
        'spock' : ['scissors', 'rock']
    }
    if player == computer:
        point_to_prompt("It's a tie! That will happen 1/3 times. TRY AGAIN!\n")
        return 'tie'
    if computer in wins_against[player]:
        point_to_prompt('YOU WON! CONGRATULATIONS!\n')
        return 'win'
    point_to_prompt('You are a LOSER! Better luck next time!\n')
    return 'lose'

def print_game_history(history):
    """
    Prints Game History
    Displays player_choice, computer_choice and result for each round
    """
    point_to_prompt("Game History this round:")
    for i, game in enumerate(history, 1):
        print(f"Round {i}: You chose {game['user_choice'].upper()}, "
              f"Computer chose {game['computer_choice'].upper()}, "
              f"Result: {game['result'].upper()}")

def end_of_game(game_results):
    """
    Function to determine if the user wants to continue or end the game
    If user decides to quit, will let them choose to:
    1. Display all saved data from all games played in history
    2. Clear all their save data
    3. Exit out of the game
    """
    if not will_continue(CONTINUE_PROMPT):
        print_game_history(game_results)

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
        return True
    return False

def get_valid_player_choice():
    """
    Prompt player for a valid choice, accepting short forms 
    and handling invalid input.
    Returns: full-form validated choice (e.g. 'rock', 'spock')
    """
    while True:
        point_to_prompt(f"Choose one: {', '.join(VALID_CHOICES)}")
        choice = input().strip().lower()

        if choice in END_PROGRAM:
            return choice  #End main loop at anytime

        full_choice = return_long_from_short(choice)

        if full_choice in VALID_CHOICES:
            return full_choice

        point_to_prompt("That's not a valid choice! Try again.")

def main():
    player_wins = 0
    player_loss = 0
    game_history = []

    while True:

        round_number = len(game_history) + 1
        print(f"\n==== ROUND {round_number} ====")

        player_choice = get_valid_player_choice()
        if player_choice in END_PROGRAM:
            break
        
        computer_choice = random.choice(VALID_CHOICES)

        result = display_winner(player_choice, computer_choice)

        if result == 'win':
            player_wins += 1
        elif result == 'lose':
            player_loss +=1

        game_history.append({
            'user_choice': player_choice,
            'computer_choice': computer_choice,
            'result': result,
        })
        save_data(player_choice, computer_choice, result)

        if player_wins == WIN_LIMIT:
            print('='*70)
            point_to_prompt(GRAND_WINNER)
            print('='*70)
            player_wins = 0
            if end_of_game(game_history):
                break
        elif player_loss == WIN_LIMIT:
            print('='*70)
            point_to_prompt(GRAND_LOSER)
            print('='*70)
            player_loss = 0
            if end_of_game(game_history):
                break

        #add a way to distinguish the different rounds
        print("="*55)

if __name__ == '__main__':
    main()
