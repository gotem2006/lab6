from func import (
    random_score,
    select_random_team,
    calculate_distance,
    calculate_player_bmi,
    calculate_average_speed,
    set_locale,
    format_date_locale,
    get_locale_currency_symbol,
    precise_percentage,
    calculate_salary_after_tax,
    display_player_info,
    get_team_players,
    add_player_to_team,
    update_player_position,
    create_player,
    Player,
    Team,
    Match
)
import datetime

def run_all_functions():
    """Шаг 10: Вызывает все функции из шагов 2-9."""

    # Шаг 2: Демонстрация импортов из шага 1
    from module1 import start_application
    start_application()

    # Шаг 4: Функции с использованием random
    score = (random_score(), random_score())
    print(f"Счет матча: {score[0]} - {score[1]}")

    teams_list = ['ЦСКА', 'Локомотив', 'Факел']
    selected_team = select_random_team(teams_list)
    print(f"Случайно выбранная команда: {selected_team}")

    # Шаг 5: Функции с использованием math
    distance = calculate_distance(0, 0, 3, 4)
    print(f"Расстояние между стадионами: {distance} км")

    bmi = calculate_player_bmi(75, 1.8)
    print(f"Индекс массы тела игрока: {bmi:.2f}")

    average_speed = calculate_average_speed(10, 0.5)
    print(f"Средняя скорость игрока: {average_speed} км/ч")

    # Шаг 6: Функции с использованием locale
    set_locale('ru_RU.UTF-8')
    date_now = datetime.datetime.now()
    formatted_date = format_date_locale(date_now)
    print(f"Текущая дата и время: {formatted_date}")

    currency_symbol = get_locale_currency_symbol()
    print(f"Символ валюты для текущей локали: {currency_symbol}")

    # Шаг 7: Функции с использованием decimal
    win_percentage = precise_percentage(15, 20)
    print(f"Процент побед команды: {win_percentage}%")

    salary_after_tax = calculate_salary_after_tax(50000, 0.13)
    print(f"Зарплата после налога: {salary_after_tax}")

    # Шаг 9: Функции, использующие data-классы

    # Шаг 9.5: Создание объекта data-класса
    player = create_player(10, 'Иван Петров', 'Нападающий')

    # Шаг 9.1: Передача объекта data-класса в функцию
    display_player_info(player)

    # Шаг 9.4: Модификация объекта data-класса
    update_player_position(player, 'Полузащитник')
    display_player_info(player)

    # Шаг 9.2: Работа со списком объектов data-класса
    team = Team(id=1, name='ЦСКА', players=[player])
    team_players = get_team_players(team)
    print(f"Игроки команды {team.name}: {team_players}")

    # Шаг 9.3: Работа со словарем объектов data-класса
    teams_dict = {team.id: team}
    new_player = create_player(11, 'Алексей Смирнов', 'Защитник')
    add_player_to_team(teams_dict, team.id, new_player)
    team_players = get_team_players(team)
    print(f"Обновленный список игроков команды {team.name}: {team_players}")

if __name__ == "__main__":
    run_all_functions()
