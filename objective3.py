import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils import (
    DF, COL_SEMESTER, COL_OVERALL, COL_DEPARTMENT, COL_LAST, 
    COL_PREPARATION, COL_GAMING, PREP_ORDER, GAMING_ORDER
)

# --- Page Setup ---
st.title("📈 Objective 3: Temporal & Habit Interaction")
st.header("Exploring trends over semesters and the interaction between study habits.", divider="green")

if DF.empty:
    st.warning("Data is not available. Check the homepage for data status.")
    st.stop()

# =========================================================================
# 📢 SUMMARY METRICS SECTION
# =========================================================================
st.subheader("📊 Summary of Key Trends and Habit Insights")

if COL_SEMESTER in DF.columns and COL_OVERALL in DF.columns:
    semester_avg = DF.groupby(COL_SEMESTER)[COL_OVERALL].mean()

    # Calculate metrics
    best_semester = semester_avg.idxmax()
    best_avg = semester_avg.max().round(2)
    worst_semester = semester_avg.idxmin()
    worst_avg = semester_avg.min().round(2)
    sem_diff = (best_avg - worst_avg).round(2)
    overall_mean = DF[COL_OVERALL].mean().round(2)

    # Determine best preparation & gaming group
    if all(col in DF.columns for col in [COL_PREPARATION, COL_OVERALL]):
        prep_avg = DF.groupby(COL_PREPARATION)[COL_OVERALL].mean()
        best_prep = prep_avg.idxmax()
        best_prep_val = prep_avg.max().round(2)
    else:
        best_prep, best_prep_val = "N/A", 0

    if all(col in DF.columns for col in [COL_GAMING, COL_OVERALL]):
        gaming_avg = DF.groupby(COL_GAMING)[COL_OVERALL].mean()
        best_gaming = gaming_avg.idxmax()
        best_gaming_val = gaming_avg.max().round(2)
    else:
        best_gaming, best_gaming_val = "N/A", 0

    # Layout for metrics
    col1, col2, col3, col4 = st.columns(4)

    # 1️⃣ Best Semester
    col1.metric(
        label="Best Performing Semester 🏆",
        value=f"{best_semester}",
        delta=f"{best_avg}",
        help="Semester with the highest mean CGPA."
    )

    # 2️⃣ CGPA Variation Across Semesters
    col2.metric(
        label="Semester CGPA Gap 📉",
        value=f"{sem_diff:.2f}",
        delta=f"{worst_semester} - {best_semester}",
        help="Difference between best and worst semester performance."
    )

    # 3️⃣ Best Preparation Time
    col3.metric(
        label="Top Preparation Time Category 📚",
        value=f"{best_prep}",
        delta=f"{best_prep_val}",
        help="Preparation habit associated with the highest mean CGPA."
    )

    # 4️⃣ Top Gaming Time Group
    col4.metric(
        label="Top Gaming Category 🎮",
        value=f"{best_gaming}",
        delta=f"{best_gaming_val}",
        help="Gaming frequency linked to the highest performance average."
    )

    st.caption(f"Overall Mean CGPA across all records: **{overall_mean:.2f}**")

st.markdown("---")  # Visual separation before charts
# =========================================================================

# --- 3A. Average Overall CGPA by Semester (Line Chart) ---
st.subheader("3.1. Average Overall CGPA Trend by Semester (Line Chart)")
if all(col in DF.columns for col in [COL_SEMESTER, COL_OVERALL, 'Semester_sort']):
    
    semester_overall = DF.groupby(COL_SEMESTER).agg(
        Mean_Overall=(COL_OVERALL, 'mean'),
        Sort_Order=('Semester_sort', 'mean')
    ).sort_values(by='Sort_Order').reset_index()

    fig_line = px.line(
        semester_overall, x=COL_SEMESTER, y='Mean_Overall',
        markers=True, title='Average Overall CGPA by Semester',
        template='plotly_white',
    )
    fig_line.update_traces(line=dict(color='orange', width=3))
    st.plotly_chart(fig_line, use_container_width=True)

st.markdown("---")

# --- 3B. Comparison of Mean Last Score and Mean Overall CGPA by Department (Dumbbell Plot) ---
st.subheader("3.2. Comparison of Mean Last Score and Mean Overall CGPA (Dumbbell Plot)")
if all(col in DF.columns for col in [COL_DEPARTMENT, COL_LAST, COL_OVERALL]):
    mean_scores_by_dept = DF.groupby(COL_DEPARTMENT)[[COL_LAST, COL_OVERALL]].mean().reset_index()
    mean_scores_by_dept = mean_scores_by_dept.sort_values(by=COL_OVERALL, ascending=True)

    fig_dumbbell = go.Figure()

    for index, row in mean_scores_by_dept.iterrows():
        fig_dumbbell.add_trace(go.Scatter(
            x=[row[COL_LAST], row[COL_OVERALL]], y=[row[COL_DEPARTMENT], row[COL_DEPARTMENT]],
            mode='lines', line=dict(color='gray', width=1), showlegend=False, hoverinfo='none' 
        ))

    fig_dumbbell.add_trace(go.Scatter(
        x=mean_scores_by_dept[COL_LAST], y=mean_scores_by_dept[COL_DEPARTMENT],
        mode='markers', marker=dict(color='blue', size=10), name='Mean Last Score'
    ))

    fig_dumbbell.add_trace(go.Scatter(
        x=mean_scores_by_dept[COL_OVERALL], y=mean_scores_by_dept[COL_DEPARTMENT],
        mode='markers', marker=dict(color='red', size=10), name='Mean Overall CGPA'
    ))

    fig_dumbbell.update_layout(
        title='Comparison of Mean Last Score and Mean Overall CGPA by Department',
        xaxis_title='Score', yaxis_title='Department', height=600,
        template='plotly_white'
    )
    st.plotly_chart(fig_dumbbell, use_container_width=True)

st.markdown("---")

# --- 3C. Mean Overall CGPA by Preparation and Gaming (Grouped Bar Chart) ---
st.subheader("3.3. Mean Overall CGPA by Preparation and Gaming")
if all(col in DF.columns for col in [COL_PREPARATION, COL_GAMING, COL_OVERALL]):
    
    prep_gaming_overall = DF.groupby([COL_PREPARATION, COL_GAMING], observed=True)[COL_OVERALL].mean().reset_index()

    fig_prep_gaming = px.bar(
        prep_gaming_overall, x=COL_PREPARATION, y=COL_OVERALL,
        color=COL_GAMING, barmode='group',
        category_orders={COL_PREPARATION: PREP_ORDER, COL_GAMING: GAMING_ORDER},
        title='Mean Overall CGPA by Preparation and Gaming Time',
        template='plotly_white'
    )
    fig_prep_gaming.update_xaxes(tickangle=45)
    st.plotly_chart(fig_prep_gaming, use_container_width=True)
