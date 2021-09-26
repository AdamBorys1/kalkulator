import logging
logging.basicConfig(level=logging.DEBUG)

dzialanie = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
liczba_1 = float(input("Podaj składnik 1: "))
liczba_2 = float(input("Podaj składnik 2: "))

informacja = ""
if dzialanie == 1:
    informacja = "Dodaję"
elif dzialanie == 2:
    informacja = "Odejmuję"
elif dzialanie == 3:
    informacja = "Mnożę"
elif dzialanie == 4:
    informacja = "Dzielę"
logging.info(f"{informacja} {liczba_1} i {liczba_2}")

if dzialanie == 1:
    print(f"Wynik to: {liczba_1 + liczba_2}")
elif dzialanie == 2:
    print(f"Wynik to: {liczba_1 - liczba_2}")
elif dzialanie == 3:
    print(f"Wynik to: {liczba_1 * liczba_2}")
elif dzialanie == 4:
    print(f"Wynik to: {liczba_1 / liczba_2}")