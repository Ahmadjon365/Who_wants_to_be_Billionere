from start import play_game, show_ratings
import json

QUESTIONS_FILE = "question.json"
PLAYERS_FILE = "players.json"


# Savollarni fayldan o'qish
def load_questions(file_name=QUESTIONS_FILE):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Savollar fayli topilmadi!")
        return []


# O'yinchilarni fayldan o'qish
def load_players():
    try:
        with open(PLAYERS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Fayl topilmasa bo'sh ro'yxat qaytariladi


# Asosiy dastur
def main():
    players = load_players()
    questions = load_questions()

    while True:
        print("\nKim millioner bo'lishni istaydi testiga xush kelibsiz!\n")
        print("Buyuruqni tanlang:")
        print("1 - Test")
        print("2 - Reyting")
        print("\n0 - Chiqish")

        choice = input("\nTanlovingizni kiriting: ")

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
