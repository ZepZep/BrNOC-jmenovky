# python 3
import csv
import sys

soubor = sys.argv[1]
jmena = []
funkce = []

pocetNaStranku = 8

slovTitul = {}
slovObraz = {}

slovTitul["org"] = "Organizátor"
slovTitul["norm"] = "Účastník"
slovTitul["vip"] = "VIP"
slovTitul["pred"] = "Přednášející"

slovObraz["org"] = "img/iluminat_pus.png"
slovObraz["norm"] = "img/brnenka^2.png"
slovObraz["vip"] = "img/ufo.png"
slovObraz["pred"] = "img/prednasejici_ico.png"

neznameFce = []

with open(soubor, "r") as csvfile:
    reader = csv.reader(csvfile)
    rownum = 0
    for row in reader:
        jmena.append(row[0])
        funkce.append(row[1])
        if row[1] not in slovTitul or row[1] not in slovObraz:
            slovTitul[row[1]] = ""
            slovObraz[row[1]] = ""
            neznameFce.append(row[1])
            
if len(neznameFce) > 0:
    print("Nektere funkce nejsou ve slovnicich:")
    print(neznameFce)
    sys.exit(1)

of = open("lidi.tex", "w")

for i in range(len(jmena)):
    if(i%pocetNaStranku == 0):
        of.write("\\newpage{}\n")
    line  = "\\confpin{"
    line += jmena[i] + "}{"
    line += slovTitul[funkce[i]] + "}{"
    line += slovObraz[funkce[i]] + "}\n"
    
    of.write(line)
