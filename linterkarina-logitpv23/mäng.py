import random

valikud=["Kivi","Paber","Käärid"]
skoor_bot=0
skoor_kasutaja=0
while True: #See on lõpmatu tsükkel, mis jätkub seni, kuni tsüklist väljumise tingimus on täidetud.
    bot=random.choice(valikud) #Funktsioon valib loendist juhusliku elemendi "Kivi", "Paber" või "Käärid"
    kasutaja=input("Valige: Kivi, Paber või Käärid ").capitalize()  # funktsioon palub kasutajal sisestada ja teisendab selle suurtähtedeks
    if kasutaja not in valikud:
        print("Vale valik")
        break #See funktsioon katkestab tsükli täitmise ja liigub tsükli järel järgmise käsu juurde.

    print(f"Teie valik: {kasutaja}")
    print(f"bot valik: {bot}")
    if kasutaja==bot:
       print("Viik")
    elif (kasutaja=="Kivi" and bot=="Käärid") or (kasutaja=="Kärid" and bot=="Paber") or (kasutaja=="Paber" and bot=="Kivi"):
       print("Te võitsite")
       skoor_kasutaja+=1  #On operaator, mis suurendab muutuja väärtust etteantud arvu võrra.
    else:
       print("bot võitis")
       skoor_bot+=1

    print(f"Teie skoor: {skoor_kasutaja} and bot skoor: {skoor_bot}")
    kordus=input("Kas soovite veel mängida? (jah/ei): ").lower()  #See funktsioon teisendab stringi väiketähtedeks.
    if kordus!="jah":
        break
