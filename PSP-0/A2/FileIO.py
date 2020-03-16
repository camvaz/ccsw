import pandas as pd
import sys
from pandas import DataFrame

# sys.path.insert(1, "./models")
from models.Set import Set

class FileIO:
    namespace: str
    file: str

    def __init__(self, _namespace: str):
        super().__init__()
        self.namespace = _namespace
    
    def read(self, fileName: str) -> DataFrame:
        return pd.read_csv(f"{self.namespace}/{fileName}")
    
    def write(self, fileName: str, set: Set) -> DataFrame:
        return set.returnSet().to_csv(f"{self.namespace}/{fileName}",index=False);
