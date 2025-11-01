import streamlit as st

st.set_page_config(page_title="Student Performance Metrics", layout="wide")

# Navigation between pages
home = st.Page("Homepage.py", title="🏠 Homepage", default=True)
objective1 = st.Page("objective1.py", title="📈 Prior Academic & Habits")
objective2 = st.Page("objective2.py", title="👥 Demographic & Socioeconomic")
objective3 = st.Page("objective3.py", title="📊 Temporal & Habit Interaction")

pg = st.navigation({
    "Menu": [home, objective1, objective2, objective3]
})

pg.run()

