import streamlit as st
from utils import DF  # Import DF to check data status

# --- Page Configuration ---
st.set_page_config(page_title="Homepage | Student Performance Metrics", layout="wide")

# --- Page Title ---
st.title("🎓 Student Performance Metrics Dashboard")
st.header("Project Overview: Scientific Visualization in Education", divider="blue")

# --- Top Banner ---
st.markdown(
    """
    <div style='text-align:center;'>
        <img src='https://images.unsplash.com/photo-1523050854058-8df90110c9f1' 
             style='width:90%; border-radius:15px; box-shadow:0 4px 10px rgba(0,0,0,0.3);'>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Introduction Section ---
st.write(
    """
    This dashboard applies the principles of **Scientific Visualization** to explore a dataset of student performance.
    The goal is to transform complex academic, behavioral, and demographic data into **clear, actionable insights** 
    that reveal key performance drivers and patterns that may not be visible in raw data.

    By visualizing this information interactively, educators and analysts can better identify the relationships between 
    academic results, study habits, and socioeconomic backgrounds — supporting evidence-based academic improvement.
    """
)

# --- Secondary Banner (Data Theme) ---
st.markdown(
    """
    <div style='text-align:center; margin-top:30px;'>
        <img src='https://images.unsplash.com/photo-1584697964190-2c194de9ae59' 
             style='width:90%; border-radius:15px; box-shadow:0 4px 10px rgba(0,0,0,0.3);'>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Objectives Section ---
st.markdown(
    """
    ### 🎯 Core Objectives of This Dashboard

    This analysis is structured around three main **visualization objectives** that support understanding of student performance:

    1. **Objective 1 – Prior Academic & Habits:**  
       Explore how academic history (HSC/SSC), class attendance, and study preparation influence overall performance.

    2. **Objective 2 – Demographic & Socioeconomic Factors:**  
       Examine how variables like **Gender**, **Department**, **Hometown**, and **Income Level** relate to performance outcomes (CGPA).

    3. **Objective 3 – Temporal & Habit Interactions:**  
       Analyze performance trends across **semesters** and explore how habits such as **study time** and **gaming** impact results over time.

    Together, these objectives help uncover actionable insights that can support academic decision-making and student guidance.
    """
)

st.markdown("---")

# --- Data Status Check ---
if DF.empty:
    st.error("❌ Data loading failed. Please check the `utils.py` file and your internet connection.")
else:
    st.success(f"✅ Data for the analysis loaded successfully. Total records: {len(DF)}.")
    st.info("Use the **sidebar menu** to explore visualizations for each objective.")
