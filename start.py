import random


def wind_game():
    directions = ["север", "юг", "восток", "запад"]
    correct = random.choice(directions)
    print("\n--- Мини-игра: Угадай направление ветра ---")
    print("Возможные направления: север, юг, восток, запад")

    while True:
        guess = input("Твой выбор: ").strip().lower()
        if guess in directions:
            break
        print("Нужно выбрать одно из направлений: север, юг, восток, запад.")

    if guess == correct:
        print("Верно! Ветер дует именно с этой стороны.")
        return True
    else:
        print(f"Не угадал. Ветер был с {correct}а.")
        return False


def left_path():
    print("\nты выходишь к старому мосту. Рядом сидит Старик-отшельник")
    print("Выберите действие:")
    print("1) поговорить")
    print("2) перейти мост")
    print("3) искать обход")

    while True:
        choice = input("Введите номер варианта: ").strip()

        if choice == "1":
            if wind_game():
                print("Старик даёт подсказку: 'Бойся тумана.'")
            else:
                print("Старик больше не хочет говорить.")
            break
        elif choice == "2":
            print("Мост трещит... но выдерживает.")
            break
        elif choice == "3":
            print("Ты находишь тихий обход.")
            break
        else:
            print("Ты стоишь и ничего не делаешь.")


def main():
    print("Добро пожаловать в игру!")
    left_path()


if __name__ == "__main__":
    main()

