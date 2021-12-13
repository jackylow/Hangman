import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages
chosen_word = random.choice(word_list)
lives = 6
print(logo)

# print(f'Pssst, the solution is {chosen_word}.')
display = []
for letter in chosen_word:
    display += "_"
print(display)
while "_" in display:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    n = - 1
    for letter in chosen_word:
        n += 1
        if guess == letter:
            display[n] = guess 
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print(stages[lives])
            print("You lose!") 
            break
    if "_" not in display:
        print("You win!") 
    print(f"{' '.join(display)}")
    print(stages[lives])
