import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from collections import OrderedDict

st.title("⏱️ Objective 3: Temporal & Habit Interaction")

# --- Load Data ---
DATA_URL = 'https://raw.githubusercontent.com/tirayanaa-aa/AssingmentSV/refs/heads/main/processed_data.csv'

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    
    # Convert numeric columns
    for col in ["HSC", "SSC", "Last", "Overall"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    
    # Extract semester number for sorting
    if "Semester" in df.columns:
        df["Semester_sort"] = df["Semester"].str.extract(r"(\d+)").astype(float)
    
    prep_order = ['0-1 Hour', '1-2 Hours', '2-3 Hours', 'More than 3 Hours']
    gaming_order = ['0-1 Hour', '1-2 Hours', '2-3 Hours', 'More than 3 Hours']
    df["Preparation"] = pd.Categorical(df["Preparation"], categories=prep_order, ordered=True)
    df["Gaming"] = pd.Categorical(df["Gaming"], categories=gaming_order, ordered=True)
    
    return df

df = load_data(DATA_URL)
st.dataframe(df.head())

# ===================================================================
# 3A. Average Overall CGPA by Semester (Line Chart)
# ===================================================================
st.subheader("A. Average Overall CGPA Trend by Semester (Line Chart)")

if all(col in df.columns for col in ["Semester", "Overall", "Semester_sort"]):
    semester_overall = (
        df.groupby("Semester")
        .agg(Mean_Overall=("Overall", "mean"), Sort_Order=("Semester_sort", "mean"))
        .sort_values(by="Sort_Order")
        .reset_index()
    )
    
    fig_line = px.line(
        semester_overall,
        x="Semester", y="Mean_Overall",
        markers=True,
        title="Average Overall CGPA by Semester",
        template="plotly_white",
    )
    fig_line.update_traces(line=dict(color="orange", width=3))
    fig_line.update_layout(yaxis_title="Average Overall CGPA")
    st.plotly_chart(fig_line, use_container_width=True)

# ===================================================================
# 3B. Mean Last Score vs. Mean Overall CGPA by Department (Dumbbell Plot)
# ===================================================================
st.subheader("B. Comparison of Mean Last Score and Mean Overall CGPA by Department (Dumbbell Plot)")

if all(col in df.columns for col in ["Department", "Last", "Overall"]):
    mean_scores = df.groupby("Department")[["Last", "Overall"]].mean().reset_index()
    mean_scores = mean_scores.sort_values(by="Overall", ascending=True)

    fig_dumbbell = go.Figure()

    # Connecting lines
    for _, row in mean_scores.iterrows():
        fig_dumbbell.add_trace(go.Scatter(
            x=[row["Last"], row["Overall"]],
            y=[row["Department"], row["Department"]],
            mode="lines",
            line=dict(color="gray", width=1),
            showlegend=False
        ))

    # Markers for Last Score
    fig_dumbbell.add_trace(go.Scatter(
        x=mean_scores["Last"],
        y=mean_scores["Department"],
        mode="markers",
        marker=dict(color="blue", size=10),
        name="Mean Last Score"
    ))

    # Markers for Overall CGPA
    fig_dumbbell.add_trace(go.Scatter(
        x=mean_scores["Overall"],
        y=mean_scores["Department"],
        mode="markers",
        marker=dict(color="red", size=10),
        name="Mean Overall CGPA"
    ))

    fig_dumbbell.update_layout(
        title="Comparison of Mean Last Score and Overall CGPA by Department",
        xaxis_title="Score",
        yaxis_title="Department",
        height=600,
        template="plotly_white"
    )
    st.plotly_chart(fig_dumbbell, use_container_width=True)

# ===================================================================
# 3C. Mean Overall CGPA by Preparation and Gaming (Grouped Bar Chart)
# ===================================================================
st.subheader("C. Mean Overall CGPA by Preparation and Gaming (Grouped Bar Chart)")

if all(col in df.columns for col in ["Preparation", "Gaming", "Overall"]):
    prep_gaming = (
        df.groupby(["Preparation", "Gaming"], observed=True)["Overall"]
        .mean()
        .reset_index()
    )

    fig_bar = px.bar(
        prep_gaming,
        x="Preparation",
        y="Overall",
        color="Gaming",
        barmode="group",
        category_orders={
            "Preparation": ['0-1 Hour', '1-2 Hours', '2-3 Hours', 'More than 3 Hours'],
            "Gaming": ['0-1 Hour', '1-2 Hours', '2-3 Hours', 'More than 3 Hours'],
        },
        title="Mean Overall CGPA by Preparation and Gaming",
        template="plotly_white"
    )
    fig_bar.update_xaxes(tickangle=45)
    fig_bar.update_layout(yaxis_title="Average Overall CGPA")
    st.plotly_chart(fig_bar, use_container_width=True)

