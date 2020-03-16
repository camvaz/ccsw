from A2.FileIO import FileIO
from A2.models.Set import Set
from A1.LinkedList import LinkedList
from A1.stats import Stats

class A3:
    def __init__(self):
        super().__init__()
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
        self.fileDirectory = input("Introduzca el directorio donde quiera almacenar los archivos: ")
        self.io = FileIO(self.fileDirectory)

        print("Read: r\nWrite: w\nPruebas: t")
        self.opc = input("> ")

        if(self.opc == "r"):
            # Si el usuario pilde leer, FileIO realiza la lectura por medio de pandas

            print(self.io.read(f"reads/{input('introduzca el nombre del archivo')}.csv"))
        
        if(self.opc == "w"):
            # Escritura
            self.items: int
            # Leemos cantidad a escribir
            self.items = int(input("introduzca el numero de datos: "))
            while(self.items > 0):
                # Ciclo para introducir uno por uno
                conjunto.add(input())
                items -= 1
            
            io.write(f"writes/{fileName}.csv", conjunto)
            print(io.read(f"writes/{fileName}.csv"))

        if(self.opc == "t"):
            # Pruebas might use unittest later
            io.write(f"writes/test.csv", Set([160,591,114,229,230,270,128,1657,624,1503]))
            print(io.read(f"writes/test.csv"))