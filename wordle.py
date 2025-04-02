import argparse
import random
import sys

from collections import Counter

from rich.console import Console
import pyfiglet


GUESS_COUNT: int = 6


def correct(letter: str) -> str:
    return f"[bold white on green]{letter}[/bold white on green]"


def close(letter: str) -> str:
    return f"[bold white on orange1]{letter}[/bold white on orange1]"


def readwords(filename: str) -> set[str]:
    return {word.rstrip().lower() for word in open(filename) if len(word) == 6}


def words(is_guess: bool) -> set[str]:
    words = readwords("answers.txt")
    if is_guess:
        words |= readwords("guesses.txt")

    return words


def getword(words: set[str]) -> str:
    return random.sample(list(words), 1)[0]


def getmatch(guess: str, answer: str) -> str:
    match: list[str] = []
    guess = guess.upper()
    answer = answer.upper()
    counts = Counter(answer)

    for (l1, l2) in zip(guess, answer):
        if l1 == l2:
            counts[l1] -= 1

    for (l1, l2) in zip(guess, answer):
        if l1 == l2:
            match.append(correct(l1))
        elif l1 in answer and counts[l1] > 0:
            match.append(close(l1))
        else:
            match.append(l1)

    return "".join(match)


def clear(console: Console) -> None:
    console.clear()
    ascii_banner = pyfiglet.figlet_format("Terminal Wordle")
    print(ascii_banner)
    print("Guess the word:")


if __name__ == "__main__":
    ans = words(False)
    wds = words(True)

    parser = argparse.ArgumentParser(description="Terminal Wordle")

    parser.add_argument("--answer", type=str, default=getword(ans))
    parser.add_argument("--max-guesses", type=int, default=GUESS_COUNT)
    args = parser.parse_args()

    matches = []

    console = Console()
    clear(console)
    i = 0
    while i < args.max_guesses:
        print("> ", end="")
        try:
            guess = input()
        except (KeyboardInterrupt, EOFError):
            sys.exit(0)

        if len(guess) == 0:
            continue

        if len(guess) != 5 or guess not in wds:
            print("Guess must be a real 5 letter word")
            continue

        match = getmatch(guess, args.answer)
        matches.append(match)
        clear(console)
        for match in matches:
            console.print(match)

        if guess == args.answer:
            print("You win!")
            sys.exit(0)

        i += 1

    print("")
    print(f"Correct word: {args.answer}")
    print("Better luck next time!")
