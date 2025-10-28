import streamlit as st
import pandas as pd
import yaml

st.set_page_config(page_title="ISO 27001 GRC Dashboard", layout="wide")
st.title("🛡 ISO 27001:2022 GRC Compliance Dashboard")

with open("controls/AnnexA.yaml") as f:
    data = yaml.safe_load(f)

controls = pd.DataFrame(data["controls"])
st.metric("Total Controls", len(controls))
st.metric("Implemented", len(controls[controls["status"] == "Implemented"]))
st.metric("Pending", len(controls[controls["status"] != "Implemented"]))

st.subheader("Control Breakdown")
st.dataframe(controls)
