import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from collections import OrderedDict

# --- Configuration ---
st.set_page_config(
    page_title="Student Performance Metrics",
    layout="wide"
)

# --- Constants ---
# Using the URL specified in your request
DATA_URL = 'https://raw.githubusercontent.com/tirayanaa-aa/AssingmentSV/refs/heads/main/processed_data.csv'

# Define columns (based on your input code)
COL_HSC = 'HSC'
COL_SSC = 'SSC'
COL_LAST = 'Last'
COL_OVERALL = 'Overall'
COL_PREPARATION = 'Preparation'
COL_ATTENDANCE = 'Attendance'
COL_GENDER = 'Gender'
COL_DEPARTMENT = 'Department'
COL_HOMETOWN = 'Hometown'
COL_INCOME = 'Income'
COL_SEMESTER = 'Semester'
COL_GAMING = 'Gaming'

# Categorical orderings for plotting consistency
ATTENDANCE_ORDER = ['0%-19%', '20%-39%', 'Below 40%', '40%-59%', '60%-79%', '80%-100%']
PREP_ORDER = ['0-1 Hour', '1-2 Hours', '2-3 Hours', 'More than 3 Hours']
GAMING_ORDER = ['0-1 Hour', '1-2 Hours', '2-3 Hours', 'More than 3 Hours']

# --- Data Loading and Caching ---

@st.cache_data
def load_data(url):
    """
    Loads the dataset, performs necessary type conversions, and creates
    numerical versions of categorical variables needed for correlation.
    """
    try:
        df = pd.read_csv(url)
        
        # 1. Ensure core academic columns are numeric
        required_cols = [COL_HSC, COL_SSC, COL_LAST, COL_OVERALL]
        for col in required_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')

        # 2. Create numerical mapping for Preparation (for Correlation Matrix)
        preparation_mapping = OrderedDict(zip(PREP_ORDER, [0.5, 1.5, 2.5, 3.5]))
        if COL_PREPARATION in df.columns:
            df['Preparation_numeric'] = df[COL_PREPARATION].map(preparation_mapping)
        
        # 3. Create numerical mapping for Attendance (for Correlation Matrix)
        attendance_mapping = OrderedDict(zip(ATTENDANCE_ORDER, [10, 30, 30, 50, 70, 90]))
        # Note: Added 'Below 40%' to mapping; will use the 0%-19% and 20%-39% if available.
        if COL_ATTENDANCE in df.columns:
             df['Attendance_numeric'] = df[COL_ATTENDANCE].map(attendance_mapping)
             # Ensure the categorical order is set for plotting later
             df[COL_ATTENDANCE] = pd.Categorical(df[COL_ATTENDANCE], categories=[c for c in ATTENDANCE_ORDER if c in df[COL_ATTENDANCE].unique()], ordered=True)

        # 4. Handle Semester column for line plot ordering
        if COL_SEMESTER in df.columns:
            # Simple conversion that works for '1st', '2nd', etc.
            df['Semester_sort'] = df[COL_SEMESTER].str.extract('(\d+)').astype(float)
        
        # Drop rows missing values in the primary performance columns
        df.dropna(subset=[COL_HSC, COL_LAST, COL_OVERALL], inplace=True)

        st.success(f"Successfully loaded and pre-processed {len(df)} rows.")
        return df
    except Exception as e:
        st.error(f"Error loading or processing data from URL: {e}")
        return pd.DataFrame()

# Load the data
df = load_data(DATA_URL)

# --- Streamlit Application Content ---

st.title("📊 Student Performance Metrics Dashboard")
st.markdown("This dashboard converts a suite of Matplotlib/Seaborn plots into interactive Plotly visualizations, organized by objective.")

if df.empty:
    st.warning("Cannot proceed as the DataFrame is empty or failed to load.")
    st.stop()

# 1. Data Preview
st.subheader("Data Overview")
st.dataframe(df, use_container_width=True)

st.divider()

# ====================================================================
# OBJECTIVE 1: PRIOR ACADEMIC & HABITS (Scatter, Heatmap, Bar Plot)
# ====================================================================
st.header("VISUALIZATION OBJECTIVE 1", divider="blue")

col1, col2 = st.columns(2)

