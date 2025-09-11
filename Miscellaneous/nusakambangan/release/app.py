#!/usr/bin/env python3

import time


def banner():
    with open("./banner.txt", "r") as f:
        print(f.read())
    print(
        "looks like a jail, has the same restriction, but it's not about the real jail!\n"
    )


def validity_check(word: str) -> bool:
    if len(word) > 1337:
        return False

    if not word.isascii():
        return False

    if any(char.isdigit() for char in word):
        return False

    blacklists = [
        "\\",
        "'",
        '"',
        " ",
        "[",
        "]",
        "os",
        "input",
        "popen",
        "subprocess",
        "breakpoint",
        "import",
        "sys",
        "eval",
        "exec",
        "flag",
        "read",
        "pop",
        "builtins"
    ]

    if any(bl in word for bl in blacklists):
        return False

    return True


def run():
    word = input(">> enter last word before jail: ")

    print("\n[i] checking...")
    time.sleep(1)
    ok = validity_check(word)
    if not ok:
        print("[-] seems like your word is not legit, try again!")
        return

    print("[+] looks like your word is legit, connecting to the jail...")
    time.sleep(1)

    try:
        exec(word, {"__builtins__": {"print": print, "str": str, "int": int, "chr": chr}}, {})
    except:
        print("[-] the world is not excepted your word, you're the trouble, get out!!!")
        return


if __name__ == "__main__":
    banner()
    run()
