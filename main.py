import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuration ---
st.set_page_config(
    page_title="Student Performance Metrics",
    layout="wide"
)

# --- Data Loading and Caching ---
# Using the URL specified in your request
DATA_URL = 'https://raw.githubusercontent.com/tirayanaa-aa/AssingmentSV/refs/heads/main/processed_data.csv'

# Define the columns used in your plot and for context
COL_HSC = 'HSC'
COL_LAST = 'Last'
COL_GENDER = 'Gender'
COL_OVERALL = 'Overall'

@st.cache_data
def load_data(url):
    """
    Loads the dataset from the provided URL, handles potential errors,
    and performs basic cleaning.
    """
    try:
        df = pd.read_csv(url)
        st.success(f"Successfully loaded {len(df)} rows from GitHub.")

        # Ensure key plotting columns are numeric
        required_cols = [COL_HSC, COL_LAST, COL_OVERALL]
        for col in required_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Drop rows missing values in the primary plotting columns
        df.dropna(subset=[COL_HSC, COL_LAST], inplace=True)

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

# 1. Display the head of the DataFrame (equivalent to the 'df' output)
st.subheader("Data Preview (First 5 Rows)")
st.dataframe(df.head(), use_container_width=True)

st.divider()

# 2. Scatter Plot: Last Score vs. HSC Score (Conversion from Matplotlib/Seaborn)
st.subheader("Interactive Plotly Scatter Plot: Last Score vs. HSC Score")
st.markdown("*(Drag to zoom, hover over points for details)*")


if all(col in df.columns for col in [COL_HSC, COL_LAST]):
    # Create the interactive scatter plot using Plotly Express
    fig = px.scatter(
        df,
        x=COL_HSC,
        y=COL_LAST,
        # Adding Gender for color to make the plot more informative
        color=COL_GENDER if COL_GENDER in df.columns else None, 
        title="Last Semester Score vs. Higher Secondary Score (HSC)",
        labels={COL_HSC: 'HSC Score', COL_LAST: 'Last Semester Score'},
        template='plotly_white'
    )
    
    # Customize layout
    fig.update_layout(
        xaxis_title="HSC Score",
        yaxis_title="Last Semester Score",
        height=500
    )
    
    # Display the Plotly figure in Streamlit
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error(f"Cannot plot scatter chart: Required columns ('{COL_HSC}' or '{COL_LAST}') are missing from the data.")


