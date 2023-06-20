
import os
import sys
import time
import random
from pathlib import Path

def recipe_management_app():
    print("Witaj w aplikacji zarządzania przepisami!")
    print("Co chcesz zrobić?")
    print("1. Zarządzaj przepisami")
    print("2. Graj w grę przepisową")

    choice = input("Wybierz opcję (1 lub 2): ")

    if choice == '1':
        wypiszwybory()
    elif choice == '2':
        play_recipe_game()
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        recipe_management_app()


def play_recipe_game():
    print("Witaj w grze przepisowej!")
    print("Twoim zadaniem jest odgadnąć brakujące składniki w podanych przepisach.")
    print("Gotowy? Zaczynamy!")

    while True:
        recipe = random.choice(recipes)
        ingredients = recipe["ingredients"]


        ingredient_to_remove = random.choice(ingredients)
        hidden_ingredients = [ingredient if ingredient != ingredient_to_remove else "___" for ingredient in ingredients]

        print("\nBrakujące składniki w przepisie:")
        for ingredient in hidden_ingredients:
            print("- " + ingredient)

        guess = input("\nPodaj brakujący składnik: ")

        if guess.lower() == ingredient_to_remove.lower():
            print("Brawo! Zgadłeś!")
            print(f"\nPrzepis na danie: {recipe['name']}")
        else:
            print(f"Niestety, to nieprawidłowa odpowiedź. Prawidłowy składnik to: {ingredient_to_remove}")

            print(f"\nPrzepis na danie: {recipe['name']}")

        while True:
            play_again = input("\nCzy chcesz zagrać ponownie? (tak/nie): ")
            if play_again.lower() == "tak":
                break
            elif play_again.lower() == "nie":
                recipe_management_app()
                return
            else:
                print("Nieprawidłowa odpowiedź. Wpisz 'tak' lub 'nie'.")


def wypiszwybory():
    print("1) Przeczytaj przepis")
    print("2) Stwórz przepis")
    print("3) Stwórz kategorię")
    print("4) Usuń przepis")
    print("5) Usuń kategorię")
    print("6) Losuj przepis")
    print("7) Oceń przepis")
    print("8) Wyświetl przepisy według oceny")
    print("9) Liczba przepisów w poszczególnych kategoriach")
    print("10) Zakończ program")


def funkcja1():
    print("Wybierz kategorię przepisu:")
    guide = Path(".", "Recipes")
    categories = list(Path(guide).glob('*'))

    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category.stem}")

    wyborkategorii = int(input("Którą kategorię wybierasz? "))
    chosen_category = categories[wyborkategorii - 1]
    przepisy = list(Path(chosen_category).glob("*.txt"))

    for i, przepis in enumerate(przepisy, start=1):
        print(f"{i}. {przepis.stem}")

    wyborprzepisu = int(input("Który przepis wybierasz? "))
    chosen_przepis = przepisy[wyborprzepisu - 1]

    with open(chosen_przepis, "r") as file:
        os.system("cls")
        print(file.read())
        time.sleep(5)

    input("Naciśnij Enter, aby powrócić do menu głównego.")

def funkcja2():
    print("Wybierz kategorię przepisu:")
    guide = Path(".", "Recipes")
    categories = list(Path(guide).glob('*'))

    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category.stem}")

    wyborkategorii = int(input("Którą kategorię wybierasz? "))
    chosen_category = categories[wyborkategorii - 1]

    przepis = input("Podaj nazwę przepisu: ")
    przepis_path = Path(chosen_category, f"{przepis}.txt")

    with open(przepis_path, "w") as file:
        file.write(input("Podaj treść przepisu: "))

    print(f"Pomyślnie utworzono przepis {przepis}")

    input("Naciśnij Enter, aby powrócić do menu głównego.")




def funkcja3():
    guide = Path(".", "Recipes")
    kategoria = input("Podaj nazwę kategorii: ")
    stworzona = os.makedirs(Path(guide, kategoria))
    print(f"Pomyślnie stworzono kategorię {kategoria}")

    input("Naciśnij Enter, aby powrócić do menu głównego.")


