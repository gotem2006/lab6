from module6 import update_player_record

def register_player(first_name, last_name, position):
    """Регистрирует нового игрока."""
    player_id = f"{first_name[0]}{last_name}{position[0]}".lower()
    print(f"Игрок {player_id} зарегистрирован.")
    return player_id

def assign_player_to_team(player_id, team_name):
    """Назначает игрока в команду."""
    print(f"Игрок {player_id} назначен в команду {team_name}")
    return True

def record_player_stats(player_id, goals, assists):
    """Записывает статистику игрока."""
    return update_player_record(player_id, goals, assists)
