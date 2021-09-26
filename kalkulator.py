import logging

dzialanie = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
liczba_1 = input("Podaj składnik 1: ")
liczba_2 = input("Podaj składnik 2: ")
informacja = ""
if dzialanie == 1:
    informacja = "Dodaję"
elif dzialanie == 2:
    informacja = "Odejmuję"
elif dzialanie == 3:
    informacja = "Mnożę"
elif dzialanie == 4:
    informacja = "Dzielę"
print(informacja)