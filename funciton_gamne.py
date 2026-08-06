from Vorota import roots_scene
from start import left_path
from game_test import right_path, clear


def main_menu():
    while True:
        clear()
        print("=" * 45)
        print("          ЗАТЕРЯННЫЙ ЛЕС")
        print("=" * 45)
        print("Перед тобой три пути.\n")
        print("1 - Отправиться к Старому мосту")
        print("2 - Войти в Туманный лес")
        print("3 - Исследовать Корневую нору")
        print("0 - Завершить путешествие")

        choice = input("\nКуда отправиться? ")

        if choice == "1":
            clear()
            print("Ты сворачиваешь на тропу, ведущую к Старому мосту...\n")
            left_path()

        elif choice == "2":
            clear()
            print("Ты делаешь шаг в густой туман...\n")
            right_path()

        elif choice == "3":
            clear()
            print("Перед тобой открывается огромная нора, оплетённая корнями...\n")
            roots_scene()

        elif choice == "0":
            clear()
            print("Путешествие окончено. До новых встреч!")
            break

        else:
            print("\nТакого варианта нет.")
            input("Нажми Enter, чтобы продолжить...")
            continue

        input("\nНажми Enter, чтобы вернуться в главное меню...")


if __name__ == "__main__":
    main_menu()