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
  df = pd.read_csv("climatology_daily_2015_2025.csv",
  index_col = "Date",
  pase_date = True)

df = load_data()
df.replace(-999, pd.NA, inplace=True)

tahun_pilihan = st.sidebar.slider(
  "Pilih Rentang Tahun", 
  int(df.index.year.min()), 
  int(df.index.year.max()), 
  (2020, 2025)
)

df_filtered = df[(df.index.year >= tahun_pilihan[0]) & (df.index.year <= tahun_pilihan[1])]

col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label = "Rata-rata Suhu", value = f"{df_filtered['T2M'].mean():.2f} °C")
