import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils import DF, COL_HSC, COL_LAST, COL_GENDER, COL_ATTENDANCE, COL_OVERALL, COL_SSC

# --- Page Setup ---
st.title("🎯 Objective 1: Prior Academic & Habits")
st.header("Visualizing the relationship between academic history, study habits, and performance.", divider="blue")

if DF.empty:
    st.warning("Data is not available. Check the homepage for data status.")
    st.stop()

# =========================================================================
# 📢 SUMMARY METRICS SECTION: STUDENT PERFORMANCE OVERVIEW (Enhanced)
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
# --- VISUALIZATIONS SECTION ---
# =========================================================================

col1, col2 = st.columns(2)

with col1:
    # --- 1A. Scatter Plot: Last Score vs. HSC Score ---
    st.subheader("A. Last Score vs. HSC Score (Scatter)")
    if all(col in DF.columns for col in [COL_HSC, COL_LAST]):
        fig_scatter = px.scatter(
            DF, x=COL_HSC, y=COL_LAST, 
            color=COL_GENDER if COL_GENDER in DF.columns else None,
            title="Last Semester Score vs. Higher Secondary Score (HSC)",
            template='plotly_white'
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

with col2:
    # --- 1B. Mean Overall CGPA by Attendance (Bar Chart) ---
    st.subheader("B. Mean Overall CGPA by Attendance (Bar Chart)")
    if COL_ATTENDANCE in DF.columns and COL_OVERALL in DF.columns:
        mean_overall_by_attendance = DF.groupby(COL_ATTENDANCE, observed=True)[COL_OVERALL].mean().reset_index()
        mean_overall_by_attendance.columns = [COL_ATTENDANCE, 'Mean Overall CGPA']

        fig_bar = px.bar(
            mean_overall_by_attendance, x=COL_ATTENDANCE, y='Mean Overall CGPA',
            color='Mean Overall CGPA', color_continuous_scale=px.colors.sequential.Viridis,
            text='Mean Overall CGPA', title='Mean Overall CGPA by Class Attendance Level'
        )
        fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")

# --- 1C. Correlation Matrix Heatmap ---
st.subheader("C. Correlation Matrix of Key Numerical Variables (Heatmap)")
numerical_cols_corr = [COL_HSC, COL_SSC, 'Preparation_numeric', 'Attendance_numeric', COL_LAST, COL_OVERALL]
available_cols_corr = [col for col in numerical_cols_corr if col in DF.columns]

if len(available_cols_corr) >= 2:
    correlation_matrix = DF[available_cols_corr].corr().round(2)

    fig_corr = go.Figure(data=go.Heatmap(
        z=correlation_matrix.values, x=correlation_matrix.columns, y=correlation_matrix.index,
        colorscale='RdBu', zmin=-1, zmax=1, text=correlation_matrix.values, texttemplate="%{text}",
        textfont={"size": 10}
    ))

    fig_corr.update_layout(title='Correlation Matrix of Academic and Habit Variables', height=600)
    st.plotly_chart(fig_corr, use_container_width=True)
