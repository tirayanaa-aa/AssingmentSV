import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Analysis of Students’ Satisfaction with Online Learning During COVID-19")

# Load CSV from GitHub
url = "https://raw.githubusercontent.com/tirayanaa-aa/AssingmentSV/refs/heads/main/processed_data.csv"

# Read the dataset
df = pd.read_csv(url)
