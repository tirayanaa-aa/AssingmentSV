import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------- CONFIG -----------------
st.set_page_config(page_title="Objective 2 - Demographics", layout="wide")

DATA_URL = 'https://raw.githubusercontent.com/tirayanaa-aa/AssingmentSV/refs/heads/main/processed_data.csv'

COL_DEPARTMENT = 'Department'
COL_GENDER = 'Gender'
COL_OVERALL = 'Overall'
COL_HOMETOWN = 'Hometown'
COL_INCOME = 'Income'

# ----------------- LOAD DATA -----------------
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    df[COL_OVERALL] = pd.to_numeric(df[COL_OVERALL], errors='coerce')
    return df

df = load_data(DATA_URL)

# ----------------- CONTENT -----------------
st.header("👥 Objective 2: Demographic & Socioeconomic Factors")
st.markdown("Analyze how demographic and socioeconomic variables influence students’ overall performance.")

# A. Grouped Bar - Department & Gender
st.subheader("A. Average Overall CGPA by Department and Gender")
dept_gender = df.groupby([COL_DEPARTMENT, COL_GENDER])[COL_OVERALL].mean().reset_index()
fig_bar = px.bar(dept_gender, x=COL_DEPARTMENT, y=COL_OVERALL, color=COL_GENDER,
                 barmode='group', title="Average Overall CGPA by Department and Gender",
                 template='plotly_white')
fig_bar.update_xaxes(tickangle=45)
st.plotly_chart(fig_bar, use_container_width=True)

# B. Violin - Hometown
st.subheader("B. CGPA Distribution by Hometown (Violin Plot)")
fig_violin = px.violin(df, x=COL_HOMETOWN, y=COL_OVERALL, box=True, points="all",
                       title="Overall CGPA Distribution by Hometown", template='plotly_white')
st.plotly_chart(fig_violin, use_container_width=True)

# C. Box - Income
st.subheader("C. CGPA Distribution by Income Level (Box Plot)")
income_order = ['Low (Below 15,000)', 'Lower middle (15,000-30,000)',
                'Upper middle (30,000-50,000)', 'High (Above 50,000)']
fig_box = px.box(df, x=COL_INCOME, y=COL_OVERALL,
                 category_orders={COL_INCOME: income_order},
                 title="Overall CGPA Distribution by Income Level", template='plotly_white')
fig_box.update_xaxes(tickangle=45)
st.plotly_chart(fig_box, use_container_width=True)
