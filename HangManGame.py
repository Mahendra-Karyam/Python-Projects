import random
def choose_word():
    words = ['hangman', 'python', 'programming', 'computer', 'game', 'challenge']
    return random.choice(words).lower()


def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display


def draw_hangman(turns):
    stages = [
        '''
           +---+
           |   |
               |
               |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        '''
    ]
    return stages[turns]


def hangman():
    print("Welcome to Hangman!")
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print(draw_hangman(attempts))
        print("\nWord:", display_word(secret_word, guessed_letters))
        if '_' not in display_word(secret_word, guessed_letters):
            print("\nCongratulations! You've guessed the word:", secret_word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print("Incorrect guess. Attempts left:", attempts)
            if attempts == 0:
                print(draw_hangman(attempts))
                print("Sorry, you're out of attempts! The word was:", secret_word)
                break
        else:
            print("Good guess!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thanks for playing Hangman!")


hangman()
