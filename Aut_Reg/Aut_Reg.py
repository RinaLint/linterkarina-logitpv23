from MinuOmaMoodul import *
salasõnad=["Parool.1"]
kasutajanimed=["Kasutajanimed.1"]
while True:
    print(kasutajanimed)
    print(salasõnad)
    print("1-registreerimine\n2-autoriseerimine\n3-nime või parooli muutmine\n4-unustanud üarooli taastamine\n5-lõpetamine")
    vastus=int(input("Sisestage arv "))
    if vastus==1:
        print("registreerimine")
        kasutajanimed,salasõnad=registreerimine(kasutajanimed,salasõnad)
    elif vastus==2:
        print("autoriseerimine")
        autoriseerimine(kasutajanimed,salasõnad)
    elif vastus==3:
        print("nime või parooli muutmine")
        vastus=input("Kas muudame nime, parooli või mõlemad ")
        if vastus=="nime":
            kasutajanimed=nimi_või_parooli_muutmine(kasutajanimed)
        elif vastus=="parool":
            salasõnad==nimi_või_parooli_muutmine(salasõnad)
        elif vastus=="mõlemad":
            kasutajanimed=nimi_või_parooli_muutmine(kasutajanimed)
            salasõnad==nimi_või_parooli_muutmine(salasõnad)
    elif vastus==4:
        print("Unustanud parooli taastamine")
        kasutajanimed, salasõnad==unustanud_parooli_taastamine(kasutajanimed, salasõnad)
    elif vastus==5:
        print("lõpetamine")
        break
    else:
        print("Tundmatu valik") 