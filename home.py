import streamlit as st
from utils import DF # Import DF to check data status

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

banner_image_2 = 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&w=1200&q=60' 
st.image(banner_image_2, use_container_width=True)

st.write(
    """
    The aim of scientific visualization is not merely to present data attractively, but to **enhance comprehension and decision-making** through visual analytics. 
    Applications span across disciplines such as *climate science, medicine, engineering, data science, and environmental studies*.

    ### Dashboard Objectives:
    Navigate to the 'Analisis Prestasi Pelajar' section to view interactive visualizations that:
    1.  **Correlate** academic history and habits.
    2.  **Compare** performance across demographic groups.
    3.  **Track** performance trends over semesters.
    """
)

if DF.empty:
    st.error("Data loading failed. Check `utils.py` for errors.")
else:
    st.info(f"Data for the dashboard loaded successfully ({len(DF)} records).")
