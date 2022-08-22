#Kysytään tiedot
kanta = float(input('Anna suorakulmion kanta: '))
korkeus = float(input('Anna suorakulmion korkeus: '))

#Laskutoimitukset
piiri = (kanta * 2) + (korkeus * 2)
ala = kanta * korkeus

#Tulostukset
print(f"piiri = {piiri}")
print(f"ala = {ala}")


