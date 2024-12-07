from module3 import create_team

def league_signup(league_name):
    """Регистрирует новую лигу."""
    print(f"Лига {league_name} создана.")
    return league_name

def add_team_to_league(league_name, city, mascot):
    """Добавляет команду в лигу."""
    team_name = create_team(city, mascot)
    print(f"Команда {team_name} добавлена в лигу {league_name}")
    return team_name

def get_league_standings(league_name):
    """Получает текущие результаты лиги."""
    return {"ЦСКА": 1, "Локомотив": 2, "Факел": 3}
