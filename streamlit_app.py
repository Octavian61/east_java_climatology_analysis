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
  return pd.read_csv("climatology_daily_2015_2025.csv",
  index_col = "Date",
  parse_date = True)

df = load_data()
df.index = pd.to_datetime(df.index)
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
with col2:
  st.metric(label = "Total Curah Hujan", value = f"{df_filtered['PRECTOTCORR'].sum():.1f} mm")
with col3:
  st.metric(label = "Rata-rata Kelembaban", value = f"{df_filtered['RH2M'].mean():.2f} %")

st.subheader("Visualisasi Tren Jangka Panjang")
tab1, tab2 = st.tabs(["Variabilitas Suhu"], ["Analisis Hujan Besar"])

with tab1:
  df_monthly = df_filtered['T2M'].resample('RE').mean().to_frame(name = "T2M_mean")
