import json

PLAYERS_FILE = "players.json"


# O'yinchi ma'lumotlarini faylga saqlash
def save_players(players):
    with open(PLAYERS_FILE, "w", encoding="utf-8") as file:
        json.dump(players, file, ensure_ascii=False, indent=4)


# O'yinchi ma'lumotlarini yangilash
def update_player_score(players, player_name, score):
    # O'yinchini ro'yxatdan izlash
    player = next((p for p in players if p["name"] == player_name), None)

    if player:
        # Agar o'yinchi mavjud bo'lsa, uning o'ynaganlar soni va eng yaxshi ballini yangilash
        player["played"] += 1
        player["score"] = max(player["score"], score)
    else:
        # Yangi o'yinchi qo'shish
        players.append({"name": player_name, "played": 1, "score": score})

    # O'yinchilar ro'yxatini faylga saqlash
    save_players(players)


# Eng yuqori ballni topish
def get_highest_score(players):
    highest_score = 0
    highest_player = ""  # Eng yuqori ballni egallagan o'yinchining ismi

    for player in players:
        if player["score"] > highest_score:
            highest_score = player["score"]
            highest_player = player["name"]

    return highest_player, highest_score
