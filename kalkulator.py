import logging
logging.basicConfig(level=logging.DEBUG)

operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
number_1 = float(input("Podaj składnik 1: "))
number_2 = float(input("Podaj składnik 2: "))

information = ""
if operation == 1:
    information = "Dodaję"
    logging.info(f"{information} {number_1} i {number_2}")
    print(f"Wynik to: {number_1 + number_2}")
elif operation == 2:
    information = "Odejmuję"
    logging.info(f"{information} {number_1} i {number_2}")
    print(f"Wynik to: {number_1 - number_2}")
elif operation == 3:
    information = "Mnożę"
    logging.info(f"{information} {number_1} i {number_2}")
    print(f"Wynik to: {number_1 * number_2}")
elif operation == 4:
    information = "Dzielę"
    logging.info(f"{information} {number_1} i {number_2}")
    print(f"Wynik to: {number_1 / number_2}")