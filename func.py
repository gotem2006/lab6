
import random
import math
import locale
from decimal import Decimal, getcontext
from dataclasses import dataclass

# Шаг 4: Функции, использующие модуль random

def random_score():
    """Шаг 4: Генерирует случайный счет для матча."""
    return random.randint(0, 5)

def select_random_team(teams):
    """Шаг 4: Выбирает случайную команду из списка."""
    return random.choice(teams)

# Шаг 5: Функции, использующие модуль math

def calculate_distance(x1, y1, x2, y2):
    """Шаг 5: Вычисляет расстояние между двумя точками (например, стадионами)."""
    return math.hypot(x2 - x1, y2 - y1)

def calculate_player_bmi(weight, height):
    """Шаг 5: Вычисляет индекс массы тела игрока."""
    return weight / math.pow(height, 2)

def calculate_average_speed(distance, time):
    """Шаг 5: Вычисляет среднюю скорость."""
    return distance / time

# Шаг 6: Функции, использующие модуль locale

def set_locale(locale_name):
    """Шаг 6: Устанавливает локаль для форматирования."""
    locale.setlocale(locale.LC_ALL, locale_name)

def format_date_locale(date_obj):
    """Шаг 6: Форматирует дату согласно локали."""
    return date_obj.strftime(locale.nl_langinfo(locale.D_T_FMT))

def get_locale_currency_symbol():
    """Шаг 6: Получает символ валюты согласно локали."""
    conv = locale.localeconv()
    return conv['currency_symbol']

# Шаг 7: Функции, использующие модуль decimal

def precise_percentage(part, whole):
    """Шаг 7: Вычисляет процент с высокой точностью."""
    getcontext().prec = 6
    return (Decimal(part) / Decimal(whole)) * Decimal(100)

def calculate_salary_after_tax(salary, tax_rate):
    """Шаг 7: Рассчитывает зарплату после вычета налога с использованием Decimal."""
    getcontext().prec = 10
    salary_dec = Decimal(salary)
    tax_rate_dec = Decimal(tax_rate)
    return salary_dec * (Decimal(1) - tax_rate_dec)

# Шаг 8: Data-классы

@dataclass
class Player:
    """Шаг 8: Data-класс для игрока."""
    id: int
    name: str
    position: str

@dataclass
class Team:
    """Шаг 8: Data-класс для команды."""
    id: int
    name: str
    players: list  # Список игроков

@dataclass
class Match:
    """Шаг 8: Data-класс для матча."""
    id: int
    home_team: 'Team'
    away_team: 'Team'
    score: tuple  # (голы домашней команды, голы гостевой команды)

# Шаг 9: Функции, использующие data-классы

def display_player_info(player):
    """Шаг 9.1: Принимает объект data-класса в качестве параметра."""
    print(f"Игрок ID: {player.id}, Имя: {player.name}, Позиция: {player.position}")

def get_team_players(team):
    """Шаг 9.2: Работает со списком объектов data-класса."""
    return [player.name for player in team.players]

def add_player_to_team(team_dict, team_id, player):
    """Шаг 9.3: Работает со словарем, где значение - объект data-класса."""
    team = team_dict.get(team_id)
    if team:
        team.players.append(player)

def update_player_position(player, new_position):
    """Шаг 9.4: Модифицирует значения объекта data-класса."""
    player.position = new_position

def create_player(id, name, position):
    """Шаг 9.5: Создает объект data-класса на основе переданных параметров."""
    return Player(id=id, name=name, position=position)
