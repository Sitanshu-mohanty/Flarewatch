import streamlit as st
import streamlit.components.v1 as components

# Page settings
st.set_page_config(page_title="Flarewatch Dashboard", layout="wide")

# Flarewatch title
st.markdown("""
    <h1 style='text-align: center; color: red;'>🚨 Flarewatch: Satellite Threat Detection System</h1>
    <h4 style='text-align: center;'>Monitoring solar flares & satellites using space weather data</h4>
""", unsafe_allow_html=True)

st.divider()

# 🔆 Animated Sun
st.markdown("""
    <div style='text-align: center;'>
        <img src="https://upload.wikimedia.org/wikipedia/commons/2/28/Sun_rotate.gif" width="200"/>
    </div>
""", unsafe_allow_html=True)

st.divider()

# 🛰️ Earth Orbit 3D Viewer (NASA Eyes)
st.markdown("## 🪐 Live Earth Orbit View (NASA Eyes 3D)")
components.html("""
    <iframe src="https://eyes.nasa.gov/apps/orrery/#/home" width="100%" height="600" frameborder="0" allowfullscreen></iframe>
""", height=600)

st.divider()

# Danger Satellites List
danger_satellites = ["GOES-16", "NOAA-21", "Sentinel-6"]
st.markdown("### 🔴 Satellites in Danger:")
for sat in danger_satellites:
    st.markdown(f"<p style='color:red;'>🛰️ {sat}</p>", unsafe_allow_html=True)
