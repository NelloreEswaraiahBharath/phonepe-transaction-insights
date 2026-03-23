import pandas as pd

def load_data():
    df = pd.read_csv("csv/aggregated_transaction.csv")
    return df
