import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataController:
    def __init__(self, data_path:str) -> None:
        self._path = data_path
        self._scaler = StandardScaler()
        self.raw_df = pd.read_csv(self._path, delimiter=';', on_bad_lines='skip')
        self.df = self.raw_df.dropna().drop_duplicates()
        self.df_columns = list(self.raw_df.columns)
        self._scaler.fit_transform(self.df)
        self.df_norm = self.normalize_df(self.df)

    def normalize_df(self, df:pd.DataFrame) -> pd.DataFrame:
        columns = list(df.columns)
        norm_data = self._scaler.transform(df)
        return pd.DataFrame(norm_data, columns=columns)
    
    def get_X_y_datasets(self, interest_column:str, columns_to_drop:str=None):
        if columns_to_drop: columns_to_drop.append(interest_column)
        else: columns_to_drop = interest_column
        X = self.df_norm.drop(columns=columns_to_drop).reset_index(drop=True)
        y = self.df[interest_column]
        return X, y