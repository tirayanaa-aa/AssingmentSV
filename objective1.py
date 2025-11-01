import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from collections import OrderedDict

# ----------------- CONFIG -----------------
st.set_page_config(page_title="Objective 1 - Academic & Habits", layout="wide")

DATA_URL = 'https://raw.githubusercontent.com/tirayanaa-aa/AssingmentSV/refs/heads/main/processed_data.csv'

COL_HSC = 'HSC'
COL_SSC = 'SSC'
COL_LAST = 'Last'
COL_OVERALL = 'Overall'
COL_PREPARATION = 'Preparation'
COL_ATTENDANCE = 'Attendance'
COL_GENDER = 'Gender'

ATTENDANCE_ORDER = ['0%-19%', '20%-39%', 'Below 40%', '40%-59%', '60%-79%', '80%-100%']
PREP_ORDER = ['0-1 Hour', '1-2 Hours', '2-3 Hours', 'More than 3 Hours']

# ----------------- LOAD DATA -----------------
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    df[COL_HSC] = pd.to_numeric(df[COL_HSC], errors='coerce')
    df[COL_LAST] = pd.to_numeric(df[COL_LAST], errors='coerce')
    df[COL_OVERALL] = pd.to_numeric(df[COL_OVERALL], errors='coerce')

    prep_map = OrderedDict(zip(PREP_ORDER, [0.5, 1.5, 2.5, 3.5]))
    df['Preparation_numeric'] = df[COL_PREPARATION].map(prep_map)

    attend_map = OrderedDict(zip(ATTENDANCE_ORDER, [10, 30, 40, 50, 70, 90]))
    df['Attendance_numeric'] = df[COL_ATTENDANCE].map(attend_map)

    df[COL_ATTENDANCE] = pd.Categorical(df[COL_ATTENDANCE],
                                        categories=[c for c in ATTENDANCE_ORDER if c in df[COL_ATTENDANCE].unique()],
                                        ordered=True)
    return df

df = load_data(DATA_URL)

# ----------------- CONTENT -----------------
st.header("🎯 Objective 1: Prior Academic & Habits")
st.markdown("This section explores how students’ past academic records and study habits affect their performance.")

# A. Scatter Plot
st.subheader("A. Last Score vs. HSC Score (Scatter)")
fig_scatter = px.scatter(df, x=COL_HSC, y=COL_LAST, color=COL_GENDER,
                         title="Last Semester Score vs. HSC Score", template='plotly_white')
st.plotly_chart(fig_scatter, use_container_width=True)

# B. Bar Chart - Attendance
st.subheader("B. Mean Overall CGPA by Attendance")
mean_by_attendance = df.groupby(COL_ATTENDANCE, observed=True)[COL_OVERALL].mean().reset_index()
fig_bar = px.bar(mean_by_attendance, x=COL_ATTENDANCE, y=COL_OVERALL,
                 color=COL_OVERALL, text=COL_OVERALL,
                 color_continuous_scale=px.colors.sequential.Viridis,
                 title="Mean Overall CGPA by Attendance Level")
fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
st.plotly_chart(fig_bar, use_container_width=True)

# C. Correlation Heatmap
st.subheader("C. Correlation Matrix (Heatmap)")
num_cols = [COL_HSC, COL_SSC, 'Preparation_numeric', 'Attendance_numeric', COL_LAST, COL_OVERALL]
corr = df[num_cols].corr().round(2)
fig_corr = go.Figure(data=go.Heatmap(
    z=corr.values, x=corr.columns, y=corr.columns, colorscale='RdBu', zmin=-1, zmax=1,
    text=corr.values, texttemplate="%{text}"
))
fig_corr.update_layout(title="Correlation of Academic and Habit Variables", yaxis=dict(autorange="reversed"))
st.plotly_chart(fig_corr, use_container_width=True)
