import streamlit as st
from utils import DF # Import DF to check data status

# --- Page Content ---
st.title("🔬 Introduction to Scientific Visualization")
st.header("Student Performance Metrics Dashboard", divider="blue")

# Add a banner image at the top
banner_image_1 = 'https://images.unsplash.com/photo-1571260899304-425eee4c7efc?auto=format&fit=crop&w=1200&q=60' 
st.image(banner_image_1, use_container_width=True)

st.write(
    """
    ***Scientific Visualization*** is a multidisciplinary field that focuses on transforming complex scientific data into visual forms that are easier to understand, interpret, and communicate. 
    Through the use of computational techniques, visualization helps researchers explore datasets, identify hidden patterns, and gain insights that would otherwise remain obscure in numerical form.
    """
)

banner_image_2 = 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&w=1200&q=60' 
st.image(banner_image_2, use_container_width=True)

st.markdown("""
### 🧠 Why Student Performance Metrics Matter
Scientific visualization bridges data and decision-making by transforming raw performance data  
into **actionable insights**. Through data analytics, we can:
- Correlate habits with academic results  
- Track improvement patterns across semesters  
- Support data-driven decisions for student success  
""")

# --- Banner 3: Graduation Success ---
st.image(
    "https://images.unsplash.com/photo-1558021211-51b6ecfa0db9?auto=format&fit=crop&w=1200&q=60",
    use_container_width=True,
    caption="Empowering Students Toward Academic Success"
)

st.markdown("""
### 🏆 Project Goals
- Encourage **data-informed learning strategies**  
- Support **continuous performance monitoring**  
- Enhance **student engagement and outcomes**

> “Data is not just numbers — it’s the story of student growth.”
""")

st.markdown("---")
st.markdown("© 2025 Student Performance Metrics Dashboard | Faculty of Data Science, UMK")
