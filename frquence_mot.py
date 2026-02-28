phrase = input("Entrez une phrase : ")
phrase=phrase.lower()

mot = input("Entrez le mot a compté : ", )
mot=mot.lower()
compteur=0
mots = phrase.split()
for m in mots :
    if m==mot:
        compteur=compteur+1

if compteur>0:
    print("le nombre de fois que le mot", mot ,"apparait est :" ,compteur)
else:
    print("le mot ",mot," n'apparait pas")


