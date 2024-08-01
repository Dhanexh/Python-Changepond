import random

def generate_number():
    return str(random.randint(1000, 9999))

def get_cows_and_bulls(secret, guess):
    cows = sum(a == b for a, b in zip(secret, guess))
    bulls = sum(1 for g in guess if g in secret) - cows
    return cows, bulls

def cows_and_bulls_game():
    print("Welcome to the Cows and Bulls Game!")
    secret_number = generate_number()
    guess_count = 0
    
    while True:
        guess = input("Enter a 4-digit number: ")
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter a 4-digit number.")
            continue
        
        guess_count += 1
        cows, bulls = get_cows_and_bulls(secret_number, guess)
        
        if cows == 4:
            print(f"Congratulations! You've guessed the number {secret_number} in {guess_count} attempts.")
            break
        
        print(f"{cows} cows, {bulls} bulls")

if __name__ == "__main__":
    cows_and_bulls_game()
