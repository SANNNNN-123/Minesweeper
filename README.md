# Minesweeper Game

## Description
This project is a simple implementation of the classic Minesweeper game using Pygame library in Python. The game generates a grid of tiles, some of which contain hidden mines. The player must clear the grid without detonating any mines.

## Features
- Randomly generated minefield with adjustable size and bomb probability.
- Left-click to reveal a tile.
- Right-click to flag a tile suspected to contain a mine.
- Recursive tile clearing: if a cleared tile has no neighboring mines, adjacent tiles are automatically cleared.
- Game over detection: the game ends when a mine is detonated or all non-mine tiles are revealed.

## Files
1. **main.py:** This is the main script that initializes the game and handles the game loop.
2. **board.py:** Contains the Board class which represents the game board, including methods for generating the board, setting neighbors, handling user clicks, and checking game status.
3. **piece.py:** Defines the Piece class which represents individual tiles on the board, including attributes such as whether it contains a mine, whether it has been clicked, and its neighbors.
4. **game.py:** The Game class in game.py is responsible for managing the game loop, handling user input, and rendering the game graphics using Pygame. It interacts with the Board class to manage the game state.

## Run
To run the game, execute the `main.py` script using Python.
Left-click to reveal tiles and right-click to flag tiles suspected to contain mines.

## Credits
This project was created by [Zuhair Aziz].
