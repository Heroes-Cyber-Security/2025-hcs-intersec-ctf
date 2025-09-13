#!/usr/bin/env python3

import random
import sys

WORD_LIST = []

GREEN = "\033[42m\033[30m"
YELLOW = "\033[43m\033[30m"
GRAY = "\033[47m\033[30m"
RESET = "\033[0m"

def fetch_word_list():
    word_file_path = "words.txt"
    with open(word_file_path, 'r') as f:
        words = [line.strip() for line in f if line.strip()]
        WORD_LIST.extend(words)

def pick_word():
    return random.choice(WORD_LIST)

def check_guess(secret, guess):
    result = []
    secret_chars = list(secret)
    guess_chars = list(guess)

    for i in range(len(secret)):
        if guess_chars[i] == secret_chars[i]:
            result.append(GREEN + guess_chars[i].upper() + RESET)
            secret_chars[i] = None
            guess_chars[i] = None
        else:
            result.append(None)

    for i in range(len(secret)):
        if guess_chars[i] is not None:
            if guess_chars[i] in secret_chars:
                result[i] = YELLOW + guess_chars[i].upper() + RESET
                secret_chars[secret_chars.index(guess_chars[i])] = None
            else:
                result[i] = GRAY + guess_chars[i].upper() + RESET
    
    return "".join(result)

def show_flag():
    flag_path = "/app/flag.txt"
    try:
        with open(flag_path, 'r') as f:
            flag = f.read().strip()
        print(f"🎊 FLAG: {flag}")
    except:
        print("Error: Could not read flag.")

def wordle():
    sys.stdout.flush()
    secret = pick_word()
    tries = 6

    print("\n=== WORDLE CLI CHALLENGE ===")
    print(f"Guess the {len(secret)}-letter word! You have {tries} tries.\n")
    sys.stdout.flush()

    for attempt in range(1, tries + 1):
        try:
            guess = input(f"Try {attempt}/{tries}: ").lower().strip()
        except EOFError:
            print("\nGoodbye!")
            return

        if len(guess) != len(secret):
            print(f"❌ Word must be exactly {len(secret)} letters.\n")
            sys.stdout.flush()
            continue

        result = check_guess(secret, guess)
        print(result + "\n")
        sys.stdout.flush()

        if guess == secret:
            print("🎉 You guessed it! The word was:", secret.upper())
            show_flag()
            return

    print("😢 Out of tries! The word was:", secret.upper())
    sys.stdout.flush()

if __name__ == "__main__":
    fetch_word_list()
    wordle()