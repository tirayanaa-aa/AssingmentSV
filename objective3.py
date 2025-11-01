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
    st.warning("Data is not available. Check the Visualisasi Ilmiah page for data status.")
    st.stop()


# --- 3A. Average Overall CGPA by Semester (Line Chart) ---
st.subheader("A. Average Overall CGPA Trend by Semester (Line Chart)")
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
st.subheader("B. Comparison of Mean Last Score and Mean Overall CGPA (Dumbbell Plot)")
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
st.subheader("C. Mean Overall CGPA by Preparation and Gaming")
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
