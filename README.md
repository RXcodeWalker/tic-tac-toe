# Tic-Tac-Toe (Python)

## Overview

This project is a command-line Tic-Tac-Toe game built in Python using object-oriented programming principles. It supports two human players, tracks scores across multiple games, and stores statistics permanently using a JSON file.

The project was created to practice Python programming concepts such as classes, functions, file handling, error handling, game state management, and data persistence.

---

## Features

### Core Gameplay

- Two-player Tic-Tac-Toe
- Turn-based gameplay
- Win detection
- Draw detection
- Input validation
- Replay system

### Player System

- Custom player names
- Player symbols (X and O)
- Individual win tracking

### Scoreboard

- Displays wins for each player
- Tracks total draws
- Updates automatically after every game

### Persistent Statistics

- Saves game statistics to a JSON file
- Loads statistics automatically when the game starts
- Preserves scores between program runs

### User Experience Improvements

- Numbered board positions (1–9)
- Clear game status messages
- Improved scoreboard formatting
- Friendly error messages

---

## Project Structure

```text
tic-tac-toe/
│
├── main.py
├── game.py
├── player.py
├── stats.json
├── README.md
└── __pycache__/
```

### File Descriptions

#### main.py

Application entry point. Creates a game object and starts the program.

#### game.py

Contains the main game logic:

- Board management
- Move validation
- Win detection
- Draw detection
- Scoreboard
- Statistics loading/saving

#### player.py

Defines the Player class.

Each player stores:

- Name
- Symbol
- Win count

#### stats.json

Stores persistent game statistics.

Example:

```json
{
  "player1_wins": 5,
  "player2_wins": 3,
  "draws": 2
}
```

---

## Concepts Demonstrated

This project demonstrates the following Python concepts:

### Object-Oriented Programming

- Classes
- Objects
- Constructors (`__init__`)
- Instance attributes
- Methods

### Data Structures

- Lists
- Dictionaries

### Control Flow

- Loops
- Conditionals
- Boolean logic

### Error Handling

- `try`
- `except`
- Input validation

### File Handling

- Reading files
- Writing files
- Context managers (`with open()`)

### JSON

- Serialization
- Deserialization
- Persistent storage

---

## How the Game Works

1. Players enter their names.
2. The board is displayed.
3. Players alternate turns.
4. The game checks for:
   - Wins
   - Draws

5. Scores are updated.
6. Statistics are saved to `stats.json`.
7. Players can choose to play again.

---

## Example Board

```text
 X | 2 | O
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | O
```

Numbers represent available positions.

---

## Installation

### Requirements

- Python 3.10 or later

### Run the Project

```bash
python main.py
```

---

## Example Gameplay

```text
Enter Player 1 name (X): Om
Enter Player 2 name (O): Alex

========================
      TIC TAC TOE
========================

Om's turn (X)

 X | 2 | O
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | O

Choose a position (1-9): 7
```

---

## Future Improvements

Planned enhancements include:

- Human vs Computer mode
- AI opponent
- Difficulty levels
- Save/load game states
- Graphical user interface (GUI)
- Unit testing
- Online multiplayer support

---

## What I Learned

Through this project I practiced:

- Designing a complete application from scratch
- Organizing code using classes
- Managing program state
- Validating user input
- Working with JSON data
- Persisting information between program runs
- Building a user-friendly command-line application

```

```

Credits: I used ChatGPT by OpenAI to enhance this readME file and to format it better.
