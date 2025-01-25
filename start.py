import json

PLAYERS_FILE = "players.json"


def save_players(players):
    with open(PLAYERS_FILE, "w", encoding="utf-8") as file:
        json.dump(players, file, ensure_ascii=False, indent=4)


def play_game(questions, players, player_name):
    score = 0
    for question in questions:
        print(f"\nSavol: {question['question']}")
        for i, answer in enumerate(question['answers'], start=1):
            print(f"{i}) {answer['key']}")

        try:
            choice = int(input("Javobni tanlang (raqam): ")) - 1
            if 0 <= choice < len(question['answers']) and question['answers'][choice]['isTrue']:
                print("To'g'ri javob!\n")
                score += 1
            else:
                print("Noto'g'ri javob!\n")
        except ValueError:
            print("Iltimos, faqat raqam kiriting!\n")

    print(f"O'yin tugadi, {player_name}, sizning ochkolaringiz: {score}\n")

    # Reytingni yangilash
    if player_name in players:
        players[player_name]['played'] += 1
        players[player_name]['best_score'] = max(players[player_name]['best_score'], score)
    else:
        players[player_name] = {'played': 1, 'best_score': score}

    save_players(players)


def show_ratings(players):
    if not players:
        print("Reytinglar mavjud emas!\n")
        return

    print("Reytinglar:")
    print("Ism           O'ynagan        Eng yaxshi natija")
    print("---------------------------------------------")
    for name, data in players.items():
        print(f"{name:<14}{data['played']:<15}{data['best_score']:<15}")
