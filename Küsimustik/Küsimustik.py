from MinuOmaMoodul import *
from random import *

file=open("Ankeet.txt", "r",encoding="utf-8")
kasutajanimed=[]
salasõnad=[]
while True:
    print("1-Administraatori registreerimine\n2-Kasutaja\n3-Autoriseerimine")
    vastus=int(input("Sisestage arv "))

    if vastus==1:
        print("Administraatori registreerimine")
        kasutajanimed,salasõnad=registreerimine(kasutajanimed,salasõnad)
    elif vastus==2:
        print("Kasutaja")
        print("Tere tulemast viktoriinile!")
        nimi=input("Mis on sinu nimi? ")
        print("Tere", nimi)
        õigevastus=0
        for rida in file:
            N=rida.split(":")
            print(N[0])
            katsed=3
            while katsed>0:
                sisend=input("Vastus: ").strip()
                if sisend==N[1].strip():
                    õigevastus+=1
                    print("Tubli!")
                else:
                    katsed-=1
                    print("Viga. Teil on",katsed,"katse.")
            else:
                print("Enam ktseid pole jäänud. Õige vastus on:",N[1].strip())
        print("Õigete vastuste arv:",õigevastus)
    elif vastus==3:
        autoriseerimine(kasutajanimed,salasõnad)
        küsimused=loe_ankeet("Ankeet.txt")
        print(f"Küsimused on: "+str(küsimused[0]),"Vastused on: "+str(küsimused[1]))
        file.close()
