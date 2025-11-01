import streamlit as st
from utils import DF  # Import DF to check data status

# --- Page Configuration ---
st.set_page_config(page_title="Homepage | Student Performance Metrics")

# --- Page Title ---
st.title("🎓 Student Performance Metrics Dashboard")
st.header("Project Overview: Scientific Visualization in Education", divider="blue")

# --- Banner Image (Top) ---
banner_image_1 = "https://images.unsplash.com/photo-1523050854058-8df90110c9f1"  # Students studying together
st.image(banner_image_1, use_container_width=True)

# --- Intro Text ---
st.write(
    """
    This dashboard applies principles of **Scientific Visualization** to analyze a dataset on student performance.
    Our goal is to transform academic, behavioral, and demographic data into **clear, data-driven insights** that help
    identify patterns of student success and potential areas for improvement.

    Through interactive visualizations, we aim to uncover relationships between study habits, attendance, and
    socioeconomic factors that may influence academic achievement.
    """
)

# --- Second Banner Image ---
banner_image_2 = "https://images.unsplash.com/photo-1584697964190-2c194de9ae59"  # Data visualization dashboard on laptop
st.image(banner_image_2, use_container_width=True)

# --- Objectives ---
st.write(
    """
    ### 🎯 Core Objectives of this Dashboard

    This analysis aims to support **academic decision-making** through data visualization.  
    The dashboard is structured into **three main objectives**:

    1. **Objective 1 – Prior Academic & Habits:**  
      
