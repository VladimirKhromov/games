# Игра угадай число
from random import randint

LEVELS = {"Очень Легко": 4,
         "Легко": 32,
         "Нормально": 128,
         "Сложно": 512,
         "Очень Сложно": 1024,
          }


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


def game_start() -> None:
    while True:
        print("Выберете уровень сложности")
        for i, key in enumerate(LEVELS.keys()):
            print(f"{i + 1}. {key}")
        level = int(input("Введите цифру: "))
        if level < 1 or level > len(LEVELS):
            print("Выбрали неверную цифру, введите еще раз")
            continue
        for i, key in enumerate(LEVELS.keys()):
            if level - 1 == i:
                game(LEVELS[key])

        a = input("Сыграем в \"угадай число\' еще раз?! (да/нет): ")
        if a.lower() == "да":
            continue
        else:
            break


if __name__ == "__main__":
    game_start()
