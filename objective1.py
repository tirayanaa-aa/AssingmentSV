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
# 📢 SUMMARY METRICS SECTION: INSERT HERE
# =========================================================================

st.subheader("Key Performance Indicators (KPIs)")

# Ensure 'Attendance_numeric' exists, which is created in utils.py
if 'Attendance_numeric' in DF.columns and 'Preparation_numeric' in DF.columns:
    col_kpi1, col_kpi2, col_kpi3 = st.columns(3)

    # 1. Overall Average CGPA
    avg_cgpa = DF[COL_OVERALL].mean().round(2)
    col_kpi1.metric(
        label="Overall Average CGPA", 
        value=f"{avg_cgpa:.2f}"
    )

    # 2. Attendance-Performance Correlation
    corr_attend = DF['Attendance_numeric'].corr(DF[COL_OVERALL]).round(2)
    col_kpi2.metric(
        label="Attendance vs. Overall CGPA Correlation", 
        value=f"{corr_attend:.2f}",
        delta="Strong Positive" if corr_attend > 0.5 else "Moderate"
    )

    # 3. HSC-Performance Correlation
    corr_hsc = DF[COL_HSC].corr(DF[COL_OVERALL]).round(2)
    col_kpi3.metric(
        label="HSC Score vs. Overall CGPA Correlation", 
        value=f"{corr_hsc:.2f}"
    )

st.markdown("---") # Visual separation before the charts begin

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

# ... (rest of the code for 1B and 1C continues here) ...
# ... (The rest of your original code follows below) ...

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
