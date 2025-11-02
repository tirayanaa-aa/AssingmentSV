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
# 📢 SUMMARY METRICS SECTION: KPIs
# =========================================================================
st.subheader("📈 Key Performance Indicators (KPIs)")

required_cols = [COL_OVERALL, 'Attendance_numeric', 'Preparation_numeric', COL_HSC]
if all(col in DF.columns for col in required_cols):
    
    # Compute metrics
    avg_cgpa = DF[COL_OVERALL].mean().round(2)
    corr_attend = DF['Attendance_numeric'].corr(DF[COL_OVERALL]).round(2)
    corr_hsc = DF[COL_HSC].corr(DF[COL_OVERALL]).round(2)
    top_score = DF[COL_OVERALL].max().round(2)

    col1, col2, col3, col4 = st.columns(4)

    # Metric 1: Average CGPA
    col1.metric(label="Average Overall CGPA 🎓", value=f"{avg_cgpa:.2f}")

    # Metric 2: Attendance vs. CGPA Correlation
    col2.metric(
        label="Attendance vs. CGPA Corr.", 
        value=f"{corr_attend:.2f}", 
        delta="Strong Positive" if corr_attend > 0.5 else "Moderate"
    )

    # Metric 3: HSC vs. CGPA Correlation
    col3.metric(
        label="HSC vs. CGPA Corr.", 
        value=f"{corr_hsc:.2f}", 
        delta="Strong Positive" if corr_hsc > 0.6 else "Moderate"
    )

    # Metric 4: Top CGPA
    col4.metric(label="Top Student CGPA 🏅", value=f"{top_score:.2f}")

st.markdown("---") # Separation line before charts

# =========================================================================
# --- VISUALIZATIONS SECTION WITH INTERPRETATION ---
# =========================================================================

col1, col2 = st.columns(2)

with col1:
    # --- 1A. Scatter Plot: Last Score vs. HSC Score ---
    st.subheader("1.1 Last Score vs. HSC Score (Scatter)")
    if all(col in DF.columns for col in [COL_HSC, COL_LAST]):
        fig_scatter = px.scatter(
            DF, x=COL_HSC, y=COL_LAST, 
            color=COL_GENDER if COL_GENDER in DF.columns else None,
            title="Last Semester Score vs. Higher Secondary Score (HSC)",
            template='plotly_white'
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
        
        # INTERPRETATION 1.1
        with st.expander("📝 Interpretation of Chart 1.1"):
            st.markdown(
                """
                **Observed Pattern:** The data shows a **positive correlation**; students with higher HSC scores generally achieve higher Last Semester Scores.

                **Scientific Meaning:** This confirms **academic continuity**—prior skills carry over. However, outliers indicate that university success depends on **adaptation and study habits**, not just past achievements.
                """
            )

with col2:
    # --- 1B. Mean Overall CGPA by Attendance (Bar Chart) ---
    st.subheader("1.2 Mean Overall CGPA by Attendance (Bar Chart)")
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
        
        # INTERPRETATION 1.2
        with st.expander("📝 Interpretation of Chart 1.2"):
            st.markdown(
                """
                **Observed Pattern:** A **clear, positive trend** shows Mean Overall CGPA rising consistently as class attendance levels increase.

                **Scientific Meaning:** This establishes **class attendance as a critical behavioral determinant**. Regular presence maximizes material exposure and reinforces disciplined habits, directly leading to superior cumulative performance.
                """
            )

st.markdown("---")

# --- 1C. Correlation Matrix Heatmap ---
st.subheader("1.3 Correlation Matrix of Key Numerical Variables (Heatmap)")
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

    # INTERPRETATION 1.3 (Full width)
    with st.expander("📝 Interpretation of Chart 1.3"):
        st.markdown(
            """
            **Observed Pattern:** The **Last Score** shows the **strongest positive correlation** with **Overall CGPA**. Habit metrics (Preparation, Attendance) show positive but moderate correlations.

            **Scientific Meaning:** **Internal university performance (Last Score) is the most immediate predictor.** The moderate correlation for habits suggests they are **contributing factors**, but that the *quality* and *efficiency* of study time, rather than just quantity, along with inherent ability, are ultimately more influential.
            """
        )
