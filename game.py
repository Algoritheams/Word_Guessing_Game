import random
 
def choose_geospatial_word():
    geospatial_words = [
        "cartography",
        "coordinate reference systems",
        "geographic data",
        "geographic information systems",
        "geographic information technology",
        "geographic database",
        "geodesy",
        "geodetic coordinate systems",
        "geodetic measurements",
        "geodetic networks",
        "geoinformatics",
        "geospatial technologies",
        "gis analysis",
        "gnss",
        "map projection",
        "remote sensing",
        "remote sensing data",
        "spatial analysis",
        "spatial planning"
    ]
 
    return random.choice(geospatial_words)
 
def display_word(secret_word, guessed_letters):
    return "".join(letter if letter in guessed_letters else "_" for letter in secret_word)
 
def geospatial_word_guess_game():
    secret_word = choose_geospatial_word()
    guessed_letters = set()
    remaining_guesses = 3  
 
    print("Welcome to the Geospatial Word Guessing Game!")
    print("The geospatial term you need to guess:", display_word(secret_word, guessed_letters))
 
    while True:
        guess = input("Guess a letter: ").lower()
 
        if guess in guessed_letters:
            print("You already guessed this letter. Try another one.")
            continue
 
        guessed_letters.add(guess)
 
        if guess not in secret_word:
            remaining_guesses -= 1
            print(f"Wrong guess! Remaining guesses: {remaining_guesses}")
        else:
            print("Correct guess!")
 
        print("The geospatial term you need to guess:", display_word(secret_word, guessed_letters))
 
        if set(secret_word) <= guessed_letters:
            print("Congratulations! You found the geospatial term.")
            break
 
        if remaining_guesses == 0:
            print(f"Unfortunately, you've run out of guesses. The correct geospatial term was: {secret_word}")
            
            # Kullanıcının bütün hakları bittikten sonra kelimeyi yazma hakkı
            user_guess = input("Try to guess the geospatial term: ").lower()
            if user_guess == secret_word:
                print("Correct! You guessed the geospatial term.")
            else:
                print(f"Sorry, the correct geospatial term was: {secret_word}")
                
            break
 
if __name__ == "__main__":
    geospatial_word_guess_game()
