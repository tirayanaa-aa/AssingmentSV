import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Prior Academic Standing and Study Habits")

# Load CSV from GitHub
url = "https://https://raw.githubusercontent.com/tirayanaa-aa/AssingmentSV/refs/heads/main/processed_data.csv"

# Read the dataset
df = pd.read_csv(url)
