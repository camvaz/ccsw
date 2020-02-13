class Utils:

    @staticmethod
    def getIntsFromList(lista:list):
        numbers = []

        # Obtenemos datos    int:
        for i in lista:
            try:
                numbers.append(int(i))
            except ValueError:
                pass

        return numbers


    @staticmethod
    def getStringsFromList(lista:list):
        strings = []

        # Obtenemos datos    int:
        for i in lista:
            try:
                int(i)
            except ValueError:
                strings.append(i)

        return strings  