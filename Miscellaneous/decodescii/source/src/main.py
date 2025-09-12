import random
import base64
import time
import os

CHALLENGE_TEMPLATE = r"""`TEMUKAN INPUT TERKECIL YANG MEMENUHI PROGRAM INI`
                                                               _^_        ____
                            `POV: YOU TRY TO DO`              /-=+\\   //#=++=\
                            `ASCII ART IN 24H,`             .-#TARGET_PLACEHOLDERv
                            `PLS DON'T GRILL ME :<`         |#:===/+++__+__++----<<\
                                                            |/-_+-<+\=_/==:       \|
    .-#?v_     __                                           //=+/                   
      / \-\   /\-\                 ________                 |     `HINT: YOU MAY NOT WANT`
       \ \\\  \ \\\      ________#/---------\               |     `TO BRUTE THIS, WHAT'S AN`
        \ \\-*-----\-/---*--------\>--v_____/               |     `EFFICIENT WAY TO GO THRU`
         \ \->#C1-[OP1]| | \*#FORC2--+^v-|\______              |     `A MONOTONIC F(x) DOMAIN?`
          \ \-\  \ \-/  \ \\      \__{OP2}-----v\             |
           \/_/   \/_/   \ \-#FORC3_>+_____v_|_\            |   /-$'OMG BERHASIL <3'
                          \_\_____/    /v-{OP3}<_/            | .-~-$'Masih kurang pak :<'
                                      |_>______------------{G}--^
"""


def generate_challenge():
    # --- Configuration ---
    TARGET_MIN, TARGET_MAX = 10**18, 10**19
    X_SEARCH_MIN, X_SEARCH_MAX = 1, 10**14
    C1_LEN, C2_LEN, C3_LEN = 2, 4, 5
    T_LEN = 19

    # --- Step 1: Generate a random monotonic function ---
    possible_ops = ["+", "*", "**"]
    c1, c2, c3 = (
        random.randint(10, 99),
        random.randint(1000, 9999),
        random.randint(10000, 99999),
    )
    constants = [c1, c2, c3]

    ops = [random.choice(possible_ops) for _ in range(3)]
    if all(op == "+" for op in ops):
        ops[random.randint(0, 2)] = "*"

    ops_list = []
    for i in range(3):
        op_symbol = ops[i]
        value = 2 if op_symbol == "**" else constants[i]
        ops_list.append((op_symbol, value))

    def func(x):
        res = x
        for op, val in ops_list:
            if op == "+":
                res += val
            elif op == "*":
                res *= val
            elif op == "**":
                res **= val
        return res

    # --- Step 2: Find a suitable x_solution ---
    low, high, x_solution = X_SEARCH_MIN, X_SEARCH_MAX, -1
    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            low = 1
            continue
        try:
            result = func(mid)
        except OverflowError:
            result = float("inf")
        if result < TARGET_MIN:
            low = mid + 1
        elif result > TARGET_MAX:
            high = mid - 1
        else:
            x_solution = mid
            high = mid - 1

    if x_solution == -1:
        return generate_challenge()

    # --- Step 3: Prepare the final output and template replacements ---
    target = func(x_solution)

    val1, val2, val3 = ops_list[0][1], ops_list[1][1], ops_list[2][1]
    op1, op2, op3 = ops_list[0][0], ops_list[1][0], ops_list[2][0]

    # Map '**' to '^' for single-character display
    display_op1 = "^" if op1 == "**" else op1
    display_op2 = "^" if op2 == "**" else op2
    display_op3 = "^" if op3 == "**" else op3

    # Pad so the ascii works out
    padded_c1 = str(val1).ljust(C1_LEN, "-")
    padded_c2 = str(val2).ljust(C2_LEN, "-")
    padded_c3 = str(val3).ljust(C3_LEN, "-")
    padded_target = str(target).ljust(T_LEN, "-")

    # Perform all the replacements
    challenge_string = CHALLENGE_TEMPLATE.replace("TARGET_PLACEHOLDER", padded_target)
    challenge_string = challenge_string.replace("C1", padded_c1)
    challenge_string = challenge_string.replace("FORC2", padded_c2)
    challenge_string = challenge_string.replace("FORC3", padded_c3)
    challenge_string = challenge_string.replace("OP1", display_op1)
    challenge_string = challenge_string.replace("OP2", display_op2)
    challenge_string = challenge_string.replace("OP3", display_op3)

    challenge_data = {
        "solution": x_solution,
        "target": target,
        "ops": ops_list,
    }

    challenge_link = "https://ajanse.me/asciidots/?code=" + (
        base64.b64encode(challenge_string.encode())
        .decode()
        .replace("/", "_")
        .replace("+", "-")
    )

    return challenge_data, challenge_string, challenge_link


