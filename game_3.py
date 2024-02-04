from game_3_lib import get_word

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









def game(level):
    secret_word = get_word(level)
    person_alpha = ["_" for _ in range(len(secret_word))]

    while True:
        print(
            f"Загаданное слово {' '.join(person_alpha)}, {len(secret_word)} {'буквы' if len(secret_word) < 5 else 'букв'}")
        guess = input("Введите букву:")

        if guess in secret_word:
            print("Есть такая буква!")
            person_alpha = update_personal_world(person_alpha, secret_word, guess)
        else:
            print("Такой буквы нет!")

        # Проверка что все буквы угаданы
        # Проверка что буква одна вводится пользователем
        # Добавить попытки


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
