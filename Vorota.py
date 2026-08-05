import random

def roots_game():
    safe = random.choice(["левый", "центральный", "правый"])
    print("Перед тобой три корня: левый, центральный, правый")
    print("Только один из ниx безопасный")

    choice = input("Какой корень выбираешь? ").lower()

    if choice == safe:
        print("Ты прошёл через корни")
        return True
    else:
        print("Корень извивается, тебя отталкивает назад")
        return False

def roots_scene():
    print("Ты подходишь  большой норе, оплетённой корнями.")

    print("1. Спуститься внутрь")
    print("2. Осмотреть корни")
    print("3. Обойти стороной")

    choice = input("Ваш выбор:")

    if choice == "1":
        roots_game()
    elif choice == "2":
        print("Корни влажные и скользкие. Ничего больше.")
    elif choice == "3":
        print("Ты осторожно обходишь нору.")
    else:
        print("Ты смотришь в темноту норы и не решаешься войти.")
