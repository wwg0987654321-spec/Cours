comptes = {
    "Alice": 1500,
    "Bob": 800,
    "Charlie": 2000
}

nom = input("Entrez votre nom : ")

if nom in comptes:
    print(f"Bienvenue {nom} ! Vous avez {comptes[nom]}€.")

    while True:
        print("Choisissez une option :")
        print("Taper 1 : Prendre 500")
        print("Taper 2 : Mettre 500")
        print("Taper 3 : Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            comptes[nom] -= 500
            print(f"Vous avez retiré 500€. Nouveau solde : {comptes[nom]}€")

        elif choix == "2":
            comptes[nom] += 500
            print(f"Vous avez ajouté 500€. Nouveau solde : {comptes[nom]}€")

        elif choix == "3":
            print("Merci de votre visite, au revoir !")
            break

        else:
            print("Choix invalide, réessayez.")

else:
    print("Utilisateur inconnu.")
