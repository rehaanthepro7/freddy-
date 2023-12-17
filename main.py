import streamlit as st
import matplotlib.pyplot as plt

# Set the page configuration with background color
st.set_page_config(
    page_title="Fredy the health advisor",
    page_icon="🤖🤖",
    layout="wide",
    initial_sidebar_state="expanded",  # Adjust as needed
    
)

# Add background color
def add_bg_from_local():
    st.markdown(
    f"""
    <style>
    .stApp {{
        background: rgb(2,0,36);
        background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(6,177,179,1) 35%, rgba(0,212,255,1) 100%);
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local()


# title
st.markdown(f"""
    <h1 style=color:white;text-align:center;margin-top:-20px>Freddy the health advisor</h1>
""",unsafe_allow_html=True)

c1,c2 = st.columns(2)
angel = plt.imread('angel.png')
with c1:
    st.image(angel)
    
evil = plt.imread('devil.png')
with c2:
    st.image(evil)