with col1:
    # --- 1A. Scatter Plot: Last Score vs. HSC Score ---
    st.subheader("A. Last Score vs. HSC Score (Scatter)")
    if all(col in df.columns for col in [COL_HSC, COL_LAST]):
        fig_scatter = px.scatter(
            df,
            x=COL_HSC,
            y=COL_LAST,
            color=COL_GENDER if COL_GENDER in df.columns else None,
            title="Last Semester Score vs. Higher Secondary Score (HSC)",
            labels={COL_HSC: 'HSC Score', COL_LAST: 'Last Score'},
            template='plotly_white'
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

with col2:
    # --- 1B. Mean Overall CGPA by Attendance (Bar Chart) ---
    st.subheader("B. Mean Overall CGPA by Attendance (Bar Chart)")
    if COL_ATTENDANCE in df.columns and COL_OVERALL in df.columns:
        # Calculate mean, using the categorical order set in load_data
        mean_overall_by_attendance = df.groupby(COL_ATTENDANCE, observed=True)[COL_OVERALL].mean().reset_index()
        mean_overall_by_attendance.columns = [COL_ATTENDANCE, 'Mean Overall CGPA']

        fig_bar = px.bar(
            mean_overall_by_attendance,
            x=COL_ATTENDANCE,
            y='Mean Overall CGPA',
            color='Mean Overall CGPA',
            color_continuous_scale=px.colors.sequential.Viridis,
            text='Mean Overall CGPA',
            title='Mean Overall CGPA by Class Attendance Level',
            category_orders={COL_ATTENDANCE: mean_overall_by_attendance[COL_ATTENDANCE].cat.categories.tolist()}
        )
        fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        fig_bar.update_layout(yaxis_title="Mean Overall CGPA")
        st.plotly_chart(fig_bar, use_container_width=True)


# --- 1C. Correlation Matrix Heatmap ---
st.subheader("C. Correlation Matrix of Key Numerical Variables (Heatmap)")
numerical_cols_corr = [COL_HSC, COL_SSC, 'Preparation_numeric', 'Attendance_numeric', COL_LAST, COL_OVERALL]
available_cols_corr = [col for col in numerical_cols_corr if col in df.columns]

if len(available_cols_corr) >= 2:
    correlation_matrix = df[available_cols_corr].corr().round(2)

    fig_corr = go.Figure(data=go.Heatmap(
        z=correlation_matrix.values,
        x=correlation_matrix.columns,
        y=correlation_matrix.index,
        colorscale='RdBu', 
        zmin=-1, 
        zmax=1,
        text=correlation_matrix.values,
        texttemplate="%{text}",
        textfont={"size": 10}
    ))

    fig_corr.update_layout(
        title='Correlation Matrix of Academic and Habit Variables',
        yaxis=dict(autorange="reversed"),
        height=600
    )
    st.plotly_chart(fig_corr, use_container_width=True)


st.divider()

# ====================================================================
# OBJECTIVE 2: DEMOGRAPHIC & SOCIOECONOMIC (Bar, Violin, Box)
# ====================================================================
st.header("VISUALIZATION OBJECTIVE 2", divider="red")

# --- 2A. Average Overall CGPA by Department and Gender (Grouped Bar Chart) ---
st.subheader("A. Average Overall CGPA by Department and Gender")
if all(col in df.columns for col in [COL_DEPARTMENT, COL_GENDER, COL_OVERALL]):
    dept_gender_overall = df.groupby([COL_DEPARTMENT, COL_GENDER])[COL_OVERALL].mean().reset_index()

    fig_bar_dept_gender = px.bar(
        dept_gender_overall,
        x=COL_DEPARTMENT,
        y=COL_OVERALL,
        color=COL_GENDER,
        barmode='group',
        title='Average Overall CGPA by Department and Gender',
        template='plotly_white',
    )
    fig_bar_dept_gender.update_xaxes(tickangle=45)
    st.plotly_chart(fig_bar_dept_gender, use_container_width=True)


col3, col4 = st.columns(2)

with col3:
    # --- 2B. Overall CGPA Distribution by Hometown (Violin Plot) ---
    st.subheader("B. Overall CGPA Distribution by Hometown (Violin)")
    if all(col in df.columns for col in [COL_HOMETOWN, COL_OVERALL]):
        fig_violin = px.violin(
            df,
            x=COL_HOMETOWN,
            y=COL_OVERALL,
            box=True, # Show box plot inside the violin
            points="all", # Show all points
            title='Overall CGPA Distribution by Hometown',
            template='plotly_white'
        )
        st.plotly_chart(fig_violin, use_container_width=True)

with col4:
    # --- 2C. Overall CGPA Distribution by Income Level (Box Plot) ---
    st.subheader("C. Overall CGPA Distribution by Income Level (Box)")
    if all(col in df.columns for col in [COL_INCOME, COL_OVERALL]):
        # Custom order for Income
        income_order = [
            'Low (Below 15,000)', 
            'Lower middle (15,000-30,000)', 
            'Upper middle (30,000-50,000)', 
            'High (Above 50,000)'
        ]
        
        fig_box = px.box(
            df,
            x=COL_INCOME,
            y=COL_OVERALL,
            category_orders={COL_INCOME: income_order},
            title='Overall CGPA Distribution by Income Level',
            template='plotly_white'
        )
        fig_box.update_xaxes(tickangle=45)
        st.plotly_chart(fig_box, use_container_width=True)

st.divider()

# ====================================================================
# OBJECTIVE 3: TEMPORAL & HABIT INTERACTION (Line, Dumbbell, Grouped Bar)
# ====================================================================
st.header("VISUALIZATION OBJECTIVE 3", divider="green")

# --- 3A. Average Overall CGPA by Semester (Line Chart) ---
st.subheader("A. Average Overall CGPA Trend by Semester (Line Chart)")
if all(col in df.columns for col in [COL_SEMESTER, COL_OVERALL, 'Semester_sort']):
    
    # Group and sort by the numeric semester column
    semester_overall = df.groupby(COL_SEMESTER).agg(
        Mean_Overall=(COL_OVERALL, 'mean'),
        Sort_Order=('Semester_sort', 'mean')
    ).sort_values(by='Sort_Order').reset_index()

    fig_line = px.line(
        semester_overall,
        x=COL_SEMESTER,
        y='Mean_Overall',
        markers=True,
        title='Average Overall CGPA by Semester',
        template='plotly_white',
    )
    fig_line.update_traces(line=dict(color='orange', width=3))
    fig_line.update_layout(yaxis_title="Average Overall CGPA")
    st.plotly_chart(fig_line, use_container_width=True)


# --- 3B. Comparison of Mean Last Score and Mean Overall CGPA by Department (Dumbbell Plot) ---
st.subheader("B. Comparison of Mean Last Score and Mean Overall CGPA (Dumbbell Plot)")
if all(col in df.columns for col in [COL_DEPARTMENT, COL_LAST, COL_OVERALL]):
    mean_scores_by_dept = df.groupby(COL_DEPARTMENT)[[COL_LAST, COL_OVERALL]].mean().reset_index()
    # Sort by mean Overall score
    mean_scores_by_dept = mean_scores_by_dept.sort_values(by=COL_OVERALL, ascending=True)

    # Plotly Dumbbell Plot creation using go.Scatter
    fig_dumbbell = go.Figure()

    # Add lines (connecting the dots)
    for index, row in mean_scores_by_dept.iterrows():
        fig_dumbbell.add_trace(go.Scatter(
            x=[row[COL_LAST], row[COL_OVERALL]],
            y=[row[COL_DEPARTMENT], row[COL_DEPARTMENT]],
            mode='lines',
            line=dict(color='gray', width=1),
            showlegend=False
        ))

    # Add markers for Last Score
    fig_dumbbell.add_trace(go.Scatter(
        x=mean_scores_by_dept[COL_LAST],
        y=mean_scores_by_dept[COL_DEPARTMENT],
        mode='markers',
        marker=dict(color='blue', size=10),
        name='Mean Last Score'
    ))

    # Add markers for Overall CGPA
    fig_dumbbell.add_trace(go.Scatter(
        x=mean_scores_by_dept[COL_OVERALL],
        y=mean_scores_by_dept[COL_DEPARTMENT],
        mode='markers',
        marker=dict(color='red', size=10),
        name='Mean Overall CGPA'
    ))

    fig_dumbbell.update_layout(
        title='Comparison of Mean Last Score and Mean Overall CGPA by Department',
        xaxis_title='Score',
        yaxis_title='Department',
        height=600,
        template='plotly_white'
    )
    st.plotly_chart(fig_dumbbell, use_container_width=True)


# --- 3C. Mean Overall CGPA by Preparation and Gaming (Grouped Bar Chart) ---
st.subheader("C. Mean Overall CGPA by Preparation and Gaming")
if all(col in df.columns for col in [COL_PREPARATION, COL_GAMING, COL_OVERALL]):
    
    # Calculate average Overall CGPA by Preparation and Gaming
    prep_gaming_overall = df.groupby([COL_PREPARATION, COL_GAMING], observed=True)[COL_OVERALL].mean().reset_index()

    # Create the grouped bar chart
    fig_prep_gaming = px.bar(
        prep_gaming_overall,
        x=COL_PREPARATION,
        y=COL_OVERALL,
        color=COL_GAMING,
        barmode='group',
        category_orders={
            COL_PREPARATION: PREP_ORDER,
            COL_GAMING: GAMING_ORDER
        },
        title='Mean Overall CGPA by Preparation and Gaming Time',
        template='plotly_white'
    )
    fig_prep_gaming.update_xaxes(tickangle=45)
    fig_prep_gaming.update_layout(yaxis_title="Average Overall CGPA")
    st.plotly_chart(fig_prep_gaming, use_container_width=True)
