#! python3

def main():
    print("Welcome to HANGMAN!\nThere is a generated Secret word and you have 10 guesses to guess the Secret word!\n")
    secret_word = input("Please enter in a secret word: ")

    already_guessed = []
    board_display = list(secret_word)
    board_secret = ["_"] * len(secret_word)

    counter = 0
    while counter <= 10:
        if counter == 10:
            print(f"You ran out of guesses! The secret word was {secret_word}!")
            break
        user_letter = input("Please enter in a letter: ")
        if user_letter in board_display:
            del board_secret[board_display.index(user_letter)]
            board_secret.insert(board_display.index(user_letter), user_letter)
            already_guessed.append(user_letter)
            counter += 1
        else:
            already_guessed.append(user_letter)
            print("Wrong! Guess another letter!\n")
            counter += 1
        if "_" not in board_secret:
            print(f"You won! The secret word was {secret_word}!\n")
            break
        print(f"Already guessed letters are {already_guessed}.")
        print(board_secret)

main()