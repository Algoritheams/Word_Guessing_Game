# Geospatial Word Guessing Game

## Introduction
Welcome to the Geospatial Word Guessing Game! This Python program is a simple word guessing game where you try to identify a geospatial term randomly selected from a predefined list. The game provides an engaging way to test your knowledge of geospatial concepts related to cartography, GIS, geomatics, and more.

## How to Play
1. Run the `geospatial_word_guess_game()` function to start the game.
2. You will be presented with a geospatial term represented by underscores, each representing a letter in the term.
3. Guess letters one at a time by entering them when prompted. The game will inform you if the letter is correct or not.
4. You have a maximum of 3 incorrect guesses before the game ends.
5. The game continues until you either correctly guess the entire geospatial term or exhaust your allowed incorrect guesses.

## Code Structure
- `choose_geospatial_word()`: Selects a random geospatial term from a predefined list.
- `display_word(secret_word, guessed_letters)`: Displays the current state of the geospatial term with correctly guessed letters revealed.
- `calculate_score(secret_word, guessed_letters, incorrect_guesses)`: Calculates the player's score based on correct guesses, incorrect guesses, and remaining uncovered letters.
- `geospatial_word_guess_game()`: Main function orchestrating the game, taking user input and managing game flow.

## Running the Code
Ensure you have Python installed on your system. Run the script and follow the on-screen instructions.

```bash
python geospatial_word_guess.py
```

## Winning and Losing
- If you correctly guess the entire geospatial term within 3 incorrect guesses, you win.
- If you exceed the allowed incorrect guesses, the correct geospatial term is revealed, and you lose.

## Scoring
Your score is calculated based on the number of correct guesses, incorrect guesses, and uncovered letters. The maximum score is 10.

## Have Fun!
Enjoy playing the Geospatial Word Guessing Game and test your knowledge of geospatial terms. Feel free to modify the code or expand the list of geospatial words for a more challenging experience. Happy guessing!
