import streamlit as st
import pandas as pd
import plotly.express as px
# ... (rest of your imports)

# --- CONFIGURATION (First st command) ---
st.set_page_config(layout="wide", page_title="Student Performance Metrics")
st.header("Scientific Visualization", divider="gray")
st.title("🎓 Student Performance Metrics")
st.markdown("---")

import plotly.express as px
import pandas as pd

# Assuming 'df' is the DataFrame loaded from 'ResearchInformation3.csv'
# Replace 'df' with your actual DataFrame variable name if different.

# Load the dataset (if not already loaded in the environment)
# df = pd.read_csv('ResearchInformation3.csv') 

# Create the interactive scatter plot
fig = px.scatter(
    data_frame=df_url, 
    x='HSC', 
    y='Last',
    title='Last Semester Score vs. Higher Secondary Score (HSC)',
    labels={'HSC': 'HSC Score', 'Last': 'Last Semester Score'}
)

# You can optionally customize the layout further
fig.update_layout(
    xaxis_title='HSC Score',
    yaxis_title='Last Score'
)

# Display the plot
fig.show()
