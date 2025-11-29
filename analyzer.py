# agents/analyzer.py

import pandas as pd

def analyzer_agent(df: pd.DataFrame) -> str:
    """
    Analyzes the DataFrame and returns a textual summary of:
    - Column info
    - Null values
    - Descriptive statistics
    - Data types
    """
    lines = []

    lines.append("🔍 Data Summary Report\n")

    # Basic structure
    lines.append("🧱 Columns and Types:")
    lines.append(df.dtypes.to_string())
    lines.append("")

    # Missing values
    nulls = df.isnull().sum()
    if nulls.sum() == 0:
        lines.append("✅ No missing values detected.")
    else:
        lines.append("⚠️ Missing Values:")
        lines.append(nulls[nulls > 0].to_string())
    lines.append("")

    # Descriptive statistics (numerical)
    if df.select_dtypes(include='number').shape[1] > 0:
        stats = df.describe().T
        lines.append("📊 Descriptive Stats (Numerical Columns):")
        lines.append(stats[['mean', 'std', 'min', 'max']].to_string())
    else:
        lines.append("ℹ️ No numerical columns found.")

    return "\n".join(lines)
