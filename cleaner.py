# agents/cleaner.py

import pandas as pd
import io

def cleaner_agent(file_bytes: bytes) -> pd.DataFrame:
    """
    Cleans and loads the uploaded CSV into a pandas DataFrame.
    Handles common issues like encoding and missing headers.
    """
    try:
        df = pd.read_csv(io.BytesIO(file_bytes))  # ✅ use byte stream

        df.columns = [col.strip() for col in df.columns]
        df.dropna(how='all', inplace=True)
        df.fillna("-", inplace=True)

        return df

    except Exception as e:
        raise ValueError(f"CSV Cleaning Failed: {e}")

