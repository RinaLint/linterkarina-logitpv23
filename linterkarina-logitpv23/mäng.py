from random import *

valikud=["Kivi","Paber",Käärid"]
kasutaja1=0
kasutaja2=0
while True:
    kasutaja1=random.choice(valikud)
    kasutaja2=input("Valige: Kivi, Paber või Käärid ").capitalize()
    if kasutaja not in valikud:
        print("Vale valik")
        break
    print(f"Teie valik: {"kasutaja2"}
    print(f"Kasutaja1 valik: {"kasutaja1"}
    if kasutaja2==kasutaja1:
       print("Viik")
    elif (kasutaja2=="Kivi" and kasutaja1=="Käärid") or (kasutaja2=="Kärid" and kasutaja1=="Paber") or (kasutaja2=="Paber" and kasutaja1=="Kivi"):
       print("Te võitsite")
       skoor_kasutaja2+=1
    else:
       print("kautaja1 võitis")
       skoor_kasutaja1+=1

    print(f"Teie skoor: {skoor_kasutaja2} and kasutaja1 skoor: {skoor_kasutaja1}")
    kordus=input("Kas soovite veel mängida? (jah/ei): ").lower()
    if kordus!="jah":
        break











player1=input("Введите имя первого игрока: ").capitalize()
player2=input("Введите имя второго игрока: ").capitalize()
mylist=["kivi","käärid","paber"]
result={player1:0,player2:0}
while True:
    
        print("Ничья!")
    elif ("player1_choice=="kivi" and player2_choice=="käärid"\nplayer1_choice=="käärid" and player2_choice=="paber"\nplayer1_choice=="paber" and player2_choice=="kivi""):
        print(f"{player1} побеждает!")
        result[player1]+=1
    else:
        print(f"{player2} побеждает!")
    result[player2]+=1
    print("Текущие счета:")
    for player, result in result.items():
        print(f"{player}: {score}")
    play_again=input("Хотите сыграть еще раз? (да/нет): ").lower()
    if play_again != "да":
        break
