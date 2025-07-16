# main_generator.py
import random
# TODO 3: Importiere die Funktionen 'find_max' und 'remove_duplicates'
# aus deinem eigenen Modul 'list_utils'.

from list_utils import find_max, remove_duplicates


def generate_random_numbers(count, min_val, max_val):
    """
    Generiert eine Liste von Zufallszahlen.
    """
    numbers = []
    # TODO 4: Generiere 'count' viele Zufallszahlen zwischen 'min_val' und 'max_val'
    # und füge sie der Liste 'numbers' hinzu. Nutze random.randint().
    for _ in range(count):
        numbers.append(random.randint(min_val, max_val))
    return numbers

if __name__ == "__main__":
    print("Willkommen zum Zufallszahlen-Generator und Listen-Helfer!")

    # TODO 5: Generiere eine Liste mit 10 Zufallszahlen zwischen 1 und 50.
    number_list = generate_random_numbers(10, 1, 50)
    print(number_list) 
    # TODO 6: Finde die größte Zahl in der generierten Liste und gib sie aus.
    max = find_max(number_list)
    print(f"Die höhste zahl hier ist: {max}")
    # TODO 7: Erstelle eine Liste mit Duplikaten zum Testen.
    dupli = [1, 1, 2, 2, 45, 45]
    # TODO 8: Entferne Duplikate aus der Liste und gib die bereinigte Liste aus.
    clean_list = remove_duplicates(dupli)
    print(clean_list)