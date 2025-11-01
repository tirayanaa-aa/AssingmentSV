import streamlit as st
import pandas as pd
import plotly.express as px

# --- Data Loading (Placeholder, should ideally be imported from a shared utils file) ---
DATA_URL = 'https://raw.githubusercontent.com/tirayanaa-aa/AssingmentSV/refs/heads/main/processed_data.csv'

@st.cache_data
def load_data(url):
    try:
        df = pd.read_csv(url)
        # Essential cleaning for plotting
        for col in ['Overall']:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        df.dropna(subset=['Overall'], inplace=True)
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

df = load_data(DATA_URL)

st.title("🌍 Objective 2: Demographic and Socioeconomic Background")
st.markdown("---")

if not df.empty:
    st.subheader("A. Overall CGPA Distribution by Hometown (Violin Plot)")
    # This is the violin plot you previously requested
    if 'Hometown' in df.columns:
        fig_violin = px.violin(
            df,
            x='Hometown',
            y='Overall',
            box=True,
            title='Overall CGPA Distribution by Hometown',
            template='plotly_white'
        )
        st.plotly_chart(fig_violin, use_container_width=True)

    # Placeholder for other Objective 2 plots (Grouped Bar, Box Plot)
    st.info("You can add the Grouped Bar Chart by Department/Gender and the Box Plot by Income here.")
else:
    st.warning("Data could not be loaded for analysis.")

