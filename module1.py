from module2 import league_signup

def welcome_message():
    """Выводит приветственное сообщение."""
    return "Добро пожаловать в систему управления спортивной лигой!"

def display_league_dashboard(league_name):
    """Отображает панель управления лиги."""
    return f"Панель управления для лиги {league_name}"

def start_application():
    """Запускает приложение."""
    print(welcome_message())
    league_signup("Премьер-лига")
