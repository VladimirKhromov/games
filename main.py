#  Угадай число
import game_1
#  Угадай число
import game_2
#  Угадай число
import game_3

GAME_LIST = [game_1, game_2, game_3]

GAMES = {f'{game.GAME_NAME}': game for game in GAME_LIST}


def show_game() -> None:
    for i, key in enumerate(GAMES.keys()):
        print(f"{i + 1}. {key}")


def run_game(game_number):
    for i, key in enumerate(GAMES.keys()):
        if game_number - 1 == i:
            GAMES[key].game_start()


def dec(s: str = "#", n: int = 60):
    print(s[0] * n)


def main():
    while True:
        dec()
        show_game()
        number_game = input("Введите число для выбора игры, или \"выход\" для завершения: ")
        if number_game.lower() == "выход":
            print("До встречи!")
            break
        elif int(number_game) not in range(1, len(GAMES) + 1):
            print("Такой игры нет, попробуй еще!")
            continue
        dec()
        run_game(int(number_game))


if __name__ == "__main__":
    main()
