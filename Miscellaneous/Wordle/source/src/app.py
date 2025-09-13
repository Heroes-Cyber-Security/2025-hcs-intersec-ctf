#!/usr/bin/env python3

import requests
import random
import os
import sys

# Global list to hold words, populated at runtime.
WORD_LIST = []

# --- ANSI Colors ---
GREEN = "\033[42m\033[30m"   # Black text on green background
YELLOW = "\033[43m\033[30m"  # Black text on yellow background
GRAY = "\033[47m\033[30m"    # Black text on white/gray background
RESET = "\033[0m"

def fetch_word_list():
    """Fetches a list of 5-letter words from the API, assuming success."""
    api_url = "https://random-word-api.vercel.app/api?words=200&length=5"
    response = requests.get(api_url, timeout=5)
    response.raise_for_status() # Will error out on 4xx/5xx status codes
    WORD_LIST.extend(list(set(response.json())))

def pick_word():
    """Picks a random word from the globally loaded WORD_LIST."""
    return random.choice(WORD_LIST)

def check_guess(secret, guess):
    """Generates the colored output for the user's guess."""
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
    """Reads the flag directly from the expected file path."""
    flag_path = "/app/flag.txt"
    with open(flag_path, 'r') as f:
        flag = f.read().strip()
    print(f"🎊 FLAG: {flag}")

def wordle():
    """Main game loop."""
    secret = pick_word() # Will crash with IndexError if WORD_LIST is empty
    tries = 6

    print("\n=== WORDLE CLI CHALLENGE ===")
    print(f"Guess the {len(secret)}-letter word! You have {tries} tries.\n")

    for attempt in range(1, tries + 1):
        try:
            guess = input(f"Try {attempt}/{tries}: ").lower().strip()
        except EOFError:
            print("\nGoodbye!")
            return

        if len(guess) != len(secret):
            print(f"❌ Word must be exactly {len(secret)} letters.\n")
            continue

        result = check_guess(secret, guess)
        print(result + "\n")

        if guess == secret:
            print("🎉 You guessed it! The word was:", secret.upper())
            show_flag()
            return

    print("😢 Out of tries! The word was:", secret.upper())

if __name__ == "__main__":
    fetch_word_list()
    wordle()