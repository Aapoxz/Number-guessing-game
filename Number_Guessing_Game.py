import random as rand

number = rand.randint(1, 30) # Generoidaan random numero 1-30 väliltä
guess = int(input("Arvaa luku väliltä 1-30: "))

if guess == number:
    print("Hienoa! Arvasit luvun oikein ja voitit pelin")
elif number < 1:
    print("Arvaus oli alle 1, hävisit pelin")
elif number > 30:
    print("Arvaus oli suurermpi kuin 30, hävisit pelin")
else:
    print(f"Voi ei! arvasit väärin ja hävisit pelin, oikea numero oli {number}")