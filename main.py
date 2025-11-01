import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURATION (First st command) ---
st.set_page_config(layout="wide", page_title="Student Performance Metrics")
st.header("Scientific Visualization", divider="gray")
st.title("🎓 Student Performance Metrics")
st.markdown("---")

# --- Data Loading and Caching ---
DATA_URL = 'https://raw.githubusercontent.com/tirayanaa-aa/AssingmentSV/refs/heads/main/processed_data.csv'
COL_OVERALL = 'Overall' # Assuming 'Overall' is the main performance column

@st.cache_data
def load_data(url):
    """
    Loads the dataset from the provided URL, handles potential errors,
    and performs basic cleaning.
    """
    try:
        df = pd.read_csv(url)
        st.success(f"Successfully loaded {len(df)} rows from GitHub.")

        # Ensure the 'Overall' column is numeric for plotting
        if COL_OVERALL in df.columns:
            df[COL_OVERALL] = pd.to_numeric(df[COL_OVERALL], errors='coerce')
            df.dropna(subset=[COL_OVERALL], inplace=True)

        return df
    except Exception as e:
        st.error(f"Error loading data from URL: {e}")
        return pd.DataFrame()

# Load the data
df = load_data(DATA_URL)

# --- Streamlit Application Content ---

st.title("📊 Student Performance Data Explorer")
st.markdown("---")

if df.empty:
    st.warning("Cannot proceed as the DataFrame is empty or failed to load.")
    st.stop()

# 1. Display the head of the DataFrame (as requested)
st.subheader("Data Preview (First 5 Rows)")
# Using st.dataframe is the Streamlit equivalent of display(df_url.head())
st.dataframe(df.head(), use_container_width=True)

st.divider()

# 2. Example Visualization using Plotly (to demonstrate integration)
st.subheader("Interactive Plotly Visualization: Overall CGPA Distribution")

if COL_OVERALL in df.columns:
    # Create the interactive histogram using Plotly Express
    fig = px.histogram(
        df,
        x=COL_OVERALL,
        nbins=20,
        title="Distribution of Student Overall CGPA",
        labels={COL_OVERALL: 'Overall CGPA'},
        template='plotly_dark' # Using a dark theme for contrast
    )
    fig.update_layout(
        xaxis_title="Overall CGPA",
        yaxis_title="Number of Students"
    )
    
    # Display the Plotly figure in Streamlit
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error(f"Cannot plot: The required column '{COL_OVERALL}' is missing from the data.")
