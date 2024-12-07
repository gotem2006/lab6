from module4 import schedule_match

def create_team(city, mascot):
    """Создает новую команду."""
    team_name = f"{city} {mascot}"
    print(f"Команда {team_name} создана.")
    return team_name

def get_team_schedule(team_name):
    """Получает расписание команды."""
    return [f"Матч против Локомотив на 2022-10-01", f"Матч против Факел на 2022-10-15"]

def schedule_team_match(team1, team2, date):
    """Планирует матч для команды."""
    return schedule_match(team1, team2, date)
