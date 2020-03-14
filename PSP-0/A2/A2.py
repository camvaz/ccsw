import sys
from FileIO import FileIO
from Set import Set

if __name__ == "__main__":
    opc: str
    io: FileIO = FileIO("./data")
    conjunto: Set = Set()
    fileName: str

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

    fileName = input("Introduzca el nombre del archivo: ")
    print("PSP A2\n\n\n".center(53))
    print("Read: r\nWrite: w\nPruevas: t")
    opc = input("> ")

    if(opc == "r"):
        print(io.read(f"reads/{fileName}.csv"))
    
    if(opc == "w"):
        items: int
        items = int(input("introduzca el numero de datos: "))
        while(items > 0):
            conjunto.add(input())
            items -= 1
        
        io.write(f"writes/{fileName}.csv", conjunto)
        print(io.read(f"writes/{fileName}.csv"))

    if(opc == "t"):
        io.write(f"writes/test.csv", Set([160,591,114,229,230,270,128,1657,624,1503]))
        print(io.read(f"writes/test.csv"))