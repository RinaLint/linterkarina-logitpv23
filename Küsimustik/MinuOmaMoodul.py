from string import *
from time import sleep
from os import path, remove

def loe_ankeet(fail:str)->any:
    fail=open(fail,"r",encoding="utf-8")
    kus=[]
    vas=[]
    #kus_vas={}
    for line in fail:
        n=line.find(":")# , - разделитель
        kus.append(line[0:n].strip())
        vas.append(line[n+1:len(line)].strip())

        #k,v=line.strip().split(":")
        #kus_vas[k]=v

    fail.close()
    return kus,vas #,kus_vas

def lisa_kusimus(failinimi, kusimus, vastus):
    fail=open(failinimi, 'a', encoding='utf-8')
    fail.write(f"{kusimus}:{vastus}\n")
    fail.close()

def testi_osalejat(kusimused_vastused, nimi):
    print(f"Tere, {nimi}! Alustame testi.")
    kusimused=list(kusimused_vastused.keys())
    
    õiged_vastused=0
    for kusimus in kusimused:
        print(f"{nimi}, küsimus: {kusimus}")
        vastus=input("Sinu vastus: ")
        if vastus.lower()==kusimused_vastused[kusimus].lower():
            õiged_vastused+=1
    return õiged_vastused

from string import *
from time import sleep
from os import path, remove
def registreerimine(kasutajad:list,paroolid:list)->any:
    """Funktsioon tagastab kasutajad ja paroolid listid:
    :param list kasutajad:Kasutaja peab sisestama kasutajanime ja see tuleks nimekirja lisada
    :param list paroolid:Kasutaja peab sisestama parooli ja see parool tuleb nimekirja lisada
    :rtype:list,list
    """
    while True:
        nimi=input("Mis on sinu nimi? ")
        if nimi not in kasutajad:
            while True:
                parool=input("Mis on sinu parool? ")
                flag_p=False
                flag_l=False
                flag_u=False
                flag_d=False
                if len(parool)>=8:
                    parool_list=list(parool)
                    for p in parool_list:
                        if p in punctuation:
                            flag_p=True
                        elif p in ascii_lowercase:
                            flag_l=True
                        elif p in ascii_uppercase:
                            flag_u=True
                        elif p in digits:
                            flag_d=True
                    if flag_p and flag_u and flag_l and flag_d:
                        kasutajad.append(nimi)
                        paroolid.append(parool)
                    break
                else:
                    print("Nõrk salasõna!")
            break
        else:
            print("Selline kasutaja on juba olemas!")
    return kasutajad, paroolid
def autoriseerimine(kasutajad:list,paroolid:list):
    """Funktsioon kuvab ekraanile "Tere tulemast!" kui kasutaja on olemas nimekirjas
         Nimi on järjendis kasutajad
         Salasõna on paroolide järjendis
         Nimi ja salasõna indeksid on võrdsed
    :param list kasutajad:...
    :param list paroolid:...
    """
    p=0
    while True:
        nimi=input("Sisesta kasutajanimi: ")
        if nimi in kasutajad:
            while True:
                parool=input("Sisesta salasõna: ")
                p+=1
                try:
                    if kasutajad.index(nimi)==paroolid.index(parool):
                        print (f"Tere tulemast! {nimi}")
                        break
                except:
                    print("Vale nimi või salasõna!")
                    if p==5:
                        print("Proovi uuesti 10 sek pärast")
                        for i in range(10):
                            sleep(1)
                            print(f"On jäänud {10-i} sek")
        else:
            print("Kasutajat pole")
        break