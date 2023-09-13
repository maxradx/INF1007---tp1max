choix = int(input("Choisissez une operation: \n 1. Addition"
                  "\n 2. Soustraction "
                  "\n 3. Multiplication "
                  "\n 4. Division "))

match choix :
    case n if n == 1 :
        nombre1 = float(input("Entrez le premier nombre: "))
        nombre2 = float(input("Entrez le second nombre: "))
        addition = nombre1 + nombre2
        print(addition)
    case n if n == 2 :
        nombre1 = float(input("Entrez le premier nombre: "))
        nombre2 = float(input("Entrez le second nombre: "))
        soustraction = nombre1 - nombre2
        print(soustraction)

    case n if n == 3 :
        nombre1 = float(input("Entrez le premier nombre: "))
        nombre2 = float(input("Entrez le second nombre: "))
        multiplication = nombre1 * nombre2
        print(multiplication)

    case n if n == 4 :
        nombre1 = float(input("Entrez le premier nombre: "))
        nombre2 = float(input("Entrez le second nombre: "))
        if nombre2 == 0 :
                print("Erreur: Division par zero.")
        else :
            division = nombre1 / nombre2
            print(division)

    case other :
        print("Erreur. L'opération choisie n'est pas valide.")