from search_score import get_valid_choice, update_player_score
import json

PLAYERS_FILE = "players.json"


def save_players(players):
    with open(PLAYERS_FILE, "w", encoding="utf-8") as file:
        json.dump(players, file, ensure_ascii=False, indent=4)


# O'yinni boshlash funksiyasi
def play_game(questions, players, player_name):
    score = 0
    help_used = False

    for question in questions:
        print(f"\nSavol: {question['question']}")
        for i, answer in enumerate(question['answers'], start=1):
            print(f"{i}) {answer['key']}")
        print("0 - Yordam (faqat bir marta foydalanish mumkin)")

        while True:
            choice = get_valid_choice("Javobni tanlang (raqam): ", len(question['answers']))
            if choice == 0 and not help_used:
                help_used = True
                print("\nYordam ishlatildi! Noto‘g‘ri javoblardan ikkitasini olib tashlaymiz:")
                incorrect_answers = [ans for ans in question['answers'] if not ans['isTrue']]
                correct_answer = [ans for ans in question['answers'] if ans['isTrue']][0]
                filtered_answers = [correct_answer] + incorrect_answers[:2]
                for i, answer in enumerate(filtered_answers, start=1):
                    print(f"{i}) {answer['key']}")
                continue  # Savolni qayta chiqarish uchun davom ettiramiz
            elif 1 <= choice <= len(question['answers']):
                if question['answers'][choice - 1]['isTrue']:
                    print("To'g'ri javob!\n")
                    score += 1
                    break
                else:
                    print("Noto'g'ri javob! O'yin tugadi.\n")
                    update_player_score(players, player_name, score)
                    return
            else:
                print("Noto'g'ri tanlov. Qaytadan tanlang!")

    print(f"O'yin tugadi, {player_name}, sizning ochkoyingiz: {score}\n")
    update_player_score(players, player_name, score)



# Reytinglarni ko'rsatish funksiyasi
def show_ratings(players):
    if not players:
        print("Reytinglar mavjud emas!\n")
        return

    print("Reytinglar:")
    print("Ism           O'ynagan        Eng yaxshi natija")
    print("---------------------------------------------")
    for player in players:
        print(f"{player['name']:<14}{player['played']:<15}{player['score']:<15}")
    print()
