import random
import time
import os
from colorama import init, Fore

init(autoreset=True)


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def whisper_game():
    sounds = ["са", "ху", "шо", "хи", "ша"]

    secret = random.sample(sounds, 3)

    print(Fore.YELLOW + "Нужно запомнить последовательность:")
    print(Fore.CYAN + "-".join(secret))

    time.sleep(3)
    clear()

    answer = input(Fore.GREEN + "Повтори через дефис: ")

    if answer == "-".join(secret):
        print(Fore.GREEN + "Дух одобрительно колышется и указывает путь.")
        return True
    else:
        print(Fore.RED + "Шёпот искажается... Дух уводит тебя в сторону.")
        return False


def right_path():
    print(Fore.BLUE + "Ты входишь в туманный лес. Перед тобой появляется Дух.")
    print(Fore.CYAN + "1 - обратиться к Духу")
    print(Fore.YELLOW + "2 - спрятаться")
    print(Fore.LIGHTGREEN_EX + "3 - убежать")

    choice = input(Fore.WHITE + "Выбор: ")

    if choice == "1":
        whisper_game()

    elif choice == "2":
        print(Fore.BLUE + "Дух проплывает мимо.")

    elif choice == "3":
        print(Fore.RED + "Ты убегаешь в неизвестную часть леса.")

    else:
        print(Fore.LIGHTBLACK_EX + "Ты молчишь, и Дух исчезает.")

