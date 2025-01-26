import json

QUESTIONS_FILE = "question.json"
PLAYERS_FILE = "players.json"

# Savollarni fayldan o'qish
def load_questions():
    try:
        with open(QUESTIONS_FILE, "r", encoding="utf-8") as file:
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
        return []

# O'yinchilarni faylga saqlash
def save_players(players):
    with open(PLAYERS_FILE, "w", encoding="utf-8") as file:
        json.dump(players, file, ensure_ascii=False, indent=4)

# O'yinchi ma'lumotlarini yangilash
def update_player_score(players, player_name, score):
    player = next((p for p in players if p["name"] == player_name), None)
    if player:
        player["played"] += 1
        player["score"] = max(player["score"], score)
    else:
        players.append({"name": player_name, "played": 1, "score": score})
    save_players(players)

# Foydalanuvchidan valid tanlov olish
def get_valid_choice(prompt, max_choice):
    while True:
        try:
            choice = int(input(prompt))
            if 0 <= choice <= max_choice:
                return choice
            else:
                print(f"Iltimos, 0 dan {max_choice} gacha raqam kiriting!")
        except ValueError:
            print("Faqat raqam kiriting!")
