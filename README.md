# Geomatics_Engineering_Word_Guessing_Game


Welcome to the Geomatics Engineering Word Guessing Game, a captivating and educational experience designed for enthusiasts of geomatics engineering terminology. This Python-based game offers a unique twist on the classic word-guessing challenge by immersing players in the world of geomatics.

# How It Works:
In this engaging game, players are presented with a randomly generated 4-letter geomatics engineering word from a carefully curated list. The challenge begins as players attempt to guess the entire word or individual letters until they either correctly identify the word or decide to conclude the round.

# Scoring Mechanism:
The scoring system adds an exciting dimension to the game. Points are calculated based on the letters correctly guessed and the frequency of requests for additional letters. Incorrect guesses incur a penalty, costing the player 10% of the current word's score. If a player chooses to give up, the points lost correspond to the sum of the uncovered letters.

# Educational Aspect:
As players delve into the geomatics engineering lexicon, they not only enjoy a thrilling word-guessing experience but also gain exposure to terminology specific to the field. The game emphasizes the importance of letter frequencies in geomatics terms, providing a subtle learning opportunity within the context of entertainment.

# Documentation and Customization:
To ensure accessibility and clarity, Python-style documentation is provided for the system. The game can easily be customized by swapping the word file with another containing geomatics engineering words, allowing for a tailored and dynamic gaming experience.

Whether you are a seasoned geomatics professional or just curious about the terminology, the Geomatics Engineering Word Guessing Game promises entertainment, education, and a unique exploration of the language associated with geomatics engineering. Get ready to unravel the words that define the world of geospatial sciences!

# Geomatic Word Guessing Game

**Geomatic Word Guessing Game** is a Python-based word guessing game that utilizes a user-provided file containing 4030 4-letter geomatic words.

## Description

In this word guessing game, players are presented with a randomly generated 4-letter geomatic word from a user-provided file. The objective is to guess the entire word or individual letters until the correct word is guessed or the player decides to quit. Players can exit the game at any point. Each letter in the English language is assigned a specific frequency, with "e" being the most common and "z" the least.

Upon quitting the game, the following information will be displayed:
- Score from each round
- Original word
- Game status (correct guess or not)
- Number of guesses required
- Final score for that game

## Rules

1. The letters that are still blank at the time of a correct guess will be summed together to give a total.
2. The number of letters that the player turns over also affects the score. The sum is divided by the number of times the player requests a letter.
3. An incorrect guess costs 10% of the score for the current word.
4. When the player gives up, the points lost are the sum of the uncovered letters.

## Documentation

Python-style documentation is provided for the system, and `pydoc` can be used to generate a full web-based API for the application.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/geomatic-word-guessing-game.git

