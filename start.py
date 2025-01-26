from search_score import get_highest_score, update_player_score
import json

PLAYERS_FILE = "players.json"


def save_players(players):
    with open(PLAYERS_FILE, "w", encoding="utf-8") as file:
        json.dump(players, file, ensure_ascii=False, indent=4)


# O'yin oynash funksiyasi
def play_game(questions, players, player_name):
    score = 0
    help_used = False  # Yordam bir marta ishlatilishi uchun bayroq

    for question in questions:
        print(f"\nSavol: {question['question']}")

        for i, answer in enumerate(question['answers'], start=1):
            print(f"{i}) {answer['key']}")
        print("0 - Yordam (faqat bir marta foydalanish mumkin)")

        valid_choice = False  # To'g'ri tanlovni tekshirish bayrog'i
        while not valid_choice:  # Agar foydalanuvchi noto'g'ri javob kiritsa, savolni qaytadan ko'rsatish
            try:
                choice = int(input("Javobni tanlang (raqam): ")) - 1

                if choice == -1 and not help_used:
                    help_used = True
                    print("\nYordam ishlatildi! Noto‘g‘ri javoblardan ikkitasini olib tashlaymiz:")
                    incorrect_answers = [ans for ans in question['answers'] if not ans['isTrue']]
                    incorrect_answers = incorrect_answers[:2]  # Faqat ikkita noto‘g‘rini olish
                    filtered_answers = [ans for ans in question['answers'] if ans['isTrue']] + incorrect_answers

                    for i, answer in enumerate(filtered_answers, start=1):
                        print(f"{i}) {answer['key']}")
                    continue  # Savolni qayta ko‘rsatish uchun davom etamiz

                if 0 <= choice < len(question['answers']):
                    valid_choice = True  # To'g'ri tanlovni kiritganida tsiklni tugatamiz

                    # To'g'ri javobni tekshirish
                    if question['answers'][choice]['isTrue']:
                        print("To'g'ri javob!\n")
                        score += 1
                    else:
                        print("Noto'g'ri javob! O'yin tugadi.\n")
                        break  # Xato bo'lsa o'yinni tugatamiz
                else:
                    print("Iltimos, faqat 0 dan 4 gacha bo'lgan raqam kiriting.")
            except ValueError:
                print("Iltimos, faqat raqam kiriting!\n")

    else:
        print(f"O'yin tugadi, {player_name}, sizning ochkoyingiz: {score}\n")
        update_player_score(players, player_name, score)  # O'yinchining ballini yangilash
        print(f"Eng yuqori natija: {get_highest_score(players)}")


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
