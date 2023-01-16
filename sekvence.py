# clanovi u sekvencama
#            0     1     2       3
osoba = ["sofija", 20, "plava", True]
print(osoba)

print(osoba[0])
print("godine:", osoba[1])

automobili = ["ford", "opel", "mercedes"]
print(automobili[1])


for x in range(5, 10, 2):
    print(x)

       #012345
kurs = "python"
# print(kurs[0])
# print(kurs[1])
# print(kurs[2])
# print(kurs[3])

duzina = len(kurs)
for x in range(len(kurs)):
#for x in range(6):
    #print(kurs[x], end="")
    print("na poziciji:", x, kurs[x])


# ustanova = "IT Academy"

# for index in range(len(ustanova)):
#     print(ustanova[index], end="")




primer = "zadatak1"
for index in range(len(primer)):
    print(primer[index]) 


broj_karaktera = len(primer)
index = 0

while index < broj_karaktera:
    print(primer[index])
    index += 1




# posto je py casse sensitive, njemu su mala i velika slova dve razlicite
# vrednosti, sa .lower() uvek ce smanjiuvati slova, sa .upper() uvek ce biti
# velika slova.

# korisnicko_ime = "admin"
# uneto_kor_ime = input("unesi korisnicko mime:")

# if korisnicko_ime == uneto_kor_ime.lower():
#     print("dobrodosli")
# else:
#     print("pogresni podaci")
#################################################


