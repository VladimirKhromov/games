# Игра угадай число
from random import randint

GAME_NAME = "Угадай число"

LEVELS = {"Очень Легко": 4,
          "Легко": 32,
          "Нормально": 128,
          "Сложно": 512,
          "Очень Сложно": 1024,
          "Немыслимо": 16384,
          }


def get_secret_number(n: int) -> int:
    return randint(1, n)


def check_numbers(guess: int, secret_number: int) -> bool:
    if guess == secret_number:
        print("Ура, вы победили!")
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
        for i, key in enumerate(LEVELS.keys()):
            print(f"{i + 1}. {key}")
        user_response = input("Выберете уровень сложности (или 'выход' для завершения): ")
        if user_response == 'выход':
            print("До свидания!")
            break

        if int(user_response) not in range(1, len(LEVELS) + 1):
            print("Некорректный выбор. Попробуйте снова.")
            continue
        for i, key in enumerate(LEVELS.keys()):
            if int(user_response) - 1 == i:
                game(LEVELS[key])


if __name__ == "__main__":
    game_start()
