import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Constants for Data and Columns ---
DATA_URL = 'https://raw.githubusercontent.com/tirayanaa-aa/AssingmentSV/refs/heads/main/processed_data.csv'

# --- Data Loading and Preprocessing ---
@st.cache_data
def load_data():
    """
    Loads the dataset and cleans up the academic year column name.
    """
    try:
        df = pd.read_csv(DATA_URL)
        
        # Identify and rename the problematic academic year column
        academic_col_match = [col for col in df.columns if 'Academic Year in EU' in col]
        
        if academic_col_match:
            df.rename(columns={academic_col_match[0]: COL_ACADEMIC_YEAR_CLEANED}, inplace=True)
            df[COL_ACADEMIC_YEAR_CLEANED] = df[COL_ACADEMIC_YEAR_CLEANED].astype(str).str.strip()
        else:
            st.error("The 'Bachelor Academic Year in EU' column was not found. Please check the CSV file structure.")
            return pd.DataFrame()
        
        return df
    except Exception as e:
        st.error(f"Error loading data from GitHub: {e}")
        return pd.DataFrame()

df = load_data()

# --- Streamlit App Layout ---
st.set_page_config(
    page_title="Student Performance Metrics",
    layout="wide"
)

st.title("🎓 Student Performance Metrics")

if df.empty or not all(col in df.columns for col in [COL_SSC_GPA, COL_HSC_GPA, COL_GENDER, COL_ACADEMIC_YEAR_CLEANED]):
    st.error("Dashboard cannot run due to missing data or essential columns.")
    st.stop()

st.subheader("Data Preview")
st.dataframe(df.head())

st.divider()
