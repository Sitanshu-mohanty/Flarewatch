import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("☀️ FlareWatch: Solar Flare Activity Dashboard")
st.markdown("Visualizing recent solar flare activity and its intensity by region.")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("flare_data_sample.csv")

df = load_data()

# Show raw data
if st.checkbox("Show raw data"):
    st.write(df)

# Flare class distribution
flare_counts = df['flare_class'].value_counts().reset_index()
flare_counts.columns = ['flare_class', 'count']

fig1 = px.bar(flare_counts, x='flare_class', y='count',
              title='Flare Class Distribution',
              color='flare_class',
              color_discrete_sequence=px.colors.qualitative.Vivid)
st.plotly_chart(fig1)

# Intensity over time
df['event_date'] = pd.to_datetime(df['event_date'])
fig2 = px.line(df, x='event_date', y='intensity', color='flare_class',
               title='Solar Flare Intensity Over Time')
st.plotly_chart(fig2)