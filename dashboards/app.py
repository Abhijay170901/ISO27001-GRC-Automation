import streamlit as st
import pandas as pd
import yaml
import os
import subprocess
from datetime import datetime

st.set_page_config(page_title="ISO 27001:2022 GRC Dashboard", layout="wide")

st.title("🛡 ISO 27001:2022 GRC Compliance Dashboard")
st.caption("Monitor control implementation, risk levels, and generate the latest Statement of Applicability (SoA)")

# --- Load data ---
with open("controls/AnnexA.yaml") as f:
    controls = yaml.safe_load(f)["controls"]
controls_df = pd.DataFrame(controls)

risks_df = pd.read_csv("risk_register/risk_register.csv")

# --- Compliance Metrics ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Controls", len(controls_df))
col2.metric("Implemented", len(controls_df[controls_df["status"] == "Implemented"]))
col3.metric("Pending", len(controls_df[controls_df["status"] != "Implemented"]))

# --- Charts ---
st.subheader("📊 Compliance Overview")
status_counts = controls_df["status"].value_counts()
st.bar_chart(status_counts)

st.subheader("⚠️ Risk Overview")
st.dataframe(risks_df)

if "Risk_Level" in risks_df.columns:
    st.bar_chart(risks_df["Risk_Level"].value_counts())

# --- SoA Generator Button ---
st.subheader("📝 Statement of Applicability (SoA)")
if st.button("Generate SoA Report"):
    try:
        subprocess.run(["python", "reports/generate_soa.py"], check=True)
        st.success(f"SoA generated successfully at {datetime.now().strftime('%H:%M:%S')}")
        with open("reports/Statement_of_Applicability.txt") as f:
            st.download_button("⬇️ Download SoA Report", f, file_name="Statement_of_Applicability.txt")
    except Exception as e:
        st.error(f"Error generating report: {e}")
