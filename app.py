# app.py

import streamlit as st
import pandas as pd
import io
from workflows.graph import run_csv_analysis

st.set_page_config(page_title="CSV Insight Agent", layout="wide")
st.title("📊 CSV Insight Agent – Your Autonomous Data Analyst")

uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    csv_bytes = uploaded_file.read()  # ✅ read file as bytes

    try:
        df = pd.read_csv(io.BytesIO(csv_bytes))  # ✅ preview
        st.subheader("🔍 Preview of Uploaded Data")
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"⚠️ Failed to read CSV: {e}")

    if st.button("🚀 Run ADA Agents"):
        with st.spinner("Analyzing..."):
            try:
                report = run_csv_analysis(csv_bytes)  # ✅ pass to graph

                st.subheader("📄 Executive Summary")
                st.write(report.get("summary", "⚠️ No summary returned."))

                if "docx" in report:
                    st.download_button(
                        label="📥 Download Report (.docx)",
                        data=report["docx"].getvalue(),
                        file_name="CSV_Insights_Report.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
                else:
                    st.warning("⚠️ DOCX report was not generated.")

            except Exception as e:
                st.error(f"❌ Something went wrong: {e}")
