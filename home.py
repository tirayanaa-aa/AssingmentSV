import streamlit as st
from utils import DF  # Import DF to check data status

# --- Page Content ---
st.title("🔬 Introduction to Scientific Visualization")
st.header("Student Performance Metrics Dashboard", divider="blue")

# Add a banner image at the top
banner_image_1 = 'https://images.unsplash.com/photo-1571260899304-425eee4c7efc?auto=format&fit=crop&w=1200&q=60' 
st.image(banner_image_1, use_container_width=True)

st.write(
    """
    ***Scientific Visualization*** is a multidisciplinary field that focuses on transforming complex scientific data into visual forms that are easier to understand, interpret, and communicate. 
    Through the use of computational techniques, visualization helps researchers explore datasets, identify hidden patterns, and gain insights that would otherwise remain obscure in numerical form.
    """
)

st.markdown("""
### 🧠 Why Student Performance Metrics Matter
Understanding student performance through data visualization provides valuable insights into academic achievement, learning behaviors, and participation trends.  
With effective visual tools, educators and decision-makers can identify performance gaps, monitor progress, and design interventions that truly make an impact.  
This dashboard serves as a bridge between data and meaningful academic improvement by transforming raw performance data into **clear, actionable insights**.
""")

# --- Section 2: About the Dataset ---
st.markdown("""
### 📚 About the Dataset
The dataset used in this dashboard represents various aspects of student performance, including academic scores, attendance rates, study habits, and demographic backgrounds.  
It combines **numerical data** (such as examination marks and CGPA) with **categorical information** (such as gender, hometown, and income level) to enable both descriptive and comparative analysis.  
This diversity allows for an in-depth exploration of how different factors contribute to overall academic success.
""")

# --- Section 3: Why Visualization Matters ---
st.markdown("""
### 🎨 Why Visualization Matters
In today’s data-driven education landscape, visualization acts as a **bridge between complexity and clarity**.  
Raw numbers alone cannot reveal relationships or trends — but through charts, heatmaps, and dashboards, we can uncover insights that lead to better decisions.  
Scientific visualization transforms large datasets into *visual narratives* that highlight performance differences, correlations, and growth patterns in a way that’s easy to interpret.
""")

# --- Section 4: How to Use This Dashboard ---
st.markdown("""
### 🧭 How to Use This Dashboard
Navigate through the sidebar to explore the analysis objectives:
1. **Objective 1 – Academic & Habit Patterns:** Explore how study habits, attendance, and prior scores influence student performance.  
2. **Objective 2 – Demographic & Socioeconomic Influences:** Analyze the impact of gender, department, hometown, and income level on academic outcomes.  
3. **Objective 3 – Temporal Trends & Behavioral Interactions:** Observe CGPA changes across semesters and the effect of habits such as study time and gaming.
Each visualization is **interactive** — you can hover, zoom, and filter data to gain deeper insights.
""")

# --- Footer ---
st.markdown("""
---
<center>
👩‍🎓 *Developed by a UMK Student — FSDK*  
📍 Universiti Malaysia Kelantan | 2025
</center>
""", unsafe_allow_html=True)
