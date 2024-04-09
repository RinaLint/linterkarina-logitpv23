from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd

def tehtudvalik(var):
    f=var.get()
    if f:
        texbox.configure(show="")
        valik.configure(image=pilt1)
    else:
        texbox.configure(show="*")
        valik.configure(image=pilt2)
def textpealkirjasse():
    vastus=mb.askquestion("Küsimus","Kas tõesti tahad info kopeerida?")
    if vastus=="yes":
        mb.showwarning("Tähelepanu", "Kohe teisaldatakse info!")
        t=texbox.get()
        pealkiri.configure(text=t)
        texbox.delete(0,END)
    else:
        mb.showinfo("Valik oli tehtud", "Info jääb omal kohal")
        nimi=sd.askstring("Saame tuttuvaks!", "Mis on sinu nimi?") #askinteger() #askfloat()
        pealkiri.configure(text=nimi)
aken=Tk()
aken.geometry("500x500")
aken.title("Akna pealkiri")
aken.configure(bg="#3deff5")
aken.iconbitmap("icon.ico")

pealkiri=Label(aken,
               text="Põhielemendid",
               bg="#df7ef7",
               fg="#000000",
               cursor="sizing",
               font="Goudy_Old_Style 16",
               justify=CENTER,
               height=3,width=26)
raam=Frame(aken)
texbox=Entry(raam,
              bg="#000000",
              fg="#df7ef7",
              font="Goudy_Old_Style 16",
              width=16,
              show="*")
pilt1=PhotoImage(file="eye.png")
pilt2=PhotoImage(file="show.png")
var=BooleanVar() #IntVar(), StringVar()
valik=Checkbutton(raam,
                  image=pilt2, #text="Punkt1"
                  variable=var,
                  onvalue=True,
                  offvalue=False,
                  command=lambda:tehtudvalik(var))
#valik.deselect() 
nupp=Button(raam,
            text="Vajutaja mind",
            bg="#000000",
            fg="#86e2eb",
            font="Goudy_Old_Style 16",
            width=16,
            command=textpealkirjasse)

pealkiri.pack()
raam.pack()
texbox.grid(row=0,column=0) #raami seed
valik.grid(row=0,column=1) #raami seed
nupp.grid(row=0,column=2) #raami seed
aken.mainloop()
