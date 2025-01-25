from start import play_game, show_ratings
import json

QUESTIONS_FILE = "question.json"
PLAYERS_FILE = "players.json"


def load_questions():
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def load_players():
    try:
        with open(PLAYERS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def main():
    questions = load_questions()
    players = load_players()

    while True:
        choice = input(int(input("""Kim millioner bo'lishni istaydi testiga xush kelibsiz!

    Buyuruqni tanlang:

    1 - Test
    2 - Reyting

    0 - Chiqish

    >>> """)))

        if choice == "1":
            player_name = input("Ismingizni kiriting: ")
            play_game(questions, players, player_name)
        elif choice == "2":
            show_ratings(players)
        elif choice == "0":
            print("Dasturdan chiqildi. Xayr!")
            break
        else:
            print("Noto'g'ri buyruq, qaytadan urinib ko'ring!\n")
