chaine = input("Entre une phrase : ")

voyelles = "aeiouyAEIOUY"
compteur = 0

for lettre in chaine:
    if lettre in voyelles:
        compteur += 1

print("Nombre de voyelles :", compteur)