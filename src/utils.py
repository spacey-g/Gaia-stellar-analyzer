import pandas as pd

def save_df(df, path):
    """Save DataFrame as CSV in the data folder."""
    df.to_csv(path, index=False)
    print(f"Saved: {path}")

def preview_df(df, n=5):
    """Preview top rows of DataFrame."""
    print(df.head(n))

