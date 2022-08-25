#Kysytään tiedot
kanta = float(input('Anna suorakulmion kanta: '))
korkeus = float(input('Anna suorakulmion korkeus: '))

#Laskutoimitukset
piiri = (kanta * 2) + (korkeus * 2)
ala = kanta * korkeus

#Tulostukset
print(f"Suorakulmion piiri on = {piiri:.2f}")
print(f"Suorakulmion ala on = {ala:.2f}")

