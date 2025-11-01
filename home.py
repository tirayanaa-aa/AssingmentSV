import streamlit as st
from utils import DF  # Import DF to check data status

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
Understanding student performance through data visualization provides valuable insights into academic achievement, learning behaviors, and participation trends.  
With effective visual tools, educators and decision-makers can identify performance gaps, monitor progress, and design interventions that truly make an impact.  
This dashboard serves as a bridge between data and meaningful academic improvement by transforming raw performance data into **clear, actionable insights**.
""")

# --- Banner 3: Graduation Success ---
st.image(
    "https://images.unsplash.com/photo-1523580846011-d3a5bc25702b?auto=format&fit=crop&w=1200&q=60",
    use_container_width=True,
    caption="Empowering Students Toward Academic Success"
)

st.markdown("""
### 🏆 Project Goals
- Encourage **data-informed learning strategies** to help students understand and improve their performance  
- Support **continuous performance monitoring** across semesters to track academic growth  
- Enhance **student engagement** through transparent, visual, and evidence-based analytics  
- Provide educators with tools to make **targeted interventions** for better student outcomes  
- Foster a culture of **accountability, motivation, and progress** in learning environments  
""")

st.info("""
This dashboard empowers both students and educators to explore performance data interactively.  
By identifying trends and correlations, it aims to **enhance learning outcomes** and promote **academic excellence** within the institution.
""")
