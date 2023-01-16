

osoba = ["sofija", 25, "plava", False]

for index in range(len(osoba)):
    print(osoba[index])

for osobina in osoba:
    print(osobina)

#######################################################################
voce_i_povrce = ["jabuka", "beli luk", "crni luk", "banana", "mandarina", "lubenica", "krastavac"]

for stavka in voce_i_povrce:
    print(stavka)

for i in range(len(voce_i_povrce)):
    print(voce_i_povrce[i])
    print("na indexu:", i, "nalazi se", voce_i_povrce[i])


for index, vrednost in enumerate(voce_i_povrce):
    print("index:", index, "stavka", vrednost)

################################################################

automobili = ["citroen", "bmw", "kia", "yugo"]
for pozicija, auto in enumerate(automobili):
    if pozicija == 1:
        print("kupujem")
        break
    print("index:", pozicija, "automobil:", auto)

automobili.append("ford")
print(automobili)
automobili[2] = "kia pro ceed"
print(automobili)
del automobili[2]
print(automobili)
automobili.remove("bmw")
print(automobili)
automobili.pop(0)
print(automobili)

automobili[0]
broj_forda = 0
for index in range(len(automobili)):
    if automobili[index] == "ford":
        print("eo ga ford")
        broj_forda += 1
print("imam", broj_forda, "na placu")

automobili.clear()
print(automobili)

#####################################################

#slice-ovi


automobili = ["citroen", "opel", "ford", "audi", "bmw", "kia", "yugo"]

automobili_akcija = []
for i in range(len(automobili)):
    if i == 1 or i == 2 or i == 3:
        automobili_akcija.append(automobili[i])
print(automobili_akcija)

automobili_akcija = automobili[1:4]
print(automobili_akcija)

#########################################################

# vezba

#a = [3,7,1,9,2,4,5,12]

brojevi = [3,7,1,9,2,4,5,12]
parni = []
neparni = []

for broj in brojevi:
    if broj % 2 == 0:
        parni.append(broj)
    else:
        neparni.append(broj)
print(parni, neparni)
