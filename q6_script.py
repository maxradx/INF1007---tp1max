poids = float(input("Entrez votre poids en kg: "))
taille = float(input("Entrez votre taille en m: "))
imc = poids / taille ** 2
print(round(imc, 2))
if imc < 18.5 :
    print("Vous etes en sous-poids")
elif imc < 24.9 :
    print("Votre poids est normal.")
elif imc < 30 :
    print("Vous etes en surpoids.")
else :
    print("Vous etes obese.")