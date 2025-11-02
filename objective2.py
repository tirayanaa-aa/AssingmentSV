import streamlit as st
import plotly.express as px
from utils import DF, COL_DEPARTMENT, COL_GENDER, COL_OVERALL, COL_HOMETOWN, COL_INCOME

# --- Page Setup ---
st.title("👤 Objective 2: Demographic & Socioeconomic Factors")
st.header("Analyzing performance variations across different demographic and socioeconomic groups.", divider="red")

if DF.empty:
    st.warning("Data is not available. Check the homepage for data status.")
    st.stop()

# =========================================================================
# 📢 SUMMARY METRICS SECTION: INSERT HERE
# =========================================================================
st.subheader("Key Demographic Insights")

col_kpi1, col_kpi2, col_kpi3 = st.columns(3)

# 1. Highest Average CGPA Group (by Gender)
if COL_GENDER in DF.columns and COL_OVERALL in DF.columns:
    gender_avg = DF.groupby(COL_GENDER)[COL_OVERALL].mean()
    top_gender = gender_avg.idxmax()
    top_avg = gender_avg.max().round(2)
    col_kpi1.metric(
        label="Highest Average CGPA (Gender)",
        value=f"{top_gender} ({top_avg:.2f})"
    )

# 2. CGPA Range
if COL_OVERALL in DF.columns:
    cgpa_range = (DF[COL_OVERALL].max() - DF[COL_OVERALL].min()).round(2)
    col_kpi2.metric(
        label="Overall CGPA Range", 
        value=f"{cgpa_range:.2f}"
    )

# 3. Most Diverse Hometown (Highest Standard Deviation)
if COL_HOMETOWN in DF.columns and COL_OVERALL in DF.columns:
    # Ensure there are enough unique values for std calculation
    if DF[COL_HOMETOWN].nunique() > 1:
        hometown_std = DF.groupby(COL_HOMETOWN)[COL_OVERALL].std()
        most_diverse_hometown = hometown_std.idxmax()
        col_kpi3.metric(
            label="Hometown with Most Diverse Scores (High Std Dev)", 
            value=f"{most_diverse_hometown}"
        )
    
st.markdown("---") # Visual separation before the charts begin
# =========================================================================

# --- 2A. Average Overall CGPA by Department and Gender (Grouped Bar Chart) ---
st.subheader("A. Average Overall CGPA by Department and Gender")
if all(col in DF.columns for col in [COL_DEPARTMENT, COL_GENDER, COL_OVERALL]):
# ... (rest of the original code follows) ...
    dept_gender_overall = DF.groupby([COL_DEPARTMENT, COL_GENDER])[COL_OVERALL].mean().reset_index()

    fig_bar_dept_gender = px.bar(
        dept_gender_overall, x=COL_DEPARTMENT, y=COL_OVERALL, 
        color=COL_GENDER, barmode='group',
        title='Average Overall CGPA by Department and Gender',
        template='plotly_white',
    )
    fig_bar_dept_gender.update_xaxes(tickangle=45)
    st.plotly_chart(fig_bar_dept_gender, use_container_width=True)

st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    # --- 2B. Overall CGPA Distribution by Hometown (Violin Plot) ---
    st.subheader("B. Overall CGPA Distribution by Hometown (Violin)")
    if all(col in DF.columns for col in [COL_HOMETOWN, COL_OVERALL]):
        fig_violin = px.violin(
            DF, x=COL_HOMETOWN, y=COL_OVERALL,
            box=True, points="all",
            title='Overall CGPA Distribution by Hometown',
            template='plotly_white'
        )
        st.plotly_chart(fig_violin, use_container_width=True)

with col4:
    # --- 2C. Overall CGPA Distribution by Income Level (Box Plot) ---
    st.subheader("C. Overall CGPA Distribution by Income Level (Box)")
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
