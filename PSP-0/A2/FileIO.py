import pandas as pd
from pandas import DataFrame
from models.Set import Set

class FileIO:
    namespace: str
    file: str

    def __init__(self, _namespace: str):
        super().__init__()
        self.namespace = _namespace
    
    def read(self, fileName: str) -> DataFrame:
        self.data = pd.read_csv(f"{self.namespace}/{fileName}")
    
    def write(self, fileName: str) -> DataFrame:
        self.data = pd.read_csv(f"{self.namespace}/{fileName}")
