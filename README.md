# Puzzle Game

This is a simple puzzle game built using Python, Pygame, and PIL (Python Imaging Library). The game loads an image, splits it into smaller pieces, shuffles them, and displays them on the screen. The objective is to rearrange the pieces to form the original image.

## Features

- Load an image and split it into smaller pieces.
- Shuffle the pieces randomly.
- Display the shuffled pieces on the screen.

## Requirements

- Python 3.x
- Pygame
- Pillow (PIL)

## Installation

1. Clone the repository or download the source code.

```sh
git clone https://github.com/yourusername/puzzle-game.git
cd puzzle-game
```

2. Install the required Python packages.

```sh
pip install pygame pillow
```

## Usage

1. Place the image you want to use for the puzzle in the project directory and update the image_path variable in app.py with the image file name.

```python
image_path = 'your_image.png'  # Update this line with your image file name
```

2. Run the game.

```
python app.py
```

## How to Play

- The game will start with the image pieces shuffled.
- Your goal is to rearrange the pieces to form the original image.
- Currently, the game only displays the shuffled pieces. You can extend the functionality to allow piece swapping or dragging to solve the puzzle.

## Project Structure

```
app.py: The main game script.
README.md: This file.
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
