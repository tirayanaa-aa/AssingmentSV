import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
# Assuming these additional columns needed for Objective 2 charts are defined in utils
from utils import (DF, COL_GENDER, COL_OVERALL, COL_DEPARTMENT, 
                   COL_HOMETOWN, COL_INCOME, COL_HSC, COL_LAST, 
                   COL_ATTENDANCE, COL_SSC) 

# --- Page Setup (CORRECTED) ---
st.title("👤 Objective 2: Demographic & Socioeconomic Factors")
st.header("Analyzing performance variations across different demographic and socioeconomic groups.", divider="red")

if DF.empty:
    st.warning("Data is not available. Check the homepage for data status.")
    st.stop()

# =========================================================================
# 📢 SUMMARY METRICS SECTION: STUDENT PERFORMANCE OVERVIEW (User's original code kept)
# =========================================================================
st.subheader("📈 Summary Metrics Overview")

required_cols = [COL_OVERALL, 'Attendance_numeric', 'Preparation_numeric']
if all(col in DF.columns for col in required_cols):

    # Compute metrics
    avg_cgpa = DF[COL_OVERALL].mean().round(2)
    avg_attendance = DF['Attendance_numeric'].mean().round(1)
    avg_study = DF['Preparation_numeric'].mean().round(1)
    top_score = DF[COL_OVERALL].max().round(2)

    # Interpretations for display
    def interpret_cgpa(cgpa):
        if cgpa >= 3.50:
            return "🌟 Excellent"
        elif cgpa >= 3.00:
            return "👍 Good"
        else:
            return "⚠️ Needs Improvement"

    def interpret_attendance(att):
        if att >= 85:
            return "🟢 Very Consistent"
        elif att >= 70:
            return "🟡 Moderate"
        else:
            return "🔴 Low"

    def interpret_study(hours):
        if hours >= 3:
            return "📘 Dedicated"
        elif hours >= 1.5:
            return "📗 Average"
        else:
            return "📕 Minimal Effort"

    # Create layout
    col1, col2, col3, col4 = st.columns(4)

    # --- Metric 1: Average CGPA ---
    col1.metric(
        label="Average Overall CGPA 🎓",
        value=f"{avg_cgpa:.2f}",
        delta=interpret_cgpa(avg_cgpa),
        help="Mean of all students' CGPA in the dataset."
    )

    # --- Metric 2: Average Attendance ---
    col2.metric(
        label="Average Attendance (%) 🏫",
        value=f"{avg_attendance}%",
        delta=interpret_attendance(avg_attendance),
        help="Shows the average attendance percentage among students."
    )

    # --- Metric 3: Average Study Time ---
    col3.metric(
        label="Average Study Time (hrs/day) ⏰",
        value=f"{avg_study}",
        delta=interpret_study(avg_study),
        help="Indicates the average daily preparation or study time."
    )

    # --- Metric 4: Top CGPA ---
    col4.metric(
        label="Top Student CGPA 🏅",
        value=f"{top_score:.2f}",
        delta="🏆 Outstanding Achievement" if top_score >= 3.80 else "🎖️ High Performer",
        help="Displays the highest CGPA recorded in this dataset."
    )

else:
    st.warning("Some required numeric columns are missing. Please verify 'utils.py' or data preparation steps.")

st.markdown("---")  # Separation line before charts

# =========================================================================
# --- VISUALIZATIONS SECTION (Objective 2 Charts with Interpretations) ---
# =========================================================================

# --- 2.1 Average Overall CGPA by Department and Gender (Bar Chart) ---
st.subheader("2.1 Average Overall CGPA by Department and Gender")
if all(col in DF.columns for col in [COL_DEPARTMENT, COL_GENDER, COL_OVERALL]):
    dept_gender_overall = DF.groupby([COL_DEPARTMENT, COL_GENDER], observed=True)[COL_OVERALL].mean().reset_index()

    fig_bar_dept_gender = px.bar(
        dept_gender_overall, x=COL_DEPARTMENT, y=COL_OVERALL, 
        color=COL_GENDER, barmode='group',
        title='Average Overall CGPA by Department and Gender',
        template='plotly_white',
    )
    fig_bar_dept_gender.update_xaxes(tickangle=45)
    st.plotly_chart(fig_bar_dept_gender, use_container_width=True)

    # SHORT INTERPRETATION 2.1
    with st.expander("📝 Interpretation 2.1: Departmental and Gender Gaps"):
        st.markdown(
            """
            **Pattern:** Performance shows variation by **Department** and often reveals a **gender gap** in specific fields.
            
            **Meaning:** This suggests differences in **subject difficulty** or potential **equity issues** that warrant a focused departmental review.
            """
        )

st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    # --- 2.2 Overall CGPA Distribution by Hometown (Violin Plot) ---
    st.subheader("2.2 Overall CGPA Distribution by Hometown (Violin)")
    if all(col in DF.columns for col in [COL_HOMETOWN, COL_OVERALL]):
        fig_violin = px.violin(
            DF, x=COL_HOMETOWN, y=COL_OVERALL,
            box=True, points="all",
            title='Overall CGPA Distribution by Hometown',
            template='plotly_white'
        )
        st.plotly_chart(fig_violin, use_container_width=True)

        # SHORT INTERPRETATION 2.2
        with st.expander("📝 Interpretation 2.2: Socio-Geographical Impact"):
            st.markdown(
                """
                **Pattern:** The CGPA distribution for 'Rural' students often shows **lower medians** or **greater spread** than 'Urban' students.
                
                **Meaning:** This suggests a **resource gap**. Students from certain hometowns may have received varied preparation, impacting their university performance.
                """
            )

with col4:
    # --- 2.3 Overall CGPA Distribution by Income Level (Box Plot) ---
    st.subheader("2.3 Overall CGPA Distribution by Income Level (Box)")
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
        
        # SHORT INTERPRETATION 2.3
        with st.expander("📝 Interpretation 2.3: Economic Influence"):
            st.markdown(
                """
                **Pattern:** The median CGPA generally **increases** as family Income Level rises.
                
                **Meaning:** This confirms the correlation between **socioeconomic status and academic capital**. Higher income often leads to better access to resources and support, positively influencing student performance.
                """
            )
