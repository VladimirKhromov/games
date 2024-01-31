GAME_NAME = "Виселица"
LEVELS = {"Легко": 0,
          "Нормально": 1,
          "Сложно": 2,
          }


def game():
    pass


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
