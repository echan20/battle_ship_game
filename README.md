# Battleship Game

## Overview

This is a classic Battleship game implemented in Python. Players take turns guessing the coordinates of their opponent's hidden ships on a grid. The goal is to sink all of the opponent's ships before they sink yours.

## Features

* **Menu-driven interface:** Easy navigation through game options including New Game, Resume Game, Instructions, and Quit
* **Instructions screen:** Clear explanation of game rules and controls
* **Configurable grid size:** Adjustable grid dimensions via `config.py`
* **Save/Load functionality:** Resume games from where you left off
* **Two-grid system:** View both your ships and the enemy's grid simultaneously
* **Ship placement phase:** Place your ships before starting the battle
* **Debug mode:** 
  - Show bot's boats in real-time
  - Debug prints for developers
* **Game statistics:** Track hits, misses, and boat status
* **Win conditions:** Clear indicators when you win or lose
* **Random bot actions:** The bot makes random attacks during its turn

## Usage

1. Make sure you have Python installed on your system
2. Download or clone this repository
3. Navigate to the project directory in your terminal
4. Run the game by executing the command: `python3 .`

## Game Flow

1. **Menu:** Choose between starting a new game, resuming a saved game, viewing instructions, or quitting
2. **Ship Placement:** Place your ships on the grid before the battle begins
3. **Battle Phase:** Take turns attacking the bot's grid
4. **Bot's Turn:** The bot makes random attacks after your turn
5. **Win/Lose:** The game ends when either you or the bot sinks all of each other's ships

## Configuration

The game can be customized through `config.py`:
- `GRID_SIZE_X` and `GRID_SIZE_Y`: Set the size of the game grid
- `AMOUNT_OF_BOATS`: Change the number of ships in the game
- `DEBUG_MODE`: Enable debug prints
- `DEBUG_SHOW_BOT_BOATS`: Show the bot's ship positions in real-time

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Author

echan20
