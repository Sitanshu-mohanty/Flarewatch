import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(page_title="Flarewatch", page_icon="🌍", layout="wide")

st.markdown("<h1 style='text-align: center; color: #FF5733;'>🚨 Flarewatch: Satellite Threat Detection System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Real-time risk dashboard to monitor solar flares and satellite safety using space weather data.</p>", unsafe_allow_html=True)
st.markdown("---")

st.sidebar.title("📁 Data Options")
data_source = st.sidebar.radio("Choose data source:", ["Upload CSV", "Use Sample Data"])

if data_source == "Upload CSV":
    uploaded_file = st.sidebar.file_uploader("Upload your space data CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("✅ Your data has been loaded.")
    else:
        st.warning("⚠️ Upload a CSV file to proceed.")
        st.stop()
else:
    df = pd.DataFrame({
        "Timestamp": pd.date_range(start="2025-07-01", periods=24, freq="H"),
        "Solar Flare Index": [0.3, 0.2, 0.5, 1.2, 1.8, 2.0, 1.7, 0.8, 0.5, 0.3, 0.2, 0.4,
                              0.9, 1.1, 1.6, 2.4, 3.1, 2.7, 1.9, 1.0, 0.7, 0.4, 0.3, 0.1]
    })

st.subheader("🛰️ Satellite Risk Index Data")
st.dataframe(df, use_container_width=True)

st.subheader("⚠️ Flare Activity Over Time")
st.line_chart(df.set_index("Timestamp"))

flare_threshold = 2.5
max_flare = df["Solar Flare Index"].max()

if max_flare >= flare_threshold:
    st.error(f"🚨 HIGH RISK: Solar flare index peaked at {max_flare}!")
else:
    st.success(f"✅ SAFE: No severe flares detected (Max Index: {max_flare})")

st.markdown("---")
st.caption("🔬 Built by Sitanshu Sekhar Mohanty | Prototype version | NASA API Integration Coming Soon.")