def funkcja4():
    print("Wybierz kategorię przepisu:")
    guide = Path(".", "Recipes")
    categories = list(Path(guide).glob('*'))

    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category.stem}")

    wyborkategorii = int(input("Którą kategorię wybierasz? "))
    chosen_category = categories[wyborkategorii - 1]
    przepisy = list(Path(chosen_category).glob("*.txt"))

    for i, przepis in enumerate(przepisy, start=1):
        print(f"{i}. {przepis.stem}")

    wyborprzepisu = int(input("Który przepis usuwasz? "))
    chosen_przepis = przepisy[wyborprzepisu - 1]

    os.remove(chosen_przepis)
    print(f"Pomyślnie usunięto przepis {chosen_przepis.stem}")

    input("Naciśnij Enter, aby powrócić do menu głównego.")


def funkcja5():
    print("Wybierz kategorię przepisu:")
    guide = Path(".", "Recipes")
    categories = list(Path(guide).glob('*'))

    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category.stem}")

    wyborkategorii = int(input("Którą kategorię usuwasz? "))
    chosen_category = categories[wyborkategorii - 1]

    przepisy = list(Path(chosen_category).glob("*.txt"))

    for przepis in przepisy:
        os.remove(przepis)

    os.rmdir(chosen_category)
    print(f"Pomyślnie usunięto kategorię {chosen_category.stem}")

    input("Naciśnij Enter, aby powrócić do menu głównego.")


def funkcja6():
    print("Losowanie przepisu:")

    guide = Path(".", "Recipes")
    przepisy = list(Path(guide).rglob("*.txt"))

    if not przepisy:
        print("Brak dostępnych przepisów.")
        return

    wyborprzepisu = random.randint(0, len(przepisy) - 1)
    chosen_przepis = przepisy[wyborprzepisu]

    kategoria = chosen_przepis.parent.stem
    nazwa_przepisu = chosen_przepis.stem

    print(f"Nazwa przepisu: {nazwa_przepisu}")
    print(f"Kategoria: {kategoria}")

    with open(chosen_przepis, "r") as file:
        os.system("cls")
        print(file.read())
        time.sleep(5)

    input("Naciśnij Enter, aby powrócić do menu głównego.")


def funkcja7():
    print("Wybierz kategorię przepisu:")
    guide = Path(".", "Recipes")
    categories = list(Path(guide).glob('*'))

    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category.stem}")

    wyborkategorii = int(input("Którą kategorię wybierasz? "))
    chosen_category = categories[wyborkategorii - 1]
    przepisy = list(Path(chosen_category).glob("*.txt"))

    if not przepisy:
        print("Brak przepisów w wybranej kategorii.")
        return

    print("Dostępne przepisy:")
    for i, przepis in enumerate(przepisy, start=1):
        print(f"{i}. {przepis.stem}")

    wyborprzepisu = int(input("Wybierz numer przepisu: "))
    chosen_przepis = przepisy[wyborprzepisu - 1]

    ocena = int(input("Podaj ocenę przepisu od 1 do 5 gwiazdek: "))
    if ocena < 1 or ocena > 5:
        print("Nieprawidłowa ocena. Wybierz wartość od 1 do 5.")
        return

    oceny_folder = Path(".", "oceny")
    oceny_folder.mkdir(exist_ok=True)

    przepis_oceny_path = Path(oceny_folder, f"{chosen_przepis.stem}_oceny.txt")
    with open(przepis_oceny_path, "a") as file:
        file.write(str(ocena) + "\n")

    print(f"Pomyślnie oceniono przepis {chosen_przepis.stem}.")

    input("Naciśnij Enter, aby powrócić do menu głównego.")


