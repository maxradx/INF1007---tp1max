a = float(input("Veuillez entrer la valeur de a (coefficient de x^2): "))
b = float(input("Veuillez entrer la valeur de b (coefficient de x): "))
c = float(input("Veuillez entrer la valeur de c (terme constant): "))

delta = (b**2) - (4*a*c)

if delta < 0  :
    print("Le projectile n'atteint jamais l'altitude désirée.")
if delta == 0 :
    print("Le projectile atteint l'altitude à un seul moment précis.")
    x = (-b) / (2*a)
    print("Instant de l'impact: ", x)
if delta > 0 :
    print("Le projectie atteint l'altitude à deux moments distincts.")

