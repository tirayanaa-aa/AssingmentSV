import streamlit as st
import plotly.express as px
from utils import DF, COL_DEPARTMENT, COL_GENDER, COL_OVERALL, COL_HOMETOWN, COL_INCOME

# --- Page Setup ---
st.title("👤 Objective 2: Demographic & Socioeconomic Factors")
st.header("Analyzing performance variations across different demographic and socioeconomic groups.", divider="red")

if DF.empty:
    st.warning("Data is not available. Please check the main application script.")
    st.stop()


# --- 2A. Average Overall CGPA by Department and Gender (Grouped Bar Chart) ---
st.subheader("A. Average Overall CGPA by Department and Gender")
if all(col in DF.columns for col in [COL_DEPARTMENT, COL_GENDER, COL_OVERALL]):
    dept_gender_overall = DF.groupby([COL_DEPARTMENT, COL_GENDER])[COL_OVERALL].mean().reset_index()

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

st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    # --- 2B. Overall CGPA Distribution by Hometown (Violin Plot) ---
    st.subheader("B. Overall CGPA Distribution by Hometown (Violin)")
    if all(col in DF.columns for col in [COL_HOMETOWN, COL_OVERALL]):
        fig_violin = px.violin(
            DF,
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
    if all(col in DF.columns for col in [COL_INCOME, COL_OVERALL]):
        # Custom order for Income
        income_order = [
            'Low (Below 15,000)', 
            'Lower middle (15,000-30,000)', 
            'Upper middle (30,000-50,000)', 
            'High (Above 50,000)'
        ]
        
        # Filter income_order to only include categories present in the data to avoid Plotly errors
        valid_income_order = [inc for inc in income_order if inc in DF[COL_INCOME].unique()]

        fig_box = px.box(
            DF,
            x=COL_INCOME,
            y=COL_OVERALL,
            category_orders={COL_INCOME: valid_income_order},
            title='Overall CGPA Distribution by Income Level',
            template='plotly_white'
        )
        fig_box.update_xaxes(tickangle=45)
        st.plotly_chart(fig_box, use_container_width=True)
