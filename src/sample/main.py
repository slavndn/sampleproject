from game_logic import generate_random_number, check_guess
from user_interface import welcome_message, get_user_guess, show_result, game_over
from difficulty_levels import get_difficulty_level, get_number_range


def play_game():

    """Запускает игру угадывания числа.

    Эта функция управляет игровым процессом. Она запрашивает у пользователя уровень
    сложности, генерирует случайное число в заданном диапазоне, а затем просит
    пользователя угадывать это число. Игра продолжается до тех пор, пока пользователь
    не угадает число, после чего отображается количество попыток.

    The game flow is as follows:
    1. Запрос уровня сложности у пользователя.
    2. Генерация случайного числа в соответствии с выбранным уровнем сложности.
    3. Отображение приветственного сообщения.
    4. Запрос предположений от пользователя и проверка каждого предположения.
    5. Отображение результата после каждого предположения.
    6. Завершение игры после правильного угадывания.

    Returns:
        None
    """

    difficulty_level = get_difficulty_level()
    min_value, max_value = get_number_range(difficulty_level)
    secret_number = generate_random_number(min_value, max_value)

    welcome_message()

    attempts = 0
    while True:
        guess = get_user_guess()
        attempts += 1
        result = check_guess(guess, secret_number)
        show_result(result)
        if result == "Поздравляю, вы угадали!":
            print(f"Вы угадали за {attempts} попыток!")
            break

    game_over()


if __name__ == "__main__":
    play_game()
