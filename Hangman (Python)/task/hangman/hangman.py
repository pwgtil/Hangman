import random
import string


def game():
    # base
    words = ("python", "java", "swift", "javascript")
    the_word = random.choice(words)
    letters_to_guess = set(the_word)
    bucket_of_letters_used = set()
    lives = 8

    # main program flow
    while lives > 0:
        print(f"\n{hide_letters(the_word, letters_to_guess)}")
        letter = input("Input a letter: ")
        if not verify_input(letter, bucket_of_letters_used):
            continue
        if letter in the_word:
            letters_to_guess.discard(letter)
            if len(letters_to_guess) == 0:
                break
        else:
            lives -= 1
            print("That letter doesn't appear in the word.")
        bucket_of_letters_used.add(letter)

    if len(letters_to_guess) == 0:
        print(f"You guessed the word {the_word}!\nYou survived!")
        return True
    else:
        print("\nYou lost!")
        return False


def hide_letters(word, letters_to_hide):
    result = word[:]
    for s in letters_to_hide:
        if s in word:
            result = result.replace(s, "-")
    return result


def verify_input(user_input, bucket_of_letters_used):
    result = False
    if len(user_input) != 1:
        print("Please, input a single letter.")
    elif user_input not in string.ascii_lowercase:
        print("Please, enter a lowercase letter from the English alphabet.")
    elif user_input in bucket_of_letters_used:
        print("You've already guessed this letter.")
    else:
        result = True
    return result


wins = 0
loses = 0
print("H A N G M A N")
while True:
    command = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if command == "play":
        if game():
            wins += 1
        else:
            loses += 1
    elif command == "results":
        print(f"You won: {wins} times\nYou lost: {loses} times")
    else:
        break
