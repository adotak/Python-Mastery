# Ahmad, Roll No: __________, 2026-11-11
"""For and while loop examples."""
import random


def times_table(number: int) -> list[str]:
    return [f"{number} x {i} = {number * i}" for i in range(1, 11)]


def check_pin(pin_inputs: list[str], correct_pin: str = "4321") -> str:
    for attempt, entered in enumerate(pin_inputs[:3], 1):
        if entered == correct_pin:
            return "Welcome"
        if attempt < 3:
            print(f"Wrong PIN. Tries left: {3 - attempt}")
    return "Card blocked"


def guessing_game() -> None:
    secret = random.randint(1, 50)
    guesses = 0
    while True:
        guess = int(input("Guess (1-50): "))
        guesses += 1
        if guess == secret:
            print(f"Got it in {guesses} guesses!")
            return
        print("Too high" if guess > secret else "Too low")


def main() -> None:
    number = int(input("Number: "))
    print("\n".join(times_table(number)))
    entered: list[str] = []
    for _ in range(3):
        entered.append(input("PIN: "))
        if entered[-1] == "4321":
            break
    print(check_pin(entered))


if __name__ == "__main__":
    main()
