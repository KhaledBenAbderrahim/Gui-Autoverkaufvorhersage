

#Dieses Framework bietet Python-Benutzern eine einfache Möglichkeit, GUI-Elemente mit den im Tk-Toolkit enthaltenen Widgets zu erstellen
from tkinter import *
from tkinter.ttk import Combobox

#Das Pickle-Modul kann ein komplexes Objekt in einen Bytestrom umwandeln und es kann den Bytestrom in ein Objekt mit der gleichen internen Struktur umwandeln.
import pickle

#funktionen importieren von dommy datn and one hote encording daten
from HelperFunction import *
#
#NumPy bietet umfassende mathematische Funktionen, Zufallszahlengeneratoren, lineare Algebra-Routinen, Fourier-Transformationen und mehr
import numpy as np
#Python warning desaktivieren
import warnings
warnings.filterwarnings('ignore')

#leer Gui oberfläche erstellen
root = Tk()


root.geometry("500x700") #Gui oberfläche dimension
root.configure(background="light green") #Gui oberfläche farbe

#-------------------------title----------------------------------------

Label(root,text="Gui Autoverkaufvorhersage",
        font=('Helvetica',15,'bold'),bg="light green",
        relief="solid").pack()

Label(root,text="application version 1.1",relief="solid",
        bg="light green").pack(side=BOTTOM)

Label(root,text="=====================",
        bg="light green").pack(fill='both')
#----------------------------------eingabe label ----------------------------------

Label(root,text="Herstellung Jahr",
        font=('Helvetica',10,'bold'),bg="light green",relief="solid",width=25).place(x=40,y=80)

Label(root,text="Kilometerstand in km",
        font=('Helvetica',10,'bold'),bg="light green",relief="solid",width=25).place(x=40,y=120)

Label(root,text="Kraftstof",
        font=('Helvetica',10,'bold'),bg="light green",relief="solid",width=25).place(x=40,y=160)

Label(root,text="Verkaufer type",
        font=('Helvetica',10,'bold'),bg="light green",relief="solid",width=25).place(x=40,y=200)

Label(root,text="Fahrzeuggetriebe",
        font=('Helvetica',10,'bold'),bg="light green",relief="solid",width=25).place(x=40,y=240)

Label(root,text="Autositz",
        font=('Helvetica',10,'bold'),bg="light green",relief="solid",width=25).place(x=40,y=280)

Label(root,text=" Drehmoment in Nm",
        font=('Helvetica',10,'bold'),bg="light green",relief="solid",width=25).place(x=40,y=320)

Label(root,text="Laufleistung in km",
        font=('Helvetica',10,'bold'),bg="light green",relief="solid",width=25).place(x=40,y=360)

Label(root,text="motor",
        font=('Helvetica',10,'bold'),bg="light green",relief="solid",width=25).place(x=40,y=400)

Label(root,text="Auto's Maximale Leistung",
        font=('Helvetica',10,'bold'),bg="light green",relief="solid",width=25).place(x=40,y=440)

Label(root,text="Auto's Ersbesitzer",
        font=('Helvetica',10,'bold'),bg="light green",relief="solid",width=25).place(x=40,y=480)

Label(root,text="Predicted ergebnis ist",
        font=('Helvetica',10,'bold'),bg="light green",relief="solid",width=25).place(x=40,y=520)

#-----------------------Date input eingabe--------------------------------------------------------------------------------

# Eingabe Herstellung jahr
h_jahr = Entry(root,text=StringVar(),width=25)
h_jahr.place(x=300,y=80)

# Eingabe von der km stand des Auto
k_stand = Entry(root,text=StringVar(),width=25)
k_stand.place(x=300,y=120)

#  Kraftstoff type wählen
kr_stoff = Combobox(root,value=["Petrol","Diesel","CNG/LPG"],width=22)
kr_stoff.current(1)
kr_stoff.place(x=300,y=160)

# Eingabe Verkaufertyp
v_type = Combobox(root,value=["Individual","Dealer","Trusmark Dealer"],width=22)
v_type.current(1)
v_type.place(x=300,y=200)

transmission = Combobox(root,value=["Manual","Automatic"],width=22)
transmission.current(1)
transmission.place(x=300,y=240)

seats = Combobox(root,value=["1","2","3","4","5","6","7","8","9","10"],width=22)
seats.current(1)
seats.place(x=300,y=280)

torque_rpm = Entry(root,text=StringVar(),width=25)
torque_rpm.place(x=300,y=320)

mil_kmpl = Entry(root,text=StringVar(),width=25)
mil_kmpl.place(x=300,y=360)

engine_cc = Entry(root,text=StringVar(),width=25)
engine_cc.place(x=300,y=400)

max_power = Entry(root,text=StringVar(),width=25)
max_power.place(x=300,y=440)

owner = Combobox(root,value=["First Owner","Second Owner","Third Owner","Fourth & Above Owner","Test Drive Car"],width=22,textvariable=StringVar())
owner.current(1)
owner.place(x=300,y=480)

def model():
        try:
                year = int(h_jahr.get())
                km_driven = int(k_stand.get())
                fuel = ref3(kr_stoff.get())
                seller_type = ref2(v_type.get())
                transmission_ma = ref1(transmission.get())
                seats_n = int(seats.get())
                torque_rpm_n = int(torque_rpm.get())
                mil_kmpl_n = int(mil_kmpl.get())
                engine_cc_n = int(engine_cc.get())
                max_power_n = int(max_power.get())

                np_array1 = np.array([year,km_driven,fuel,seller_type,transmission_ma,seats_n,torque_rpm_n,mil_kmpl_n,engine_cc_n,max_power_n])
                np_array2= np.array(Helper(owner.get()))


                filename = 'Models/CarSelling.pickle'
                loaded_model = pickle.load(open(filename, 'rb'))
                to_predict = loaded_model.predict(np.concatenate((np_array1,np_array2)).reshape(1,-1))

                print(to_predict)
                Label(root,text=str(to_predict[0])+"$",font=('Helvetica',10,'bold'),bg="light green",relief="solid",width=20).place(x=300,y=520)
        except:
                pass

        return 

button = Button(root,text="predict",width=25,command=model)
button.place(x=40,y=560)

button = Button(root,text="Termination",width=25,command=root.destroy)
button.place(x=300,y=560)

#-------------------------------------------------------------------------------------------
















root.resizable(0,0)
root.mainloop()