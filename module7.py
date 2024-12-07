def calculate_player_stats(goals, assists):
    """Рассчитывает основные статистики игрока."""
    return {'goals': goals, 'assists': assists, 'points': goals + assists}

def format_player_name(first_name, last_name):
    """Форматирует имя игрока."""
    return f"{first_name} {last_name}"

def get_team_ranking(team_name):
    """Получает рейтинг команды."""
    rankings = {'ЦСКА': 1, 'Локомотив': 2, 'Факел': 3}
    return rankings.get(team_name, None)
