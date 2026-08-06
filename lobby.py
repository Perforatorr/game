print("Ты заблудился в Затерянном лесу---")
print("Выбери одну из троп---")
print("---1 тропа - Левая тропа---")
print("---2 тропа - Правая тропа---")
print("---3 тропа - Корневая нора---")
print("---Какую выберешь?---")

choice = input("Ваш выбор: ")

if choice == "1":
    import start
    start.main()
elif choice == "2":
    import game_test
    game_test.main()
elif choice == "3":
    import Vorota
    Vorota.main()
else:
    print("Ты смотришь на тропы и не решаешься идти.")
