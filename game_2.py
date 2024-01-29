# игра камень ножницы бумага
from random import choice

GAME_NAME = 'Камень, ножницы, бумага.'
OPTIONS = ['камень', 'ножницы', 'бумага']


def is_win(user_choice: str, computer_choice: str) -> None:
    if user_choice == computer_choice:
        print("--> Ничья!")
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
            (user_choice == 'ножницы' and computer_choice == 'бумага') or \
            (user_choice == 'бумага' and computer_choice == 'камень'):
        print("--> Вы победили!")
    else:
        print("--> Компьютер победил!")


def game():
    while True:
        # Пользовательский ввод
        user_choice = input("Выберите: камень, ножницы или бумага (или 'выход' для завершения): ").lower()

        if user_choice == 'выход':
            print("До свидания!")
            break
        elif user_choice not in OPTIONS:
            print("Некорректный выбор. Попробуйте снова.")
            continue

        # Выбор компьютера
        computer_choice = choice(OPTIONS)
        print(f"Компьютер выбрал: {computer_choice}")

        # Определение победителя
        is_win(user_choice, computer_choice)


def game_start() -> None:
    game()


if __name__ == "__main__":
    game_start()
