# Importamos pandas para la lectura del csv
import pandas as pd
# Importamos DataFrame para usar tipado
from pandas import DataFrame
# Importamos nuestra clase set
from models.Set import Set

class FileIO:
    namespace: str
    file: str

    def __init__(self, _namespace: str):
        # Constructor que recibe el namespace donde vamos a almacenar los csv
        super().__init__()
        self.namespace = _namespace
    
    def read(self, fileName: str) -> DataFrame:
        # Leemos csvs por medio de pandas
        return pd.read_csv(f"{self.namespace}/{fileName}")
    
    def write(self, fileName: str, set: Set) -> DataFrame:
        # Escribimos csvs por medio de pandas, ocupamos composicion para hacer uso de nuesta clase Set
        return set.returnSet().to_csv(f"{self.namespace}/{fileName}",index=False)
