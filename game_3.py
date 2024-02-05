from game_3_lib import get_word, rus_letters

GAME_NAME = "Виселица"
LEVELS = {"Легко": 0,
          "Нормально": 1,
          "Сложно": 2,
          }


def update_personal_world(l: list, secret: str, quess: str) -> list:
    # len(quess) == 1
    for index in range(len(secret)):
        if secret[index] == quess:
            l[index] = secret[index]
    return l


def check_letter(letter: str):
    if len(letter) == 1 and letter in rus_letters:
        return True
    return False

def get_attempt(level):
    if level in range(0,len(LEVELS)):
        return 10 - level*2
    return 5

def game(level):
    # Получаем слово
    secret_word = get_word(level)
    # Создаем табло для букв
    person_alpha = ["_" for _ in range(len(secret_word))]
    # Даем количество попыток
    attempt = get_attempt(level)

    while person_alpha != list(secret_word):
        print(
            f"Загаданное слово {' '.join(person_alpha)}, {len(secret_word)} {'буквы' if len(secret_word) < 5 else 'букв'}")
        print(f' У вас осталось {attempt} попыток')
        guess = input("Введите букву:").lower()

        if not check_letter(guess):
            print('Неверно, попробуйте еще раз')
        elif guess in secret_word:
            print("Есть такая буква!")
            person_alpha = update_personal_world(person_alpha, secret_word, guess)
        else:
            attempt -= 1
            if attempt == 0:
                print("К сожалению вы проиграли!")
                print(f'Правильное слобо было --{secret_word}--')
                break
            print(f"Такой буквы нет! Минус попытка")

        # Добавить попытки
    else:
        print(f'Поздравляем! Вы угадали --{secret_word}-- и победили!')


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
