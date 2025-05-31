"""
File to help import/export data from main RPS program to JSON file
Used to save games, delete all saves and retrieve save information
Retrieve info such as # of times won with rock, paper, scissors, etc
"""
from collections import defaultdict
import json
import os

FILE_NAME = 'rps_save_data.json'
VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
VALID_RESULTS = ['win', 'lose', 'tie']

def load_saved_data():
    """
    Load existing data from JSON
    Used to pull dictionaries from JSON list of saved data
    """
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def clear_saves():
    """
    Function to empty and clear out the list in the JSON file
    Empty all saved data and start new list
    """

    with open(FILE_NAME, 'w') as file:
        json.dump([], file)

def save_data(user_choice, computer_choice, result):
    """
    Save data from program in JSON file
    Take data as params and write this data as a dict in the JSON list
    PARAMS: user_choice: the user choice of rock, paper, scissors
    computer_choice: the computer's choice of rock, paper, scissors
    result: the result of the game (win, lose, tie)
    """
    saved_data = load_saved_data()

    saved_data.append({
        'user_choice': user_choice,
        'computer_choice' : computer_choice,
        'result' : result
    })

    with open(FILE_NAME, 'w') as file:
        json.dump(saved_data, file, indent=4)

def return_saved_data():
    """
    Take saved data and return a new string that displays:
    Number of wins, losses and ties with each pick (rock, paper, scissors)
    """
    stats = defaultdict(lambda: {'win': 0, 'lose': 0, 'tie': 0})

    for data in load_saved_data():
        choice = data['user_choice']
        result = data['result']
        if choice in VALID_CHOICES and result in VALID_RESULTS:
            stats[choice][result] += 1

    ouput = []
    for choice in VALID_CHOICES:
        ouput.append(f'{choice.upper()}: \n'
                     f'    total wins: {stats[choice]['win']}\n'
                     f'    total losses: {stats[choice]['lose']}\n'
                     f'    total ties: {stats[choice]['tie']}\n'
                     )
    return ''.join(ouput)