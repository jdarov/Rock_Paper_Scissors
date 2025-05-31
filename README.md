# 🪨📄✂️🦎🖖 Rock Paper Scissors Lizard Spock (Terminal Game)

Welcome to **Rock Paper Scissors Lizard Spock**, a Python terminal game that expands the classic RPS game with extra strategy, persistent game history, short input handling, and a race to become the **Grand Winner**!

> "Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock... and so on. But what if there was more?"

Inspired by *The Big Bang Theory*, this project adds **Lizard** and **Spock** to the mix for maximum chaos and fun.

---

## 🚀 Features

- 🧠 Intelligent short-input parser (`r`, `sc`, `sp`, etc.)
- 💾 Save game data to JSON for persistent history
- 🏆 First to 5 wins is crowned the **Grand Winner**
- 📜 View or clear saved match history
- 💬 Friendly and funny prompts
- 🎯 Clean modular Python code

---

## 🎮 How to Play

1. Clone the repo
2. Run the game using Python 3.10+
3. Choose your weapon (rock, paper, scissors, lizard, or spock)
4. First to 5 wins is declared Grand Champion!
5. After quitting, you can view or clear your saved games

```bash
git clone https://github.com/jdarov/rps-lizard-spock.git
cd rps-lizard-spock
python3 rock_paper_scissors.py
```

---

## 🧩 Game Logic

```
SCISSORS cuts PAPER
PAPER covers ROCK
ROCK crushes LIZARD
LIZARD poisons SPOCK
SPOCK smashes SCISSORS
SCISSORS decapitates LIZARD
LIZARD eats PAPER
PAPER disproves SPOCK
SPOCK vaporizes ROCK
ROCK crushes SCISSORS
```

---

## 🧠 Functions Breakdown

### `point_to_prompt(prompt)`
Prefixes a user prompt with `==>` to make it clear and readable.

### `will_continue(message)`
Prompts the user with a yes/no message. Returns `True` to continue or `False` to end the game.

### `return_long_from_short(play_choice)`
Converts short inputs like `'r'`, `'sc'`, `'sp'`, etc. into the full choice (`'rock'`, `'scissors'`, `'spock'`).

### `display_winner(player, computer)`
Compares player and computer choices and returns the result (`'win'`, `'lose'`, `'tie'`).

### `print_game_history()`
Prints the current round’s history with all moves and outcomes.

### `end_of_game()`
Runs when the player chooses to quit. Prompts to view or clear saved game history from previous sessions.

---

## 🗃 Save System

Game outcomes are saved in a JSON file using helper functions from `rps_save_config.py`:

- `save_data()`: Save each round
- `return_saved_data()`: Load all past games
- `clear_saves()`: Erase saved history

---

## 📁 File Structure

```
rps-lizard-spock/
│
├── rock_paper_scissors.py # Main game logic
├── rps_save_config.py     # Save/load/clear JSON data
├── saved_games.json       # (auto-created) Stores match history
└── README.md              # You're reading it!
```

---

## 🧪 Example Output

```
==> Choose one: rock, paper, scissors, lizard, spock
> r
==> You chose ROCK, computer chose SPOCK

==> You are a LOSER! Better luck next time!

==> Do you want to play again? ('y' for yes or 'n' for no)
> n

==> Game History this round:
Round 1: You chose ROCK, Computer chose SPOCK, Result: LOSE

==> 1 to view saved history
==> 2 to clear all saves
==> or n to quit?
```

---

## 🛠 Future Ideas

- Add multiplayer support
- Add score persistence across sessions
- Convert to a GUI (Tkinter, PyQt) or web version (Flask)

---

## 📣 Author

**Joshua Darovitz**  
📍 From Truck Driver to Software Engineer  
🎥 [Hello World, Goodbye Trucking!](https://www.youtube.com/@jdarov)
🛠 GitHub: [@jdarov](https://github.com/jdarov)

---

## 🌟 Show Your Support

If you like this game:
- ⭐ Star the repo
- 🐛 Submit feedback or bugs
- 🧪 Try beating Spock... if you dare

---

> “Scissors decapitates Lizard. Lizard eats Paper. Spock vaporizes Rock. Rock crushes Scissors... I lose.”  
— Sheldon Cooper