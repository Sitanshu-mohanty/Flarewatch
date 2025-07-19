import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Flarewatch", layout="wide")

# Sun animation + title
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://media.giphy.com/media/5PhsM62X1Y4MVbmWHj/giphy.gif" width="400">
        <h1 style="color: red;">Flarewatch</h1>
        <p><b>Tracking solar flare risks for satellite safety</b></p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# Section title
st.subheader("🛰️ Real-time Satellite Orbit Map")

# Orbiting Globe
components.html(
    """
    <!DOCTYPE html>
    <html>
    <head>
      <style>
        html, body {
          margin: 0;
          height: 100%;
          overflow: hidden;
        }
      </style>
    </head>
    <body>
    <div id="globeViz"></div>
    <script src="https://unpkg.com/three@0.121.1/build/three.min.js"></script>
    <script src="https://unpkg.com/globe.gl"></script>
    <script>
      const world = Globe()
        (document.getElementById('globeViz'))
        .globeImageUrl('//unpkg.com/three-globe/example/img/earth-dark.jpg')
        .backgroundColor('#000000')
        .showAtmosphere(true)
        .atmosphereColor('lightskyblue')
        .atmosphereAltitude(0.25)
        .pointOfView({ lat: 20, lng: 80, altitude: 2.5 }, 0);

      world
        .ringsData([
          { lat: 10, lng: 80, maxR: 2, propagationSpeed: 1, repeatPeriod: 1000 },
          { lat: 35, lng: -120, maxR: 2, propagationSpeed: 1, repeatPeriod: 1500 },
          { lat: -10, lng: 60, maxR: 2, propagationSpeed: 1, repeatPeriod: 1300 }
        ])
        .ringColor(() => ['red', 'crimson', 'darkred']);
    </script>
    </body>
    </html>
    """,
    height=600
)
