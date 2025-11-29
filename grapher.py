# agents/grapher.py

import pandas as pd
import matplotlib.pyplot as plt
import os
import uuid

# Make sure charts are saved to a persistent folder
CHART_DIR = "assets/charts"
os.makedirs(CHART_DIR, exist_ok=True)

def grapher_agent(df: pd.DataFrame) -> list:
    """
    Generates simple charts for the DataFrame:
    - Histograms for numerical columns
    - Bar plots for top categories in object columns
    Saves each chart to /assets/charts/ and returns a list of file paths.
    """
    chart_paths = []

    # Plot histograms for numerical
    for col in df.select_dtypes(include="number").columns:
        try:
            fig, ax = plt.subplots()
            df[col].dropna().plot(kind="hist", ax=ax, bins=20, color='skyblue', edgecolor='black')
            ax.set_title(f"Distribution of {col}")
            ax.set_xlabel(col)

            filename = f"{col}_hist_{uuid.uuid4().hex[:6]}.png"
            path = os.path.join(CHART_DIR, filename)
            fig.savefig(path)
            plt.close(fig)
            chart_paths.append(path)
        except Exception as e:
            print(f"[Grapher] Failed to generate histogram for {col}: {e}")

    # Bar plots for top categories
    for col in df.select_dtypes(include="object").columns:
        try:
            value_counts = df[col].value_counts().head(5)
            fig, ax = plt.subplots()
            value_counts.plot(kind="bar", ax=ax, color='coral')
            ax.set_title(f"Top Categories in {col}")
            ax.set_ylabel("Count")

            filename = f"{col}_bar_{uuid.uuid4().hex[:6]}.png"
            path = os.path.join(CHART_DIR, filename)
            fig.savefig(path)
            plt.close(fig)
            chart_paths.append(path)
        except Exception as e:
            print(f"[Grapher] Failed to generate bar chart for {col}: {e}")

    return chart_paths
