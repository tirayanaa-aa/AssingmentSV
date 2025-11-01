import streamlit as st

# --- Configuration ---
st.set_page_config(
    page_title="Student Performance Metrics",
    layout="wide"
)

# --- Define Pages ---

# Ensure all file references exist in the same directory as main.py
home = st.Page('home.py', title='Homepage', default=True, icon=":material/home:")
obj1 = st.Page('objective1.py', title='Objective 1: Academic & Habits', icon=":material/trending_up:")
obj2 = st.Page('objective2.py', title='Objective 2: Demographic & Socioeconomic', icon=":material/group:")
obj3 = st.Page('objective3.py', title='Objective 3: Temporal & Interaction', icon=":material/timeline:")

# --- Navigation Structure ---
pg = st.navigation(
    {
        "Menu Utama": [home],
        "Analisis Prestasi Pelajar": [obj1, obj2, obj3]
    }
)

# Run the navigation
pg.run()
