# Игра угадай число
from random import randint


def get_secret_number(n: int) -> int:
    return randint(1, n)


def check_numbers(guess: int, secret_number: int) -> bool:
    if guess == secret_number:
        print("Ура, вы выйграли!")
        return True
    elif guess > secret_number:
        print("Секретное число меньше, чем предположение")
        return False
    elif guess < secret_number:
        print("Секретное число больше, чем предположение")
        return False


def game(max_number: int = 128) -> None:
    secret_number = get_secret_number(max_number)
    print(f"Компьютер загадал число от 1 до {max_number}, попробуйте угадать!")
    while True:
        guess = int(input("Введите число: "))

        if check_numbers(guess, secret_number):
            break


if __name__ == "__main__":
    game()
