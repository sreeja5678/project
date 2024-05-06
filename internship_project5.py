import random

class Hangman:
    def __init__(self, word, max_attempts=6):
        self.word = word.lower()
        self.max_attempts = max_attempts
        self.remaining_attempts = max_attempts
        self.guessed_letters = set()
        self.hidden_word = ['_' if char.isalpha() else char for char in self.word]

    def guess(self, letter):
        letter = letter.lower()
        if letter in self.guessed_letters:
            print("You've already guessed this letter.")
            return

        self.guessed_letters.add(letter)
        if letter in self.word:
            print("Correct guess!")
            for i, char in enumerate(self.word):
                if char == letter:
                    self.hidden_word[i] = letter
        else:
            self.remaining_attempts -= 1
            print("Incorrect guess.")
            self.draw_hangman()

    def draw_hangman(self):
        stages = [
            """
               ________
              |        |
              |        O
              |       \|/
              |        |
              |       / \\
             _|_
            |   |______
            |__________|
            """,
            """
               ________
              |        |
              |        O
              |       \|/
              |        |
              |       /
             _|_
            |   |______
            |__________|
            """,
            """
               ________
              |        |
              |        O
              |       \|/
              |        |
              |
             _|_
            |   |______
            |__________|
            """,
            """
               ________
              |        |
              |        O
              |       \|
              |        |
              |
             _|_
            |   |______
            |__________|
            """,
            """
               ________
              |        |
              |        O
              |        |
              |        |
              |
             _|_
            |   |______
            |__________|
            """,
            """
               ________
              |        |
              |        O
              |
              |
              |
             _|_
            |   |______
            |__________|
            """,
            """
               ________
              |        |
              |
              |
              |
              |
             _|_
            |   |______
            |__________|
            """
        ]
        print(stages[self.max_attempts - self.remaining_attempts])

    def display_hidden_word(self):
        print(' '.join(self.hidden_word))

    def is_game_over(self):
        if '_' not in self.hidden_word:
            print("Congratulations! You've won!")
            return True
        elif self.remaining_attempts == 0:
            print("Sorry, you've run out of attempts. The word was '{}'.".format(self.word))
            return True
        return False

def choose_word(category):
    animals = ['lion', 'elephant', 'giraffe', 'monkey', 'zebra']
    countries = ['india', 'canada', 'australia', 'france', 'brazil']
    movies = ['avatar', 'titanic', 'inception', 'jurassic park', 'interstellar']
    categories = {
        'animals': animals,
        'countries': countries,
        'movies': movies
    }
    if category in categories:
        return random.choice(categories[category])
    else:
        print("Invalid category. Choosing a word from 'animals' category.")
        return random.choice(animals)

def main():
    print("Welcome to Hangman!")
    category = input("Choose a category (animals, countries, movies): ")
    word = choose_word(category)
    game = Hangman(word)

    while not game.is_game_over():
        game.display_hidden_word()
        print("Remaining attempts:", game.remaining_attempts)
        guess = input("Guess a letter: ")
        game.guess(guess)

if __name__ == "__main__":
    main()
