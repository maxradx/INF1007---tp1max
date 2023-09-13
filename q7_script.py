secondes = int(input("Entrez le nombre de secondes: "))
annees = secondes / 31536000
semaines = (annees % 1) * (365/7)
jours = (semaines % 1) * 7
heures = (jours % 1) * 24
minutes = (heures % 1) * 60
secondesRestantes = (minutes % 1) * 60


estAnneesNonNull = annees // 1
estSemaineNonNull = semaines // 1
estJoursNonNull = jours // 1
estHeursNonNull = heures // 1
estMinutesNonNull = minutes // 1
estSecondesRestantes = secondesRestantes // 1



print("En", secondes, "secondes, on a: ", end="")

if estAnneesNonNull > 0 :
    print(int(estAnneesNonNull), " annees, ", end="")
if estSemaineNonNull > 0 :
    print(int(estSemaineNonNull), "semaines, ", end ="")
if estJoursNonNull > 0 :
    print(int(estJoursNonNull), "jours, ", end="")
if estHeursNonNull > 0 :
    print(int(estHeursNonNull), "heures, ", end ="")
if estMinutesNonNull > 0 :
    print(int(estMinutesNonNull), "minutes ", end ="")
if estSecondesRestantes > 0 :
    print("et ", end="")
    print(int(estSecondesRestantes), "secondes", end ="")

print(".") #perso : attention le point va etre espace si termine a minute