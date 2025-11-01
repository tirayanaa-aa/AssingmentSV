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

# Assuming the DataFrame is named 'df' from previous operations.
# If your DataFrame variable is named differently, replace 'df' below.

# Create the interactive scatter plot using plotly.express
fig = px.scatter(
    data_frame=df,
    x='HSC',
    y='Last',
    title='Last Semester Score vs. Higher Secondary Score (HSC)',
    # Customize hover labels for clarity
    labels={
        'HSC': 'HSC Score',
        'Last': 'Last Semester Score'
    },
    # Optional: Add color/size for further analysis (e.g., color by Gender)
    # color='Gender',
)

# Customize layout (optional)
fig.update_layout(
    xaxis_title='HSC Score',
    yaxis_title='Last Semester Score'
)

# Display the plot
fig.show()
