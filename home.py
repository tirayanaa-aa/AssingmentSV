import streamlit as st

# --- Page Setup ---
st.title("📚 Student Performance Metrics Dashboard Context")
st.header("Understanding the Data and Objectives", divider="blue")

# --- Context Section 1: Data Source and Purpose ---

st.markdown(
    """
    ### 🎯 Project Goal: Identifying Key Performance Predictors
    
    This dashboard analyzes performance data from a cohort of students to identify the most significant factors—academic, habitual, and socioeconomic—that correlate with their **Overall Cumulative Grade Point Average (CGPA)**. 
    
    The insights generated are intended to help academic advisors and faculty develop targeted intervention strategies to improve student outcomes.
    """
)

# You can add a context-relevant image here if you have one related to education or data
# st.image('URL_TO_YOUR_CONTEXT_IMAGE', caption='Visualizing educational data.', use_container_width=True)

# --- Context Section 2: Key Variables Used ---

st.markdown("---")

st.subheader("📊 Key Variables Under Analysis")
st.write(
    """
    The analysis relies on multiple data points categorized into three main areas:
    """
)

col_acad, col_habit, col_socio = st.columns(3)

with col_acad:
    st.markdown("#### **Academic History**")
    st.markdown(
        """
        - **HSC/SSC Scores:** Prior academic achievement.
        - **Last Score:** Performance in the immediate previous semester.
        - **Semester:** Tracking performance changes over time.
        """
    )

with col_habit:
    st.markdown("#### **Study Habits**")
    st.markdown(
        """
        - **Attendance:** Percentage of classes attended (a critical habit).
        - **Preparation:** Hours spent studying or preparing for classes.
        - **Gaming:** Hours spent on non-academic activities (e.g., gaming).
        """
    )

with col_socio:
    st.markdown("#### **Socioeconomic & Demographic**")
    st.markdown(
        """
        - **Gender:** Standard demographic split.
        - **Department:** Academic grouping (context for course difficulty).
        - **Hometown:** Geographic background.
        - **Income:** Family income level (socioeconomic factor).
        """
    )
    
# --- Context Section 3: Navigation Guide ---

st.markdown("---")

st.subheader("🗺️ Dashboard Navigation Guide")
st.markdown(
    """
    Navigate the dashboard using the sidebar menu:
    
    * **Objective 1 (Prior Academic & Habits):** Focuses on correlation and direct impact (e.g., Attendance vs. CGPA).
    * **Objective 2 (Demographic & Socioeconomic):** Examines disparities across groups (e.g., Income, Hometown, Gender).
    * **Objective 3 (Temporal & Habit Interaction):** Tracks performance trends over semesters and the complex relationship between multiple habits (Preparation and Gaming).
    """
)
