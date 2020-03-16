from A2.FileIO import FileIO
from A2.models.Set import Set
from A1.LinkedList import LinkedList
from A1.stats import Stats
from tkinter import Tk
from tkinter.filedialog import askopenfilename

class A3:
    def __init__(self):
        super().__init__()
        Tk().withdraw() 
        self.io = FileIO()
        self.conjunto = Set()
        # Dibujillo de bienvenida
        print("""\
                _
                | |
                | |===( )   //////
                |_|   |||  | o o|
                        |||( c  )                  ____
                        ||| \= /                  ||   \_
                        ||||||                   ||     |
                        ||||||                ...||__/|-"
                        ||||||             __|________|__
                            |||             |______________|
                            |||             || ||      || ||
                            |||             || ||      || ||
    ------------------------|||-------------||-||------||-||-------
                            |__>            || ||      || ||
        """)

        print("PSP A2\n\n\n".center(53))
        print("Read: r\nWrite: w\nPruebas: t")
        self.opc = input("> ")
        
        if(self.opc == "r"):
            self.filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
            res = self.io.read(self.filename)
            cleanarray = [i[0] for i in res.to_numpy()]
            self.stat = Stats(cleanarray)
            print(f"Std Deviation: {self.stat.standardDeviation()}")

        elif(self.opc == "w"):
            # Escritura
            items: int
            # Leemos cantidad a escribir
            items = int(input("Introduzca el numero de datos: "))
            print("Ingrese datos uno por uno")
            while(items > 0):
                # Ciclo para introducir uno por uno
                self.conjunto.add(input(">"))
                items -= 1

            self.filename=input("Introduzca el nombre del archivo a escribir: ") 
            res = self.io.write(f"{self.filename}.csv", self.conjunto)
            cleanarray = [i[0] for i in res.to_numpy()]
            self.stat = Stats(cleanarray)
            print(f"Std Deviation: {self.stat.standardDeviation()}")

        elif(self.opc == "t"):
            files = ["test1", "test2", "test3"]
            for i in files:
                res = self.io.read(f"./csvtests/{i}.csv")
                cleanarray = [i[0] for i in res.to_numpy()]
                self.stat = Stats(cleanarray)
                print(f"Std Deviation: {self.stat.standardDeviation()}")

        else:
            print("Opcion invalida. Ejecute de nuevo")

A3()