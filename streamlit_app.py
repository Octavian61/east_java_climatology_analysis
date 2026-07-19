import streamlit as st
import pandas as pd

st.set_page_config(
  page_title = "East Java Climatology Analysis",
  layout = "wide"
)

st.title("East Java Climatology Analysis Dashboard")
st.markdown("Analisis klimatologi kawasan Jawa Timur dari data NASA dalam rentang 2015-2025")
st.write("---")

st.sidebar.header("Pemilihan Parameter")
@st.cache_data
def load_data():
  df = pd.read_csv("climatology_daily_2015_2025.csv")
  return df

