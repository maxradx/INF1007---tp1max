print (" Type de conversion :  \n "
                  "1: Kilometres vers Miles (K vers M) \n "
                  "2: Miles vers kilometres (M vers K) ")
choix = int(input("Entrez votre choix (1 ou 2): "))
distance = float(input("Entrez la distance a convertir: "))

if choix == 1 :
    miles = distance * 0.621371
    print(float(distance), "kilometres equivalent a", round(float(miles), 2), "miles.")

else :
    km = distance / 0.621371
    print(float(distance), "miles equivalent a", round(float(km), 2), "kilometres.")