if __name__ == "__main__":
    challenge_data, challenge_string, challenge_link = generate_challenge()

    qs = [
        [
            "1. THE WEIRD STRING...",
            "We intercepted this IRC communication from one of their members during a C2 authentication, we believe it contains the key to their C2. Help us crack it.",
            "22 59 34 6e 6b 33 33 20 5a 33 72 30 20 46 75 6c 6c 20 35 37 30 70 20 20 35 33 76 33 6e 20 48 30 37 33 6c 20 37 68 72 33 33 20 20 4b 31 6c 30 20 37 68 72 33 33 20 59 34 6e 6b 33 33 20 20 30 6e 33 20 46 31 76 33 20 20 30 6e 33 20 37 68 72 33 33 20 30 6e 33 20 37 77 30 20 22",
            "1312",
            "Hmm, wrong key, Agent. Our forensics team believe this is some kind of encoding, however.",
        ],
        [
            "2. Asset?",
            "Continuing the investigation, the actors seems to have caught on and changed the cover of their messages.\n>  We believe this contains a malicious binary they're about to send. Help us locate it on the web, provide the link.",
            "3G4P47S44:8D7/DR44+3EEB6S44EECM9EM-DZED1Q5LQE0/DZEDT44S44+8DA44ZEDGEC3EF2LE1Q5-EDJ:4944SUEF1A TAI1AWL6A69L7BG%63M6U6AQIBXY9UTAX+9 TA8*6PTAA+84X6VX8CIA71A5X60C9DH8K+997BWYATTAYY9HX7HX7HX7Y0",
            "https://files.catbox.moe/fmg01x.webp",
            "Hmm, doesn't seem to be a valid URL, Agent. Though, this is quite an interesting looking encoding, kinda reminds me of that... thing, back during COVID...",
        ],
        [
            "3. Final Attack",
            "Investigating the binary, it seems to be a ransomware polyglot. Our forensics team found this encryption software which validates the key with the following program, help us crack it!",
            base64.b64encode(challenge_link.encode()),
            challenge_data["solution"],
            f"Hmm, that doesn't seem to be the right key, Agent.",
        ],
    ]

    assg = hex(random.randint(0, int(time.time())))
    print("Generating a new challenge...")
    print("𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃")
    print(f"Welcome, Agent {assg},")
    print("𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃")

    print(
        "> A new threat actor has recently been identified running amok in the depths of the dark web."
    )
    print("> You will be provided with the case facts below, help us solve this case.")
    print(
        "> A toolkit is provided at https://gchq.github.io/CyberChef/, we believe this will help you greatly.\n\n"
    )

    for q in qs:
        print()
        print(q[0])
        print("> ", q[1])
        print("-" * len(q[0]))
        print(q[2])
        print()
        if input("Answer: ") != str(q[3]):
            print(q[4])
            exit()
        print("That worked! Great job, Agent. Moving on.")

    print()
    print(f"CONGRATS AGENT {assg},")
    print(f"YOU HAVE HELPED US CRACK THIS CASE.")
    username = os.environ.get('USERNAME')
    with open(f"/home/{username}/flag.txt", "r") as f:
        flag = f.read()
    print(f"HERE'S YOUR PAYCHECK: {flag}")
