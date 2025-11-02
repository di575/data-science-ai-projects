import pandas as pd


class EDAnalyzer:
    def basic_overview(self, df: pd.DataFrame):
        print("Shape:", df.shape)
        print("Columns:", list(df.columns))
        print(df.describe(include="all").T.head())

    def missing_value_analysis(self, df: pd.DataFrame):
        mv = df.isna().sum().sort_values(ascending=False)
        print("Missing values:\n", mv.head(10))
