import streamlit as st

# --- Configuration ---
st.set_page_config(
    page_title="Student Performance Metrics",
    layout="wide"
)

# --- Define Pages ---

# 1. Scientific Visualization Introduction/Context Page
# SET AS DEFAULT: This will be the first page users see.
# In main.py
viz_intro = st.Page(
    'pages/dashboard_context.py', 
    title='Visualisasi Ilmiah (Start)',  # <-- This line was indented too far
    default=True, 
    icon=":material/visibility:"
)

# 2. Student Performance Metrics Dashboard Pages
obj1 = st.Page('pages/objective1_page.py', title='Objektif 1: Akademik & Tabiat', icon=":material/trending_up:")
obj2 = st.Page('pages/objective2_page.py', title='Objektif 2: Demografi & Ekonomi', icon=":material/group:")
obj3 = st.Page('pages/objective3_page.py', title='Objektif 3: Tren & Interaksi', icon=":material/timeline:")

# --- Navigation Structure ---
pg = st.navigation(
    {
        # We can still keep the 'Menu Utama' section, but it now only holds the intro page
        "Menu Utama": [viz_intro],
        "Analisis Prestasi Pelajar": [obj1, obj2, obj3]
    }
)

# Run the navigation
pg.run()
