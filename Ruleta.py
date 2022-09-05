import random as rand
from tkinter import *
import tkinter.font as font
Equipos=[["Williams","CadetBlue3"],["Haas","dimgray"],["Alfa Romeo","firebrick4"],["Alpha Tauri","midnight blue"],["Racing Point","orchid2"],["Renault","gold2"],["McLaren","DarkOrange"],["Ferrari","red4"],["Red Bull","medium blue"],["Mercedes","SeaGreen2"]]
Pistas=["Australia","Bahrein","Vietnam","China","Holanda","España","Monaco","Azerbaiyan","Canada","Francia","Austria","GranBretaña","Hungria","Belgica","Italia","Singapur","Rusia","Japon","EE.UU","Mexico","Brasil"]
class inters(object):
    def __init__(self,delta,delay):
        self.delta=delta
        self.delay=delay
    def setDelta(self,delta):
        self.delta=delta
    def setDelay(self,delay):
        self.delay=delay
    def getDelta(self):
        return self.delta
    def getDelay(self):
        return self.delay


def SeleccionarEquipo():
    EquipoSeleccionado=rand.choice(Equipos)
    return EquipoSeleccionado
def SeleccionarPista():
    PistaSeleccionada=rand.choice(Pistas)
    return PistaSeleccionada
window = Tk()

window.title("Ruleta Automatica F1")

window.geometry('800x300')
lblTituloSpace=Label(window,text="",font=("Formula1 Display Wide",20))
lblTituloSpace.grid(columnspan=3,row=0)
lblTitulo=Label(window,text="Ruleta Automatica F1",font=("Formula1 Display Wide",18))
lblTitulo.place(x=0,y=5)
lbl1 = Label(window, text="Equipo Seleccionado 1:",font=("Formula1 Display Bold", 15),fg="black")
lbl1.grid(column=0, row=1)
lbl11 = Label(window, text="",font=("Formula1 Display Regular", 15),fg="Blue")
lbl11.grid(column=2, row=1)
def SeleccionE1():
    tiempos=inters(10,0)
    randi = rand.randint(10,100)
    for i in range(randi):
        EqSelect=SeleccionarEquipo()
        update_text = lambda EqSelect=EqSelect:lbl11.configure(text=EqSelect[0],fg=EqSelect[1])
        window.after(tiempos.getDelay(), update_text)
        tiempos.setDelay(tiempos.getDelay()+tiempos.getDelta()) 
        
    
lbl2 = Label(window, text="Equipo Seleccionado 2:",font=("Formula1 Display Bold", 15),fg="black")
lbl2.grid(column=0, row=2)
lbl22 = Label(window, text="",font=("Formula1 Display Regular", 15),fg="Blue")
lbl22.grid(column=2, row=2)
def SeleccionE2():
    tiempos=inters(10,0)
    randi = rand.randint(10,100)
    for i in range(randi):
        EqSelect=SeleccionarEquipo()
        update_text = lambda EqSelect=EqSelect:lbl22.configure(text=EqSelect[0],fg=EqSelect[1])
        window.after(tiempos.getDelay(), update_text)
        tiempos.setDelay(tiempos.getDelay()+tiempos.getDelta()) 

lbl3 = Label(window, text="Pista Seleccionada:",font=("Formula1 Display Bold", 12))
lbl3.grid(column=1, row=4)
def SeleccionE3():
    tiempos=inters(10,0)
    randi = rand.randint(10,100)
    for i in range(randi):
        Pista=SeleccionarPista()
        update_text = lambda Pista=Pista:lbl3.configure(text="Pista Seleccionada:"+" "+Pista)
        window.after(tiempos.getDelay(), update_text)
        tiempos.setDelay(tiempos.getDelay()+tiempos.getDelta()) 
    
    
def clicked():
    SeleccionE1()
    SeleccionE2()
    SeleccionE3()
myFont = font.Font(family='Formula1 Display Bold' , size=15)
btn = Button(window, text="Generar Resultados",bg="red",fg="white", command=clicked)
btn['font'] = myFont
btn.grid(column=1, row=6)

window.mainloop()

