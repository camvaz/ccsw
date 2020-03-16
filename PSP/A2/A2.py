from FileIO import FileIO
from models.Set import Set

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
    fileName = input("Introduzca el nombre del archivo: ")
    print("Read: r\nWrite: w\nPruebas: t")
    opc = input("> ")

    if(opc == "r"):
        # Si el usuario pilde leer, FileIO realiza la lectura por medio de pandas
        print(io.read(f"reads/{fileName}.csv"))
    
    if(opc == "w"):
        # Escritura
        items: int
        # Leemos cantidad a escribir
        items = int(input("introduzca el numero de datos: "))
        while(items > 0):
            # Ciclo para introducir uno por uno
            conjunto.add(input())
            items -= 1
        
        io.write(f"writes/{fileName}.csv", conjunto)
        print(io.read(f"writes/{fileName}.csv"))

    if(opc == "t"):
        # Pruebas might use unittest later
        io.write(f"writes/test.csv", Set([160,591,114,229,230,270,128,1657,624,1503]))
        print(io.read(f"writes/test.csv"))