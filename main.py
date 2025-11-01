import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Constants for Data and Columns ---
# Use the local file name where your data resides
DATA_FILE = 'ResearchInformation3.csv'

# Define constants for the actual column names in ResearchInformation3.csv
COL_SSC_GPA = 'SSC'
COL_HSC_GPA = 'HSC'
COL_GENDER = 'Gender'
COL_OVERALL = 'Overall'
COL_ATTENDANCE = 'Attendance'

# --- Data Loading and Preprocessing ---
@st.cache_data
def load_data():
    """
    Loads the local dataset.
    """
    try:
        # Load the CSV file
        df = pd.read_csv(DATA_FILE)

        # Basic cleaning and type conversion
        df[COL_HSC_GPA] = pd.to_numeric(df[COL_HSC_GPA], errors='coerce')
        df[COL_SSC_GPA] = pd.to_numeric(df[COL_SSC_GPA], errors='coerce')
        df[COL_OVERALL] = pd.to_numeric(df[COL_OVERALL], errors='coerce')

        # Drop rows with missing values in key columns
        df.dropna(subset=[COL_HSC_GPA, COL_SSC_GPA, COL_OVERALL], inplace=True)

        return df
    except FileNotFoundError:
        st.error(f"Error: The data file '{DATA_FILE}' was not found. Please ensure it is uploaded.")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Error processing data: {e}")
        return pd.DataFrame()

