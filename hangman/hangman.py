import sys

def hangman(lines):
    word = lines[0]
    alph = lines[1]

    lives = 10
    game = {}
    for letter in word:
        game[letter] = False

    for letter in alph:
        if game.get(letter) is not None:
            game[letter] = True

            if all(game.values()):
                return "WIN"
        else:
            lives -= 1

            if lives == 0:
                return "LOSE"


def main():
    lines = [line.strip() for line in sys.stdin]
    print(hangman(lines))
main()
