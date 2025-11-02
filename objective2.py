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
# 📢 SUMMARY METRICS SECTION
# =========================================================================
st.subheader("📊 Summary of Key Demographic Insights")

if COL_OVERALL in DF.columns:
    avg_cgpa = DF[COL_OVERALL].mean().round(2)
    max_cgpa = DF[COL_OVERALL].max().round(2)
    min_cgpa = DF[COL_OVERALL].min().round(2)

    # Determine top performing gender
    if COL_GENDER in DF.columns:
        gender_avg = DF.groupby(COL_GENDER)[COL_OVERALL].mean()
        top_gender = gender_avg.idxmax()
        top_gender_val = gender_avg.max().round(2)
    else:
        top_gender, top_gender_val = "N/A", 0

    # Determine top performing income group
    if COL_INCOME in DF.columns:
        income_avg = DF.groupby(COL_INCOME)[COL_OVERALL].mean()
        top_income = income_avg.idxmax()
        top_income_val = income_avg.max().round(2)
    else:
        top_income, top_income_val = "N/A", 0

    # Layout
    col1, col2, col3, col4 = st.columns(4)

    # 1️⃣ Average CGPA
    col1.metric(
        label="Average CGPA 🎓",
        value=f"{avg_cgpa:.2f}",
        delta=f"Range: {min_cgpa} - {max_cgpa}",
        help="Shows the mean overall CGPA with its range."
    )

    # 2️⃣ Top Performing Gender
    col2.metric(
        label="Top Performing Gender 🚻",
        value=f"{top_gender}",
        delta=f"{top_gender_val}",
        help="Gender group with the highest average CGPA."
    )

    # 3️⃣ Top Performing Income Group
    col3.metric(
        label="Top Performing Income Group 💰",
        value=f"{top_income}",
        delta=f"{top_income_val}",
        help="Income level with the highest average CGPA."
    )

    # 4️⃣ CGPA Variation (Diversity)
    cgpa_std = DF[COL_OVERALL].std().round(2)
    variation_status = (
        "🔹 High Variation" if cgpa_std > 0.5 else "🔸 Moderate" if cgpa_std > 0.3 else "🟢 Consistent"
    )
    col4.metric(
        label="CGPA Variation 📈",
        value=f"{cgpa_std}",
        delta=variation_status,
        help="Represents consistency of student performance across groups."
    )

st.markdown("---")  # Visual separation before the charts
# =========================================================================

# --- 2A. Average Overall CGPA by Department and Gender (Grouped Bar Chart) ---
st.subheader("A. Average Overall CGPA by Department and Gender")
if all(col in DF.columns for col in [COL_DEPARTMENT, COL_GENDER, COL_OVERALL]):
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
