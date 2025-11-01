import streamlit as st

st.set_page_config(
    page_title="Student Performance Metrics"
)

objective1 = st.Page('objective1.py', title='PRIOR ACADEMIC & HABITS', icon=":material/thumb_up_off_alt:")

objective2 = st.Page('objective2.py', title='DEMOGRAPHIC & SOCIOECONOMIC', icon=":material/assignment_turned_in:")

objective3 = st.Page('objective3.py', title='TEMPORAL & HABIT INTERACTION', icon=":material/schedule:")

home = st.Page('Homepage.py', title='Homepage', default=True, icon=":material/home:")

pg = st.navigation(
        {
            "Menu": [home, objective1, objective2, objective3]
        }
    )

pg.run()
