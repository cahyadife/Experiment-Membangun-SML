import pandas as pd
import os

RAW_PATH = os.path.join('..', 'namadataset_raw', 'indonesia_gdp_raw.csv')
OUTPUT_DIR = 'namadataset_preprocessing'
OUTPUT_PATH = os.path.join(OUTPUT_DIR, 'indonesia_gdp_preprocessed.csv')

if __name__ == '__main__':
    df = pd.read_csv(RAW_PATH)
    # Contoh preprocessing sederhana: hapus baris duplikat dan NA
    df = df.drop_duplicates()
    df = df.dropna()

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print(f'Preprocessed data saved to {OUTPUT_PATH}')
