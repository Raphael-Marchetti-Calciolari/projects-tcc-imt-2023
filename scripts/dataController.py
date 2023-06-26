import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataController:
    def __init__(self, data_path:str) -> None:
        self._path = data_path
        self._scaler = StandardScaler()
        self.raw_df = pd.read_csv(self._path, delimiter=';', on_bad_lines='skip')
        self.df = self.raw_df.dropna().drop_duplicates()
        self.df_columns = list(self.raw_df.columns)
        self.df_norm = self.normalize_df(self.df)

    def normalize_df(self, df:pd.DataFrame) -> pd.DataFrame:
        columns = list(df.columns)
        norm_data = self._scaler.fit_transform(df)
        return pd.DataFrame(norm_data, columns=columns)