# Word Blitz Assistant
I'm really bad at word blitz... and this totally isn't cheating :)

## Description
Word Blitz is a word game on Facebook messenger that is a cross between Boggle and Word with Friends - the player searches for words that can be constructed from sequentially adjacent tiles. Different words have different point values based on the letter, length of the word and various bonuses associated with a tile i.e. double letter, triple letter, double word, ...

## Setup
1. Clone this repo.
1. `Pip install -r requirements.txt`
1. Perform additional installation and setup for Python Tesseract and PyAutoGUI
1. For more consistent performance, maximize your browser window and input pixel locations for the bounding box of the word board.

## How the Program Works
At a high level, the program does the following:
1. Take a screenshot
1. Perform OCR on the image to extract the letters on the board
1. Search for words
1. Control the mouse to import words into the game.

## To-do?
- Refactoring
- Read and make use of bonus scoring (dl, tl, dw, ...)
- Find a more complete dictionary
