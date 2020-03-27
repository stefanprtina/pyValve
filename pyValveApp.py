import tkinter as tk
import time
import serial
import serial.tools.list_ports
import matplotlib as plt


class pyValveApp(tk.Frame):
    def __init__(self, parent):
        self.parent = parent

        fontBold = "helvetica 14 bold"
        fontRegular = "helvetica 13"

        parent.title("pyValve v0.2")
        self.frame = tk.Frame(self.parent)
        self.labelPodaci = tk.Label(self.parent, text="Osnovni podaci o ventilu",font=fontBold)
        self.labelPodaci.place(x=20, y=10)

        #Lokacija ventila
        self.labelLokacijaVentila = tk.Label(self.parent, text="Lokacija ventila:", bd=1, font=fontRegular)
        self.labelLokacijaVentila.place(x=30, y=55)
        self.entryLokacijaVentila = tk.Entry(self.parent)
        self.entryLokacijaVentila.place(x=150, y=50)

        #Serijski broj
        self.labelSerBrojVentila = tk.Label(self.parent, text="Serijski broj:", bd=1, font=fontRegular)
        self.labelSerBrojVentila.place(x=30, y=85)
        self.entrySerBrojVentila = tk.Entry(self.parent)
        self.entrySerBrojVentila.place(x=150, y=80)

        #Nominalni precnik
        self.labelPrecnikVentila = tk.Label(self.parent, text="Nominalni prečnik:", font=fontRegular)
        self.labelPrecnikVentila.place(x=30, y=115)

        self.entryPrecnikVentila = tk.Entry(self.parent)
        self.entryPrecnikVentila.place(x=150, y=110)

        #Radni medijum
        self.labelRadniMedijVentila = tk.Label(self.parent, text="Radni medijum:", font=fontRegular)
        self.labelRadniMedijVentila.place(x=30, y=145)

        self.entryRadniMedijVentila = tk.Entry(self.parent)
        self.entryRadniMedijVentila.place(x=150, y=140)

        self.labelIspitniPodaci = tk.Label(self.parent, text="Ispitni podaci", font=fontBold)
        self.labelIspitniPodaci.place(x=30, y=180)

        #Pritisak početka otvaranja

        self.labelPritisakOtvaranja = tk.Label(self.parent, text="Pritisak otvaranja:", font=fontRegular)
        self.labelPritisakOtvaranja.place(x=30, y=215)

        self.entryPritisakOtvaranja = tk.Entry(self.parent)
        self.entryPritisakOtvaranja.place(x=150, y=210)

        #Ispitni medijum
        self.labelRadniMedijVentila = tk.Label(self.parent, text="Ispitni medijum:", font=fontRegular)
        self.labelRadniMedijVentila.place(x=30, y=245)

        self.radniMedijVar = tk.StringVar(self.parent)
        self.radniMedijList = ["N2", "Voda"]
        self.radniMedijVar.set(self.radniMedijList[0])

        self.selRadniMedijVentila = tk.OptionMenu(self.parent, self.radniMedijVar, *self.radniMedijList)
        self.selRadniMedijVentila.place(x=150, y=240)

        #Port selection

        #label
        self.labelPortSel = tk.Label(self.parent, text="Interfejs senzora", font=fontBold)
        self.labelPortSel.place(x=420, y=10)

        #Serijski port
        self.labelSerPort = tk.Label(self.parent, text="Izaberi port", font=fontRegular)
        self.labelSerPort.place(x=420, y=40)

        self.serPortVar = tk.StringVar(self.parent)
        self.serPortList = [port.device for port in serialCom.getPorts()]

        if(self.serPortList):
            self.serPortVar.set(self.serPortList[0])
        self.selSerPort = tk.OptionMenu(self.parent, self.serPortVar, *self.serPortList)
        self.selSerPort.place(x=420, y=70)

        self.buttonOpenSerial = tk.Button(text="Konektuj inferfejs", command=lambda: serialCom.open(self, self.parent, self.serPortVar.get()))
        self.buttonOpenSerial.place(x=470, y=100)
        self.frame.pack()

class serialCom():

    def open(self, parent, port):
        self.parent = parent
        ser = serial.Serial(port, 9600, timeout=0.1)
        time.sleep(2)
        if(ser.inWaiting()>0):
            print(ser.readline())
            self.buttonOpenSerial.config(bg="GREEN")
            return True
        return FALSE

    def getPorts():
        portsAvailable = serial.tools.list_ports.comports()
        return portsAvailable

    def greenify(self):
        print("OK")

root = tk.Tk()
root.geometry("800x600")

app = pyValveApp(root)
root.mainloop()
