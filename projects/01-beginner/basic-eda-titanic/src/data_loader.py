import pandas as pd
from pathlib import Path
import requests


class TitanicDataLoader:
    def __init__(self, data_path="data/raw/titanic.csv"):
        self.data_path = Path(data_path)
        self.data_path.parent.mkdir(parents=True, exist_ok=True)

    def load_data(self) -> pd.DataFrame:
        if not self.data_path.exists():
            url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
            r = requests.get(url)
            self.data_path.write_bytes(r.content)
        df = pd.read_csv(self.data_path)
        for c in ["Pclass", "Sex", "Embarked"]:
            if c in df.columns:
                df[c] = df[c].astype("category")
        return df
