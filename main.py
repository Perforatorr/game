from Vorota import roots_scene
from start import left_path
from game_test import right_path
from game_test import clear
import time


def main_menu():
    while True:
        clear()
        print("Путь через Затерянный Лес")
        print("\nВыберите сцену:")
        print("1. Левая тропа (Старый мост)")
        print("2. Правая тропа (Туманный лес)")
        print("3. Ворота (Корневая нора)")
        print("0. Выход из игры")

        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            left_path()
        elif choice == "2":
            right_path()
        elif choice == "3":
            roots_scene()
        elif choice == "0":
            clear()
            print("Спасибо за игру!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
            time.sleep(5)

if __name__ == "__main__":
    main_menu()
