import pandas as pd
import os
import requests

URL = 'https://api.worldbank.org/v2/country/IDN/indicator/NY.GDP.MKTP.CD?format=json&per_page=100'
RAW_PATH = os.path.join('..', 'namadataset_raw', 'indonesia_gdp_raw.csv')
OUTPUT_DIR = 'namadataset_preprocessing'
OUTPUT_PATH = os.path.join(OUTPUT_DIR, 'indonesia_gdp_preprocessed.csv')

if __name__ == '__main__':
    # Try fetching from API first
    try:
        print("Fetching data from World Bank API...")
        response = requests.get(URL, timeout=10)
        data = response.json()[1]
        df = pd.DataFrame(data)
        df = df[['date', 'value']].rename(columns={'date': 'Year', 'value': 'GDP_USD'})
        df['Year'] = df['Year'].astype(int)
        print("Successfully fetched from API.")
    except Exception as e:
        print(f"API fetch failed ({e}). Falling back to local raw file...")
        # Fallback to local raw csv
        df = pd.read_csv(RAW_PATH)
        df = df[['Year', 'GDP_USD']]

    # Preprocessing
    df = df.dropna().sort_values('Year').reset_index(drop=True)
    df['GDP_Growth_Rate'] = df['GDP_USD'].pct_change() * 100
    df['GDP_Growth_Rate'] = df['GDP_Growth_Rate'].fillna(0)

    # Save output
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Preprocessed data successfully saved to {OUTPUT_PATH}")
