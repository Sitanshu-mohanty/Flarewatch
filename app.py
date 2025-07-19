import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(page_title="Flarewatch Dashboard", layout="wide")

# 🔥 Solar Flare Animation (from Wikipedia)
st.markdown(
    """
    <div style='display: flex; justify-content: center; margin-bottom: 20px;'>
        <video width="600" autoplay loop muted>
            <source src="https://upload.wikimedia.org/wikipedia/commons/transcoded/5/5f/Solar_flare_from_June_7%2C_2011.ogv/Solar_flare_from_June_7%2C_2011.ogv.360p.webm" type="video/webm">
            Your browser does not support the video tag.
        </video>
    </div>
    """,
    unsafe_allow_html=True
)

# 🌞 Title & Subtitle
st.markdown("<h1 style='text-align: center; color: red;'>⚡ Flarewatch: Satellite Threat Detection System</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Real-time dashboard to monitor solar flares and satellite safety using space weather data.</h4>", unsafe_allow_html=True)

st.divider()

# 🌍 NASA 3D Earth Orbit Live View
st.markdown("## 🌐 Live Earth Orbit View (NASA 3D)")
components.html(
    """
    <iframe src="https://eyes.nasa.gov/apps/orrery/#/home"
            width="100%" height="600" frameborder="0" allowfullscreen></iframe>
    """,
    height=600
)
