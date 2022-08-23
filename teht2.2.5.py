import math

#Arvot
luoti = (13.3)
naula = (32 * luoti)
leiviskä = (20 * naula)

#Kysytään tiedot
arvo1lei = float(input('Anna leiviskät: '))
arvo2nau = float(input('Anna naulat: '))
arvo3luo = float(input('Anna luodit: '))
grammayht = luoti * arvo3luo + naula * arvo2nau + leiviskä * arvo1lei
#kilot = gramma / 1000

kg = math.floor(grammayht // 1000)
grammayht2 = grammayht % 1000

#Laskutoimitus

print(f"Massa nykymittojen mukaan: \n{kg} kilogrammaa ja {grammayht2:.2f} grammaa.")





#Laske yllämainittujen muuttujien yhteis gramma
#Pitää tulostaa monta kg ja grammaa
#Tee muuttuja gramma (summa)
#Jaa summa lopuksi / 1000 niin saat kilot
#Muuttuja kilo = math.floor(gramma / 1000)
#Halutaan kokonaislukuna kilot, ei desimaalia
#math.floor komento. Pyöristää luvut alaspäin, käytä tätä kun jaat summan 1000 niin saat kilot.
#Lopuksi laske vielä jämä grammat

#Kaksi // merkkiä unohtaa desimaalit