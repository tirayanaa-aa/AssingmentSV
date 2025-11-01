import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go # Added this back for completeness

# --- Constants for Data and Columns ---
DATA_FILE = 'ResearchInformation3.csv' # Use your local file name
COL_HSC_GPA = 'HSC'
COL_SSC_GPA = 'SSC'
COL_OVERALL = 'Overall'
COL_GENDER = 'Gender'
COL_ATTENDANCE = 'Attendance'
# ... (Add any other necessary column constants)

# --- Data Loading and Cleaning (Place it here) ---
@st.cache_data
def load_data():
    """
    Loads the local dataset and performs necessary cleaning/typing.
    """
    try:
        df = pd.read_csv(DATA_FILE)

        # 1. Convert relevant columns to numeric (handling errors)
        for col in [COL_HSC_GPA, COL_SSC_GPA, COL_OVERALL]:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # 2. Convert categorical columns to appropriate types
        df[COL_ATTENDANCE] = df[COL_ATTENDANCE].astype('category')
        
        # 3. Drop rows with missing values in key columns
        df.dropna(subset=[COL_HSC_GPA, COL_SSC_GPA, COL_OVERALL], inplace=True)
        
        return df
    except FileNotFoundError:
        st.error(f"Error: The data file '{DATA_FILE}' was not found.")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Error loading or processing data: {e}")
        return pd.DataFrame()

# Load the cleaned data once and cache it
df = load_data()

# --- CONFIGURATION (First st command - Now safe to execute) ---
st.set_page_config(layout="wide", page_title="Student Performance Metrics")
st.header("Scientific Visualization", divider="gray")
st.title("🎓 Student Performance Metrics")
st.markdown("---")

# --- App Content Starts Here ---
if df.empty:
    st.stop()

st.subheader("Data Preview")
st.dataframe(df.head())

# ... (rest of your app code, which uses the 'df' DataFrame)
