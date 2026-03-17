def save_data(df, path):
    df.to_csv(path, index=False)
def create_summary(df):
    summary = df.groupby("order_date").agg({
        "revenue": "sum",
        "quantity": "sum"
    }).reset_index()
    return summary