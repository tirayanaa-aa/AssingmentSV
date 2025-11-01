import streamlit as st

# --- Configuration ---
st.set_page_config(
    page_title="Student Performance Metrics",
    layout="wide" # Use 'wide' layout for better visualization
)

# --- Define Pages ---

# 1. Homepage (Your existing 'home.py')
home = st.Page('home.py', title='Homepage', default=True, icon=":material/home:")

# 2. Main Scientific Visualization Context Page (The descriptive page)
viz_intro = st.Page('dashboard_context.py', title='Visualisasi Ilmiah', icon=":material/visibility:")

# 3. Student Performance Metrics Dashboard Pages (The three objectives)
obj1 = st.Page('pages/objective1_page.py', title='Objektif 1: Akademik & Tabiat', icon=":material/trending_up:")
obj2 = st.Page('pages/objective2_page.py', title='Objektif 2: Demografi & Ekonomi', icon=":material/group:")
obj3 = st.Page('pages/objective3_page.py', title='Objektif 3: Tren & Interaksi', icon=":material/timeline:")

# --- Navigation Structure ---
pg = st.navigation(
    {
        "Menu Utama": [home, viz_intro],
        "Analisis Prestasi Pelajar": [obj1, obj2, obj3]
    }
)

# Run the navigation
pg.run()
