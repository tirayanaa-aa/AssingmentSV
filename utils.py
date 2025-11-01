import streamlit as st
import pandas as pd
from collections import OrderedDict

# --- Constants ---
# Assuming the file is hosted online or accessible via a path
DATA_URL = 'https://raw.githubusercontent.com/tirayanaa-aa/AssingmentSV/refs/heads/main/processed_data.csv'

# Define columns
COL_HSC = 'HSC'
COL_SSC = 'SSC'
COL_LAST = 'Last'
COL_OVERALL = 'Overall'
COL_PREPARATION = 'Preparation'
COL_ATTENDANCE = 'Attendance'
COL_GENDER = 'Gender'
COL_DEPARTMENT = 'Department'
COL_HOMETOWN = 'Hometown'
COL_INCOME = 'Income'
COL_SEMESTER = 'Semester'
COL_GAMING = 'Gaming'

# Categorical orderings for plotting consistency
ATTENDANCE_ORDER = ['0%-19%', '20%-39%', 'Below 40%', '40%-59%', '60%-79%', '80%-100%']
PREP_ORDER = ['0-1 Hour', '1-2 Hours', '2-3 Hours', 'More than 3 Hours']
GAMING_ORDER = ['0-1 Hour', '1-2 Hours', '2-3 Hours', 'More than 3 Hours']

# --- Data Loading and Caching ---

@st.cache_data
def load_data(url):
    """Loads and pre-processes the dataset."""
    try:
        df = pd.read_csv(url)
        
        # Ensure core academic columns are numeric
        required_cols = [COL_HSC, COL_SSC, COL_LAST, COL_OVERALL]
        for col in required_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')

        # Create numerical mappings for correlation
        preparation_mapping = OrderedDict(zip(PREP_ORDER, [0.5, 1.5, 2.5, 3.5]))
        if COL_PREPARATION in df.columns:
            df['Preparation_numeric'] = df[COL_PREPARATION].map(preparation_mapping)
        
        attendance_mapping = OrderedDict(zip(ATTENDANCE_ORDER, [10, 30, 30, 50, 70, 90]))
        if COL_ATTENDANCE in df.columns:
             df['Attendance_numeric'] = df[COL_ATTENDANCE].map(attendance_mapping)
             df[COL_ATTENDANCE] = pd.Categorical(df[COL_ATTENDANCE], categories=[c for c in ATTENDANCE_ORDER if c in df[COL_ATTENDANCE].unique()], ordered=True)

        # Handle Semester column for line plot ordering
        if COL_SEMESTER in df.columns:
            df['Semester_sort'] = df[COL_SEMESTER].str.extract('(\d+)').astype(float)
        
        df.dropna(subset=[COL_HSC, COL_LAST, COL_OVERALL], inplace=True)

        # In a real app, you might not show st.success here, but we'll leave it for debugging
        # st.success(f"Successfully loaded and pre-processed {len(df)} rows.")
        return df
    except Exception as e:
        st.error(f"Error loading or processing data from URL: {e}")
        return pd.DataFrame()

# Load the data once and make it accessible
DF = load_data(DATA_URL)

