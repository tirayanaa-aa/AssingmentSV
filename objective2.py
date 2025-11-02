import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils import DF, COL_DEPARTMENT, COL_GENDER, COL_OVERALL, COL_HOMETOWN, COL_INCOME

# --- Page Setup ---
st.title("👤 Objective 2: Demographic & Socioeconomic Factors")
st.header("Analyzing performance variations across different demographic and socioeconomic groups.", divider="red")

if DF.empty:
    st.warning("Data is not available. Check the homepage for data status.")
    st.stop()


# =========================================================================
# 📢 SUMMARY METRICS SECTION: DEMOGRAPHIC PERFORMANCE OVERVIEW
# =========================================================================
st.subheader("📈 Overall Performance Snapshot")

if COL_OVERALL in DF.columns:
    # Compute basic descriptive statistics for the main performance metric
    avg_cgpa = DF[COL_OVERALL].mean().round(2)
    median_cgpa = DF[COL_OVERALL].median().round(2)
    min_cgpa = DF[COL_OVERALL].min().round(2)
    max_cgpa = DF[COL_OVERALL].max().round(2)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Average Overall CGPA 🎓", f"{avg_cgpa:.2f}", help="Mean of all students' CGPA.")
    col2.metric("Median Overall CGPA 📊", f"{median_cgpa:.2f}", help="The middle value of all CGPA scores.")
    col3.metric("Minimum CGPA 📉", f"{min_cgpa:.2f}", help="Lowest CGPA recorded.")
    col4.metric("Maximum CGPA 🏆", f"{max_cgpa:.2f}", help="Highest CGPA recorded.")

else:
    st.warning("Overall CGPA column is missing for summary statistics.")

st.markdown("---")

# =========================================================================
# 🎯 KEY FINDINGS SUMMARY BOX (Objective 2)
# =========================================================================
st.subheader("📚 Key Findings Summary: Demographic Factors")
st.info(
    """
    This objective analyzes structural influences on student performance based on their background. 
    The grouped bar chart often reveals **performance variations between departments**, suggesting differences in course rigor or grading standards. Furthermore, **gender-based gaps** in average CGPA are sometimes evident within specific majors. 
    The distribution plots indicate that **socioeconomic background is a contributing factor**; higher-income groups or students from more developed hometowns may exhibit a tighter, higher median CGPA distribution, reflecting greater access to educational support and resources. 
    Collectively, these visualizations confirm that academic performance is not purely a function of individual effort but is partially shaped by external demographic and socioeconomic conditions.
    """
)

st.markdown("---") # Separation line before charts

# =========================================================================
# --- VISUALIZATIONS SECTION ---
# =========================================================================

# --- 2A. Average Overall CGPA by Department and Gender (Grouped Bar Chart) ---
st.subheader("1. Average Overall CGPA by Department and Gender")
if all(col in DF.columns for col in [COL_DEPARTMENT, COL_GENDER, COL_OVERALL]):
    dept_gender_overall = DF.groupby([COL_DEPARTMENT, COL_GENDER])[COL_OVERALL].mean().reset_index()

    fig_bar_dept_gender = px.bar(
        dept_gender_overall, x=COL_DEPARTMENT, y=COL_OVERALL, 
        color=COL_GENDER, barmode='group',
        title='Average Overall CGPA by Department and Gender',
        template='plotly_white',
    )
    fig_bar_dept_gender.update_xaxes(tickangle=45)
    st.plotly_chart(fig_bar_dept_gender, use_container_width=True)

    # SHORT INTERPRETATION 2A
    with st.expander("📝 Interpretation A: Departmental & Gender Influence"):
        st.markdown(
            """
            **Pattern:** Significant variations in average CGPA are observed both **across departments** and **between genders** within the same department.
            
            **Meaning:** This suggests that academic performance is influenced by **departmental differences in curriculum difficulty, grading policies, or internal competition**. Gender gaps highlight areas where specific support or bias might exist.
            """
        )


st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    # --- 2B. Overall CGPA Distribution by Hometown (Violin Plot) ---
    st.subheader("2. Overall CGPA Distribution by Hometown (Violin)")
    if all(col in DF.columns for col in [COL_HOMETOWN, COL_OVERALL]):
        fig_violin = px.violin(
            DF, x=COL_HOMETOWN, y=COL_OVERALL,
            box=True, points="all",
            title='Overall CGPA Distribution by Hometown',
            template='plotly_white'
        )
        st.plotly_chart(fig_violin, use_container_width=True)

        # SHORT INTERPRETATION 2B
        with st.expander("📝 Interpretation B: Hometown Distribution"):
            st.markdown(
                """
                **Pattern:** Differences in the **density and width** of the violin shapes across hometown categories. For instance, urban areas might show a narrower, higher distribution.
                
                **Meaning:** The consistency and median CGPA are potentially linked to the quality of pre-university education or the level of exposure and resources available in different residential backgrounds. **Hometown can influence academic readiness.**
                """
            )

with col4:
    # --- 2C. Overall CGPA Distribution by Income Level (Box Plot) ---
    st.subheader("3. Overall CGPA Distribution by Income Level (Box)")
    if all(col in DF.columns for col in [COL_INCOME, COL_OVERALL]):
        income_order = [
            'Low (Below 15,000)', 'Lower middle (15,000-30,000)', 
            'Upper middle (30,000-50,000)', 'High (Above 50,000)'
        ]
        valid_income_order = [inc for inc in income_order if inc in DF[COL_INCOME].unique()]

        fig_box = px.box(
            DF, x=COL_INCOME, y=COL_OVERALL,
            category_orders={COL_INCOME: valid_income_order},
            title='Overall CGPA Distribution by Income Level',
            template='plotly_white'
        )
        fig_box.update_xaxes(tickangle=45)
        st.plotly_chart(fig_box, use_container_width=True)

        # SHORT INTERPRETATION 2C
        with st.expander("📝 Interpretation C: Income Level Impact"):
            st.markdown(
                """
                **Pattern:** Compare the **median line** (50th percentile) and the **interquartile range** (box height) across income groups. Often, higher income groups show higher medians and smaller variability.
                
                **Meaning:** Higher income may correlate with **increased stability and access to academic resources** (e.g., technology, books, tutoring), reducing performance risk. This highlights socioeconomic factors as a significant influence on academic achievement.
                """
            )
