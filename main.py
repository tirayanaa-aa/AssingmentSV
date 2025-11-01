import streamlit as st

# --- Configuration ---
st.set_page_config(
    page_title="Student Performance Metrics",
    layout="wide"
)

# --- Define Pages ---

# 1. Scientific Visualization Introduction/Context Page (This is the new starting page)
viz_intro = st.Page(
    'pages/dashboard_context.py', 
    title='Visualisasi Ilmiah (Start)', 
    default=True, 
    icon=":material/visibility:"
)

# 2. Student Performance Metrics Dashboard Pages
# Files are assumed to be in the 'pages/' subdirectory
obj1 = st.Page('pages/objective1.py', title='Objektif 1: Akademik & Tabiat', icon=":material/trending_up:")
obj2 = st.Page('pages/objective2.py', title='Objektif 2: Demografi & Ekonomi', icon=":material/group:")
obj3 = st.Page('pages/objective3.py', title='Objektif 3: Tren & Interaksi', icon=":material/timeline:")

# --- Navigation Structure ---
pg = st.navigation(
    {
        "Menu Utama": [viz_intro],
        "Analisis Prestasi Pelajar": [obj1, obj2, obj3]
    }
)

# Run the navigation
pg.run()
