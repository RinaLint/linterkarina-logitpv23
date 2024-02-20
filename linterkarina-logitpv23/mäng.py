from random import *

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