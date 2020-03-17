from FileIO import FileIO
from models.Set import Set
from tkinter import Tk
from tkinter.filedialog import askopenfilename

if __name__ == "__main__":
    # Declaring variables
    opc: str
    io: FileIO = FileIO("./data")
    conjunto: Set = Set()
    fileName: str

    # Dibujillo de bienvenida
    print("""\
              _
             | |
             | |===( )   //////
             |_|   |||  | o o|
                    ||| ( c  )                  ____
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
    opc = input("> ")

    if(opc == "r"):
        fileName = askopenfilename()
        # Si el usuario pilde leer, FileIO realiza la lectura por medio de pandas
        print(io.read(f"./reads/{fileName}.csv"))
    
    if(opc == "w"):
        # Escritura
        fileName = input("Introduzca el nombre del archivo: ")
        items: int
        # Leemos cantidad a escribir
        items = int(input("introduzca el numero de datos: "))
        while(items > 0):
            # Ciclo para introducir uno por uno
            conjunto.add(input())
            items -= 1
        
        io.write(f"./writes/{fileName}.csv", conjunto)
        print(io.read(f"./writes/{fileName}.csv"))

    if(opc == "t"):
        files = ["test1", "test2", "test3"]
        for i in files:
            res = io.read(f"../csvtests/{i}.csv")
            print(res)