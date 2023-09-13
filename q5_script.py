montant_initial = float(input("Entrez le montant initial: "))
taux_interet = float(input("Entrez le taux d'interet annuel (en %): "))
nombre_annees_investissement = float(input("Entrez le nombre d'annees de l'investissement: "))
montant_final = montant_initial * (1 + (taux_interet) / 100) ** nombre_annees_investissement
print(round(montant_final, 2))