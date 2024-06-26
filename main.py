import random
import os
from hangman_art import logo, stages
from hangman_words import word_list

# Initialize game
lives = 6
print(logo)

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = ["-" for _ in range(word_length)]
guessed_letters = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while not end_of_game:
    # Show current status
    print(f"{' '.join(display)}")
    print(stages[lives])
    
    # Check if game should end
    if "-" not in display:
        end_of_game = True
        print(f"You win!\nThe correct word is: {chosen_word}")
        break
    elif lives == 0:
        end_of_game = True
        print(f"You lose!\nThe correct word was: {chosen_word}")
        break
    
    # Ask for a guess
    guess = input("Guess a letter: ").lower()
    clear()
    
    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
        continue
    
    guessed_letters.append(guess)
    
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    else:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = letter

# End of game
print(stages[lives])  # Show the final state
