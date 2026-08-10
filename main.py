from loader import load_data
from cleaner import clean_data
from engineer import feature_engineering
from validator import validate_data
from storage import save_data

def main():
    print("Loading data...")
    df = load_data()
    print("Cleaning data...")
    df = clean_data(df)
    print("Feature engineering...")
    df = feature_engineering(df)
    print("Validating...")
    validate_data(df)
    print("Saving to storage...")
    save_data(df)
    print("Pipeline completed successfully!")

if __name__ == "__main__":
    main()
