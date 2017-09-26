#Oef 3 bereken uren em minuten in seconden
uur = int(input("geef het uur"))
minuut = int(input("geef de minuten"))
second = int(input("geef de seconden"))

totaal = (uur * 3600) + (minuut * 60) + second

print("het totaal aantal seconden is: {0}".format(totaal))