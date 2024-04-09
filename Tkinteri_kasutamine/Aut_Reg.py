from tkinter import *
from tkinter import messagebox as mb

def tehtudvalik(var, nimi, text):
    f=var.get()
    if f:
        texbox.configure(show="")
        valik.configure(image=pilt1)
    else:
        texbox.configure(show="*")
        valik.configure(image=pilt2)
def aut():
    kasutajanimi=kasutaja.get()
    parool=texbox.get() 
    if (kasutajanimi,parool) in kasutajad:
        mb.showinfo("Autentimine", f"Tere tulemast, {kasutajanimi}!")
    else:
        mb.showerror("Autentimine", "Kasutajanimi ei ole registreeritud!")
def reg():
    kasutajanimi2=kasutaja2.get()
    parool2=texbox2.get()
    if (kasutajanimi2,parool2) not in kasutajad:
        kasutajad.append((kasutajanimi2,parool2))
        mb.showinfo("Registreerimine", f"Kasutaja {kasutajanimi2} registreeritud!")
    else:
        mb.showerror("Registreerimine", "Kasutajanimi on juba registreeritud!")
aken=Tk()
aken.geometry("700x700")
aken.title("Autoriseerimine või registreerimine")
aken.configure(bg="#3deff5")
aken.iconbitmap("icon.ico")
kasutajad=[]
pealkiri=Label(aken,
               text="Autoriseerimine",
               bg="#df7ef7",
               fg="#000000",
               cursor="sizing",
               font="Goudy_Old_Style 16",
               justify=CENTER,
               height=3,width=26)
raam=Frame(aken)
kasutaja=Entry(raam,
              bg="#f5a3a2",
              fg="#df7ef7",
              font="Goudy_Old_Style 16",
              width=16)
texbox=Entry(raam,
              bg="#f5a3a2",
              fg="#df7ef7",
              font="Goudy_Old_Style 16",
              width=16,
              show="*")
pilt1=PhotoImage(file="eye.png")
pilt2=PhotoImage(file="show.png")
var=BooleanVar()
valik=Checkbutton(raam,
                  image=pilt2,
                  variable=var,
                  onvalue=True,
                  offvalue=False,
                  command=lambda:tehtudvalik(var,valik,texbox))
nupp=Button(raam,
            text="Sisenema",
            bg="#f5a3a2",
            fg="#86e2eb",
            font="Goudy_Old_Style 16",
            width=16,
            command=aut)
pealkiri2=Label(aken,
               text="Registreerimine",
               bg="#df7ef7",
               fg="#000000",
               cursor="sizing",
               font="Goudy_Old_Style 16",
               justify=CENTER,
               height=3,width=26)
raam2=Frame(aken)
kasutaja2=Entry(raam2,
              bg="#f5a3a2",
              fg="#df7ef7",
              font="Goudy_Old_Style 16",
              width=16)
texbox2=Entry(raam2,
              bg="#f5a3a2",
              fg="#df7ef7",
              font="Goudy_Old_Style 16",
              width=16,
              show="*")
pilt1=PhotoImage(file="eye.png")
pilt2=PhotoImage(file="show.png")
var=BooleanVar()
valik2=Checkbutton(raam2,
                  image=pilt2,
                  variable=var,
                  onvalue=True,
                  offvalue=False,
                  command=lambda:tehtudvalik(var,valik2,texbox2))
nupp2=Button(raam2,
            text="Registreerima",
            bg="#000000",
            fg="#86e2eb",
            font="Goudy_Old_Style 16",
            width=16,
            command=reg)
pealkiri.pack()
raam.pack()
kasutaja.grid(row=0, column=0)
texbox.grid(row=0,column=1)
valik.grid(row=0,column=2)
nupp.grid(row=0,column=3)
pealkiri2.pack()
raam2.pack()
kasutaja2.grid(row=0, column=0)
texbox2.grid(row=0, column=1)
valik2.grid(row=0, column=2)
nupp2.grid(row=0, column=3)
aken.mainloop()