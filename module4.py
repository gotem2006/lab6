from module5 import register_player

def schedule_match(team1, team2, date):
    """Планирует матч между двумя командами."""
    print(f"Матч между {team1} и {team2} запланирован на {date}")
    return True

def cancel_match(match_id):
    """Отменяет запланированный матч."""
    print(f"Матч {match_id} отменен")
    return True

def register_new_player(first_name, last_name, position):
    """Регистрирует и назначает игрока в команду."""
    player_id = register_player(first_name, last_name, position)
    return player_id
