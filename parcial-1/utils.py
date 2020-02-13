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
