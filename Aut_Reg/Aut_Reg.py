from MinuOmaMoodul import *

salasõnad=[]
kasutajanimed=[]
while True:
    print("1-registreerimine\n2-autoriseerimine\n3-nime või parooli muutmine\n4-unustanud parooli taastamine\n5-lõpetamine")
    vastus=int(input("Sisestage arv"))
    if vastus==1:
        print("Registreerimine")
        kasutajanimed,salasõnad=registreerimine(kasutajanimed,salasõnad)
    if vastus==2:
        print("Autoriseerimine")
    if vastus==3:
        print("Nime või parooli muutmine")
    if vastus==4:
        print("Unustanud parooli taastamine")
    if vastus==5:
        print("Lõpetamine")
        break
    else:
        print("Tundmatu valik")