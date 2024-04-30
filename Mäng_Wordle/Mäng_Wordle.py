import tkinter as tk
import random
from tkinter import simpledialog

def laadi_sõnad(sõnad):
    with open(sõnad, 'r', encoding='utf-8') as fail:
        sõnad = [rivi.strip().upper() for rivi in fail if len(rivi.strip()) == 5]
    return sõnad

def kontrolli_sõna(arvamine, sõna):
    tulemus = []
    for i, täht in enumerate(arvamine):
        if täht == sõna[i]:
            tulemus.append('green')
        elif täht in sõna:
            tulemus.append('yellow')
        else:
            tulemus.append('black')
    return tulemus

def uuenda_liidest(arvamine, tulemus):
    for i, täht in enumerate(arvamine):
        sisestus = sisestused[hetke_üritus][i]
        sisestus.delete(0, 'end')
        sisestus.insert('end', täht)
        sisestus.config(disabledforeground=tulemus[i], state='disabled')

def saatmine():
    global hetke_üritus
    arvamine = arvamine_muutuja.get().upper()
    if len(arvamine) != 5:
        tulemus_silt.config(text="Sõna peab olema 5 tähemärki pikk!")
        return

    tulemus = kontrolli_sõna(arvamine, hetke_sõna)
    uuenda_liidest(arvamine, tulemus)

    if arvamine == hetke_sõna or hetke_üritus == 5:
        tulemus_silt.config(text=f"Sõna: {hetke_sõna}")
        for sisestusrida in sisestused:
            for sisestus in sisestusrida:
                sisestus.config(state='disabled')
    else:
        hetke_üritus += 1
        tulemus_silt.config(text="")
        arvamine_muutuja.set("")

def algus_uuesti():
    global hetke_sõna, hetke_üritus
    hetke_sõna = random.choice(sõnad)
    hetke_üritus = 0
    arvamine_muutuja.set("")
    tulemus_silt.config(text="")

    for sisestusrida in sisestused:
        for sisestus in sisestusrida:
            sisestus.config(state='normal')
            sisestus.delete(0, 'end')

def lisa_sõna():
    uus_sõna = simpledialog.askstring("Lisa sõna", "Sisestage sõna, mida soovite lisada:")
    if uus_sõna:
        sõnad.append(uus_sõna.upper())

def eemalda_sõna():
    sõna_kustutada = simpledialog.askstring("Eemalda sõna", "Sisestage sõna, mida soovite eemaldada:")
    if sõna_kustutada:
        if sõna_kustutada.upper() in sõnad:
            sõnad.remove(sõna_kustutada.upper())
        else:
            tulemus_silt.config(text="Seda sõna pole loendis!")

# Initsialiseerimine
sõnad = laadi_sõnad('Sõnad.txt')
hetke_sõna = random.choice(sõnad)
hetke_üritus = 0

aken = tk.Tk()
aken.title("Sõnapilt")
aken.geometry("800x800")
aken.config(bg='lightblue')

# Создание рамки для выравнивания содержимого по левому краю
põhiraam = tk.Frame(aken, bg='lightblue')
põhiraam.pack(expand=True)

# Создание полей ввода для букв слова
sisestused = [[tk.Entry(põhiraam, font=('Arial', 36), width=2, bg='lightblue', fg='black') for _ in range(5)] for _ in range(6)]
for i, rida in enumerate(sisestused):
    for j, sisestus in enumerate(rida):
        sisestus.grid(row=i, column=j, padx=5, pady=5, sticky='w')  # Изменено расположение ячеек на левый край

# Поле ввода для предполагаемого слова
arvamine_muutuja = tk.StringVar()
arvamine_sisestus = tk.Entry(põhiraam, textvariable=arvamine_muutuja, font=('Arial', 36), width=8, bg='lightblue', fg='black')
arvamine_sisestus.grid(row=7, column=0, columnspan=5, pady=15, sticky='w')  # Изменено расположение поля ввода на левый край

saatmis_nupp = tk.Button(põhiraam, text="Saada", font=("Arial", 36) command=saatmine, bg='lightblue', fg='black', width=20, height=3)
saatmis_nupp.grid(row=8, column=0, columnspan=5, pady=15, sticky='w')

tulemus_silt = tk.Label(põhiraam, text="", font=('Arial', 36), bg='lightblue', fg='white')
tulemus_silt.grid(row=9, column=0, columnspan=5, pady=15, sticky='w')

algus_uuesti_nupp = tk.Button(põhiraam, text="Alusta uuesti", command=algus_uuesti, bg='lightblue', fg='black', width=20, height=3)
algus_uuesti_nupp.grid(row=10, column=0, columnspan=5, pady=15, sticky='w')

lisa_sõna_nupp = tk.Button(põhiraam, text="Lisa sõna", command=lisa_sõna, bg='lightblue', fg='black', width=20, height=3)
lisa_sõna_nupp.grid(row=11, column=0, columnspan=2, pady=15, padx=5, sticky='w')

eemalda_sõna_nupp = tk.Button(põhiraam, text="Eemalda sõna", command=eemalda_sõna, bg='lightblue', fg='black', width=20, height=3)
eemalda_sõna_nupp.grid(row=11, column=2, columnspan=2, pady=15, padx=15, sticky='w')

aken.mainloop()

 