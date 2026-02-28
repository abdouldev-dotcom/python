users={}
   
def ajouter_user():
    nom=input("Entrer le nom : ")
    age=int(input("Entrer son age :"))
    users[nom]=age
    print("Utilisateur ajouté")

def afficher_user():
    if len(users)==0 :
        print("Il n'y a pas d'utilisateur.")
    else:
        for nom, age in users.items():
            print(nom,"-",age, "ans")   

def supprimer_users():
    if len(users)==0 :
        print("Il n'y a rien a supprimé.")
    else:
        nom=input("Entrer le nom de l'utilisateur a supprimé :")
        if nom in users:
            del users[nom]
            print("Utilisateur supprimé.")
        else:
            print("Utilisateur introuvable")

def modifier_users():
  if len(users)==0:
    print("Cet utilisateur n'existe pas " )
  else:
    nom=input("Entrer le nom de l'utilisateur a modifier :")
  
    if nom in users:
        print("1 -Modifier le nom")
        print("2 -Modifier l'age")
        print("3 -Modifier le nom et l'age")
        print("4 -Retour")
        choix=input("Entrez votre choix")

        if choix == "1":
            nouveau_nom=input("Entrer son nouveau nom :")
            age =users[nom]
            del users[nom]
            users[nouveau_nom]=age
            print("Le nouveau nom de l'utilisateur est ",nouveau_nom," et son age est ",age)

        elif choix == "2":
            new_age=int(input("Entrer son nouvel age :"))
            users[nom]=new_age
            print("Le nom de l'utilisateur est ",nom, "et son nouvel age est ",new_age)
    
        elif choix == "3":
            nouveau_nom=input("Entrer son nouveau nom :")
            new_age=int(input("entrer son nouvel age :"))
            del users[nom]
            users[nouveau_nom]=new_age
            print("Le nouveau nom de l'utilisateur est ",nouveau_nom," et son nouvel age est ",new_age)

        elif choix=="4":
            return

    else:
        print("Utilisateur introuvable")

while True:
    print("\n--- MENU ---")
    print("1 - Ajouter un utilisateur")
    print("2 - Afficher les utilisateurs")
    print("3 - Modifier un utilisateur")
    print("4 - Supprimer un utilisateur")
    print("5 - Quitter")

    choix = input("Entrez votre choix : ")

    if choix == "1":
                ajouter_user()

    elif choix == "2":
                afficher_user()
                
    elif choix == "3":
                modifier_users()

    elif choix == "4":
                supprimer_users()

    elif choix == "5":
                print("Au revoir !")
                break

    else:
        print("Choix invalide, réessayez.")

                 