import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="FlareWatch", layout="wide")

st.title("☀️ FlareWatch")
st.subheader("Track Solar Flares. Assess Satellite Risk.")

# Load Data
flare_data = pd.read_csv("data/flare_data.csv")
sat_data = pd.read_csv("data/satellite_data.csv")

# Map of flares
st.markdown("### 🌍 Affected Earth Regions from Recent Flares")
fig = px.scatter_geo(
    flare_data,
    lat="latitude",
    lon="longitude",
    color="intensity",
    size="impact_radius",
    projection="natural earth",
    title="Solar Flare Impact Zones",
)
st.plotly_chart(fig, use_container_width=True)

# Satellite Table
st.markdown("### 🛰️ Satellites at Potential Risk")
st.dataframe(sat_data)
