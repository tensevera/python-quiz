# Program na testovani
# Program se me zepta na otazky
# Podle toho jak odpovim mi napise pocet bodu

# Moodle/Google Forms

# Kolik nohou má pes - 4 
# Je Scratch programovací jazyk? - ano
# Kolik očí má ryba v Simpsonových - 3
# Pro co šel tvůj táta? - mléko
# Kolik je 1+1? - 2
# Působí na tebe právě teď radiace? - ano
# Kolik očí má člověk? - 2
# V jakém roce vznikl Python? - 1991


pocet_bodu = 0

odpoved = int(input("Kolik nohou má pes?\n"))
if (odpoved == 4):
    print("Jsi genius")
    pocet_bodu += 1

odpoved = input("Je Scratch programovací jazyk?\n")
if (odpoved == "ano"):
    print("Jsi genius")
    pocet_bodu += 1

odpoved =int(input("kolik ocí ryba v simpsonových?\n"))
if (odpoved == 3):
    print("Joe mama")
    pocet_bodu += 1

odpoved = input("pro co sel tvuj tata?\n")
if (odpoved == "mleko" or odpoved=="pro tebe ne"):
    print("Jsi genius")
    pocet_bodu += 1

odpoved = int(input("kolik je 1+1?\n"))
if (odpoved == 2):
    print("pán študoval")
    pocet_bodu += 1

odpoved = input("pusobí na tebe právě radiace?\n")
if (odpoved == "ano"):
    print("Jsi genius")
    pocet_bodu += 1
elif (odpoved == "ne"):
    print(" s alobalovou cepickou más pravdu")
 
odpoved = int(input("kolik oci ma zpravna ezo gal?\n"))
if (odpoved == 3):
    print('KAM9NEK PRO TEBE')
    pocet_bodu += 1   

odpoved = int(input("kdy vznikl python?\n"))
if (odpoved == 1991):
    print("Jsi genius")
    pocet_bodu += 1

print(pocet_bodu)