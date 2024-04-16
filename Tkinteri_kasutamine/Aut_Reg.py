from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import smtplib, ssl
from email.message import EmailMessage
import imghdr

def tehtudvalik(var, nimi, text):
    f=var.get()
    if f:
        text.configure(show="")
        nimi.configure(image=pilt1)
    else:
        text.configure(show="*")
        nimi.configure(image=pilt2)
def aut():
    kasutajanimi=kasutaja.get()
    parool=texbox.get() 
    if (kasutajanimi,parool) in kasutajad:
        mb.showinfo("Autentimine", f"Tere tulemast, {kasutajanimi}!")
    else:
        mb.showerror("Autentimine", "Kasutajanimi ei ole registreeritud!")
def reg():
    mail=sd.askstring("Kirjuta oma e-posti!", "Kuhu saada kirja?")
    password=sd.askstring("Kirjuta om parool!", "Kirjuta oma salasõna")
    email(mail, password)
    kasutajanimi2=kasutaja2.get()
    parool2=texbox2.get()
    if (kasutajanimi2,parool2) not in kasutajad:
        kasutajad.append((kasutajanimi2,parool2))
        mb.showinfo("Registreerimine", f"Kasutaja {kasutajanimi2} registreeritud!")
    else:
        mb.showerror("Registreerimine", "Kasutajanimi on juba registreeritud!")
def muuda():
    vana_kasutajanimi=kasutaja_muuda.get()
    vana_parool=texbox_muuda.get()
    uus_kasutajanimi=uus_kasutaja.get()
    uus_parool=uus_texbox.get()
    kasutaja_info=(vana_kasutajanimi, vana_parool)
    if kasutaja_info in kasutajad:
        kasutajad.remove(kasutaja_info)
        kasutajad.append((uus_kasutajanimi, uus_parool))
        mb.showinfo("Muuda nime ja parolit", "Kasutaja andmed edukalt muudetud!")
    else:
        mb.showerror("Muuda nime ja parolit", "Sellist kasutaja ei leitud!")
def email(mail:str, password:str):
    smtp_server="smtp.gmail.com"
    port=587
    sender_email="karinalinter7@gmail.com"
    password=password
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg.set_content("")
    msg['Subject']="Olete edukalt registreeritud!"
    msg['From']="Karina Linter" 
    msg['To']=mail
    try:
        server=smtplib.SMTP(smtp_server,port)
        server.starttls(context=context)
        server.login(sender_email,password)
        server.send_message(msg)
    finally:
        server.quit()
aken=Tk()
aken.geometry("800x800")
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
              fg="#000000",
              font="Goudy_Old_Style 16",
              width=16)
texbox=Entry(raam,
              bg="#f5a3a2",
              fg="#000000",
              font="Goudy_Old_Style 16",
              width=16,
              show="*")
pilt1=PhotoImage(file="eye.png")
pilt2=PhotoImage(file="show.png")
var=BooleanVar()
valik=Checkbutton(raam,
                  image=pilt1,
                  variable=var,
                  onvalue=True,
                  offvalue=False,
                  command=lambda:tehtudvalik(var,valik,texbox))
nupp=Button(raam,
            text="Sisenema",
            bg="#f5a3a2",
            fg="#000000",
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
              fg="#000000",
              font="Goudy_Old_Style 16",
              width=16)
texbox2=Entry(raam2,
              bg="#f5a3a2",
              fg="#000000",
              font="Goudy_Old_Style 16",
              width=16,
              show="*")
valik2=Checkbutton(raam2,
                  image=pilt1,
                  variable=var,
                  onvalue=True,
                  offvalue=False,
                  command=lambda:tehtudvalik(var,valik2,texbox2))
nupp2=Button(raam2,
            text="Registreerima",
            bg="#f5a3a2",
            fg="#000000",
            font="Goudy_Old_Style 16",
            width=16,
            command=reg)
pealkiri3=Label(aken,
               text="Muuda nime ja paroolit",
               bg="#df7ef7",
               fg="#000000",
               cursor="sizing",
               font="Goudy_Old_Style 16",
               justify=CENTER,
               height=3,width=26)
raam3=Frame(aken)
kasutaja_muuda=Entry(raam3,
              bg="#f5a3a2",
              fg="#000000",
              font="Goudy_Old_Style 16",
              width=16)
texbox_muuda=Entry(raam3,
              bg="#f5a3a2",
              fg="#000000",
              font="Goudy_Old_Style 16",
              width=16,
              show="*")
uus_kasutaja=Entry(raam3,
              bg="#f5a3a2",
              fg="#000000",
              font="Goudy_Old_Style 16",
              width=16)
uus_texbox=Entry(raam3,
              bg="#f5a3a2",
              fg="#000000",
              font="Goudy_Old_Style 16",
              width=16,
              show="*")
nupp_muuda=Button(raam3,
            text="Muuda nime ja parool",
            bg="#f5a3a2",
            fg="#000000",
            font="Goudy_Old_Style 16",
            width=16,
            command=muuda)
pealkiri4=Label(raam3,
               text="Vanad andmed",
               bg="#f3f576",
               fg="#000000",
               cursor="sizing",
               font="Goudy_Old_Style 16",
               justify=CENTER,
               height=2,width=16)
raam4=Frame(aken)
pealkiri5=Label(raam3,
               text="Uued andmed",
               bg="#f3f576",
               fg="#000000",
               cursor="sizing",
               font="Goudy_Old_Style 16",
               justify=CENTER,
               height=2,width=16)
raam5=Frame(aken)
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
pealkiri3.pack()
raam4.pack()
raam5.pack()
raam3.pack()
pealkiri4.grid(row=0, columnspan=2)
kasutaja_muuda.grid(row=1, column=0)
texbox_muuda.grid(row=1, column=1)
pealkiri5.grid(row=2, columnspan=2)
uus_kasutaja.grid(row=3, column=0)
uus_texbox.grid(row=3, column=1)
nupp_muuda.grid(row=4, columnspan=2)
aken.mainloop()