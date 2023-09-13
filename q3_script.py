phrase = str(input("Veuillez entrer une phrase: "))
nombre_de_mots = 1
caractere = str(" ")
i=0


while i < len(phrase) :
    if phrase[i] == caractere :
        nombre_de_mots += 1
    i += 1
print("La phrase contient", nombre_de_mots, "mots.")
print("Phrase en majuscules:", phrase.upper())