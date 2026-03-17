from extract import extract_data
from transform import transform_data
from load import save_data, create_summary
def main():
    raw_file = "data/raw/orders.csv"
    clean_file = "data/processed/cleaned.csv"
    summary_file = "data/processed/summary.csv"
    df = extract_data(raw_file)
    df_clean = transform_data(df)
    summary = create_summary(df_clean)
    save_data(df_clean, clean_file)
    save_data(summary, summary_file)
    print("Pipeline executed successfully!")
if __name__ == "__main__":
    main()