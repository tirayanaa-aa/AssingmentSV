import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Data Loading (Must be repeated on every page or factored out to a shared file) ---
DATA_URL = 'https://raw.githubusercontent.com/tirayanaa-aa/AssingmentSV/refs/heads/main/processed_data.csv'

@st.cache_data
def load_data(url):
    try:
        df = pd.read_csv(url)
        # Essential cleaning for plotting
        for col in ['HSC', 'Last', 'Overall']:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        df.dropna(subset=['HSC', 'Last', 'Overall'], inplace=True)
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

df = load_data(DATA_URL)

st.title("🎯 Objective 1: Prior Academic and Study Habits")
st.markdown("---")

if not df.empty:
    st.subheader("A. Last Score vs. HSC Score")
    # This is the scatter plot you previously requested
    fig_scatter = px.scatter(
        df,
        x='HSC',
        y='Last',
        color='Gender',
        title="Last Semester Score vs. Higher Secondary Score (HSC)",
        template='plotly_white'
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    # Placeholder for other Objective 1 plots (Heatmap, Attendance Bar)
    st.info("You can add the Correlation Heatmap and the Attendance Bar Chart here.")
else:
    st.warning("Data could not be loaded for analysis.")

