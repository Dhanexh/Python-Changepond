def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman_game():
    word = "EVAPORATE"
    guessed_letters = set()
    incorrect_guesses = set()
    
    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))
    
    while set(word) != guessed_letters:
        guess = input("Guess your letter: ").upper()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters or guess in incorrect_guesses:
            print("You've already guessed that letter.")
            continue
        
        if guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! {display_word(word, guessed_letters)}")
        else:
            incorrect_guesses.add(guess)
            print(f"Incorrect! {display_word(word, guessed_letters)}")
    
    print("Congratulations! You've guessed the word correctly.")

if __name__ == "__main__":
    hangman_game()
