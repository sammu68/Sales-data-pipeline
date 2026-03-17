import pandas as pd
def transform_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    df["quantity"] = df["quantity"].astype(int)
    df["price"] = df["price"].astype(float)
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["revenue"] = df["quantity"] * df["price"]
    return df