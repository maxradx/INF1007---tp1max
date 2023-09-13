print(("Choisissez une operation: "
       "\n 1. Addition"
        "\n 2. Soustraction "
        "\n 3. Multiplication "
        "\n 4. Division "))

choix = int(input("Saisissez le numéro de l'opération choisie: "))

if choix == 1 :
    nombre1 = float(input("Entrez le premier nombre: "))
    nombre2 = float(input("Entrez le second nombre: "))
    estAddition = nombre1 + nombre2
    print(estAddition)

elif choix == 2:
    nombre1 = float(input("Entrez le premier nombre: "))
    nombre2 = float(input("Entrez le second nombre: "))
    estSoustraction = nombre1 - nombre2
    print(estSoustraction)

elif choix == 3 :
    nombre1 = float(input("Entrez le premier nombre: "))
    nombre2 = float(input("Entrez le second nombre: "))
    estMultiplication = nombre1 * nombre2
    print(estMultiplication)

elif choix == 4 :
        nombre1 = float(input("Entrez le premier nombre: "))
        nombre2 = float(input("Entrez le second nombre: "))
        if nombre2 == 0 :
                print("Erreur: Division par zero.")
        else :
            estDivision = nombre1 / nombre2
            print(estDivision)

else:
    print("Erreur. L'opération choisie n'est pas valide.")