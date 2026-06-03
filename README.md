# Tic-Tac-Toe Game

A command-line implementation of Tic-Tac-Toe demonstrating object-oriented design, persistent data management, and robust user input handling in Python.

## Why I Built This

I wanted to build something complete—not just a tutorial project, but an actual game you could play multiple times and it would remember the scores. It seemed simple enough to understand quickly, but complex enough to explore core programming concepts like classes, file handling, and error checking. Plus, I enjoyed the challenge of building something with a clear purpose that works reliably from start to finish.

## Features

- **Two-player gameplay** with custom player names and turn-based mechanics
- **Intelligent win/draw detection** using pattern matching against all 8 winning combinations
- **Persistent scoreboard** that automatically saves and loads player statistics between sessions via JSON
- **Robust input validation** with comprehensive error handling for invalid moves and out-of-range inputs
- **Intuitive board interface** with numbered positions (1-9) for easy move entry
- **Replay system** allowing multiple consecutive games with scoreboard tracking

## Technologies Used

- **Python 3** — Core language
- **JSON** — Data persistence for game statistics
- **Object-Oriented Programming** — Modular class-based architecture

## Project Structure

```
tic-tac-toe/
├── main.py          # Application entry point
├── game.py          # TicTacToe class with core game logic
├── player.py        # Player class for tracking player state
├── stats.json       # Persistent statistics storage
└── README.md        # Project documentation
```

### Key Files

| File         | Purpose                                                                              |
| ------------ | ------------------------------------------------------------------------------------ |
| `main.py`    | Initializes and runs the game                                                        |
| `game.py`    | Handles board management, move validation, win detection, and statistics persistence |
| `player.py`  | Represents individual players with name, symbol, and win count                       |
| `stats.json` | JSON file storing cumulative player wins and draws                                   |

## Installation

1. Ensure Python 3.6+ is installed:

   ```bash
   python --version
   ```

2. Clone or download this repository:

   ```bash
   git clone <repository-url>
   cd tic-tac-toe
   ```

3. No external dependencies required — only Python standard library (json module).

## Usage

Run the game from the command line:

```bash
python main.py
```

Follow the on-screen prompts to:

1. Enter names for Player 1 and Player 2
2. Select board positions (1-9) for each move
3. Continue playing or exit after each game

## Example Workflow

```
Welcome to Tic-Tac-Toe!

Enter Player 1 name (X): Alice
Enter Player 2 name (O): Bob

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Alice (X), choose a position (1-9): 5

 1 | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | 9

Bob (O), choose a position (1-9): 1

 O | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | 9

[Game continues...]

========================
      SCOREBOARD
========================
Alice (X): 5
Bob (O): 0
Draws: 0
========================

Would you like to play again? (y/n): n

Thanks for playing!
```

## Python Concepts Demonstrated

### Object-Oriented Programming

- **Class design**: Separate `Player` and `TicTacToe` classes with clear responsibilities
- **Encapsulation**: Game state and board logic contained within the `TicTacToe` class
- **Method organization**: Logical grouping of related operations (display, validation, state management)

### File Handling & Data Persistence

- **JSON serialization**: `json.dump()` and `json.load()` for reading/writing statistics
- **Exception handling**: Graceful fallback when `stats.json` doesn't exist on first run
- **File modes**: Read (`"r"`) and write (`"w"`) operations with proper resource management

### Input Validation & Error Handling

- **Try-except blocks**: Catches `ValueError` for non-integer inputs and `FileNotFoundError` for missing stats file
- **Range validation**: Ensures moves are within valid boundaries (1-9)
- **State validation**: Checks for occupied positions before placing moves
- **User feedback**: Clear error messages guide users toward correct input

### Game Logic & Algorithm Design

- **Win detection algorithm**: Checks 8 predefined winning combinations in O(1) constant time
- **State management**: Tracks current player, board state, and win counts efficiently
- **Turn switching**: Simple conditional logic for alternating between players

## Future Improvements

- **AI opponent** implementing minimax algorithm for single-player mode
- **Difficulty levels** with varied AI strategies (random, deterministic, optimal)
- **Game history** tracking individual game moves for replay functionality
- **Graphical user interface** using tkinter or pygame for enhanced user experience
- **Multiplayer networking** enabling remote games via socket communication
- **Performance metrics** analyzing winning strategies and common patterns
- **Unit tests** with pytest to ensure code reliability and maintainability

## Learning Outcomes

- Reinforced Python fundamentals including classes, control flow, and built-in functions
- Developed proficiency with JSON for persistence layer without external databases
- Practiced robust error handling and input validation for user-facing applications
- Applied object-oriented design principles to separate concerns and improve code maintainability
- Gained experience building complete, self-contained applications with proper state management

````

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
````

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
