import streamlit as st
from utils import DF

# --- Page Content ---
st.title("📊 Student Performance Metrics Dashboard")
st.header("Project Overview: Scientific Visualization in Education", divider="blue")

# 📢 ACTION REQUIRED: Replace the URL below with the direct link to your new banner image.
# Example of a new image URL: 'https://new-image-host.com/path/to/my/new_banner.png'
banner_image_1 = 'https://assets.qlik.com/image/upload/w_1408/q_auto/qlik/glossary/compare/seo-hero-compare_cyuosd.jpg' 

st.image(banner_image_1, use_container_width=True)
# ... (rest of your home.py content remains the same)

st.write(
    """
    ***Scientific Visualization*** is a multidisciplinary field that focuses on transforming complex scientific data into visual forms that are easier to understand, interpret, and communicate. 
    Through the use of computational techniques, visualization helps researchers explore datasets, identify hidden patterns, and gain insights that would otherwise remain obscure in numerical form.
    """
)

banner_image_2 = 'https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/main/3u1i_2.jpeg' 
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
