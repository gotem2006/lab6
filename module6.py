from module7 import calculate_player_stats

def update_player_record(player_id, goals, assists):
    """Обновляет запись игрока со статистикой."""
    stats = calculate_player_stats(goals, assists)
    print(f"Игрок {player_id} статистика обновлена: {stats}")
    return stats

def calculate_team_points(wins, losses, draws):
    """Рассчитывает количество очков команды."""
    return wins * 3 + draws

def format_team_name(city, mascot):
    """Форматирует название команды."""
    return f"{city} {mascot}"
