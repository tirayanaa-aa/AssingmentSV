import streamlit as st
from utils import DF

# --- Page Content ---
st.title("📊 Student Performance Metrics Dashboard")
st.header("Project Overview: Scientific Visualization in Education", divider="blue")

# Add a banner image at the top
banner_image_1 = 'https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/main/3u1i.jpeg' 
st.image(banner_image_1, use_container_width=True)

st.write(
    """
    This dashboard applies principles of ***Scientific Visualization*** to a dataset of student performance. Our goal is to transform complex academic, habitual, and demographic data into clear, actionable visual insights.
    
    By using computational visualization techniques, we aim to identify key predictors of success and areas for potential intervention that would be difficult to spot in raw numerical tables.
    """
)

banner_image_2 = 'https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/main/3u1i_2.jpeg' 
st.image(banner_image_2, use_container_width=True)

st.write(
    """
    ### 🎯 Core Objectives of this Analysis

    The purpose of this exercise is to ***enhance comprehension and decision-making*** in academic guidance. The dashboard is structured into three main analytical objectives:

    1.  **Objective 1 (Academic & Habits):** Analyze the direct correlation between past scores (HSC/SSC), class attendance, and study time with overall performance.
    2.  **Objective 2 (Demographic & Socioeconomic):** Examine how factors like **Gender**, **Department**, **Hometown**, and **Income Level** influence the distribution of student performance (CGPA).
    3.  **Objective 3 (Temporal & Interaction):** Investigate performance trends across **Semesters** and the combined effects of habits like **Preparation Time** and **Gaming**.
    
    By completing this project, students should be able to produce **informative, accurate, and interactive visualizations** that effectively communicate scientific findings.
    """
)

st.markdown("---")

# Data Status Check
if DF.empty:
    st.error("Data loading failed. Please check the `utils.py` file and the data source.")
else:
    st.success(f"Data for the analysis loaded successfully. Total records: {len(DF)}.")
    st.info("Navigate to the **'Analisis Prestasi Pelajar'** menu to begin exploring the visualizations.")