def funkcja8():
    print("Wybierz kategorię przepisu:")
    guide = Path(".", "Recipes")
    categories = list(Path(guide).glob('*'))

    if not categories:
        print("Brak dostępnych kategorii.")
        return

    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category.stem}")

    wyborkategorii = int(input("Którą kategorię wybierasz? "))
    chosen_category = categories[wyborkategorii - 1]
    przepisy = list(Path(chosen_category).glob("*.txt"))

    if not przepisy:
        print("Brak przepisów w wybranej kategorii.")
        return

    oceny_przepisow = {}
    oceny_folder = Path(".", "oceny")

    for przepis in przepisy:
        przepis_oceny_path = Path(oceny_folder, f"{przepis.stem}_oceny.txt")
        if przepis_oceny_path.exists():
            with open(przepis_oceny_path, "r") as file:
                oceny = file.read().splitlines()
                oceny = list(map(int, oceny))
                if oceny:
                    oceny_przepisow[przepis] = sum(oceny) / len(oceny)

    if not oceny_przepisow:
        print("Brak ocen przepisów w wybranej kategorii.")
        return

    posortowane_przepisy = sorted(oceny_przepisow, key=oceny_przepisow.get, reverse=True)

    print("Przepisy posortowane według oceny:")
    for i, przepis in enumerate(posortowane_przepisy, start=1):
        print(f"{i}. {przepis.stem} (ocena: {oceny_przepisow[przepis]:.2f})")

    input("Naciśnij Enter, aby powrócić do menu głównego.")
def funkcja9():
    guide = Path(".", "Recipes")
    categories = list(Path(guide).glob('*'))

    liczba_przepisow = {}

    for category in categories:
        przepisy = list(Path(category).glob("*.txt"))
        liczba_przepisow[category.stem] = len(przepisy)

    print("Liczba przepisów w poszczególnych kategoriach:")
    for kategoria, liczba in liczba_przepisow.items():
        print(f"{kategoria}: {liczba} przepisów")

    input("Naciśnij Enter, aby powrócić do menu głównego.")



def funkcja10():
    sys.exit()


recipes = [
    {
        "name": "Spaghetti Bolognese",
        "ingredients": ["makaron", "mięso mielone", "cebula", "sos pomidorowy"]
    },
    {
        "name": "Sałatka Cezar",
        "ingredients": ["sałata", "kurczak", "grzanki", "parmezan"]
    },
    {
        "name": "Kanapka z awokado",
        "ingredients": ["chleb", "awokado", "pomidory", "rukola"]
    },
    {
        "name": "Omlet",
        "ingredients": ["jajka", "szynka", "ser", "cebula"]
    },
    {
        "name": "Tarta z warzywami",
        "ingredients": ["ciasto francuskie", "brokuły", "papryka", "ser"]
    },
    {
        "name": "Zupa pomidorowa",
        "ingredients": ["pomidor", "cebula", "czosnek", "śmietana", "bazylia"]
    },
    {
        "name": "Kotlet schabowy",
        "ingredients": ["schab", "jajko", "mąka", "bułka tarta"]
    },
    {
        "name": "Risotto z grzybami",
        "ingredients": ["ryż", "grzyby", "cebula", "bulion", "parmezan"]
    },
    {
        "name": "Krem z dyni",
        "ingredients": ["dynia", "cebula", "czosnek", "śmietana"]
    }
]
imie = input("Hej, jak masz na imię? ")
os.system('cls')
print(f"Hej, {imie}. Czego tu szukasz?")
recipe_management_app()
while True:
    time.sleep(2)
    os.system('cls')
    wypiszwybory()

    try:
        wybor = int(input("Wybierz jedną z powyższych opcji: "))
    except ValueError:
        print("Nieprawidłowy wybór. Wybierz numer opcji.")
        continue

    if wybor == 1:
        funkcja1()
    elif wybor == 2:
        funkcja2()
    elif wybor == 3:
        funkcja3()
    elif wybor == 4:
        funkcja4()
    elif wybor == 5:
        funkcja5()
    elif wybor == 6:
        funkcja6()
    elif wybor == 7:
        funkcja7()
    elif wybor == 8:
        funkcja8()
    elif wybor == 9:
        funkcja9()
    elif wybor == 10:
        funkcja10()
    else:
        print("Nieprawidłowy wybór. Wybierz numer opcji.")
