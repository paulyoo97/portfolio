import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# Theming
# https://blog.streamlit.io/introducing-theming/
# https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="About", page_icon="", layout="wide")    # layout by default is centered.

st.sidebar.success("Select a page above.")

# LottieFiles Animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

animation = load_lottieurl("https://lottie.host/208766c7-98f3-4113-97e5-192440721b84/Huba2FYU5Q.json")
# https://lottie.host/208766c7-98f3-4113-97e5-192440721b84/Huba2FYU5Q.json
# https://lottie.host/50b0997f-9610-4e67-9652-e1f1f50d4ec7/W2uGG3C7E6.json

# Header section
with st.container():
    st.subheader("Hi, I'm Paul \U0001f30a")
    st.title("An Operations Engineer currently working in the IT industry")
    st.write(
        """
        *I'm passionate about mechanical engineering and data analytics.*        
        """)


# What I do
with st.container():
    st.write("---")
    left, right = st.columns(2)
    with left:
        st.header("My Current Job")
        st.write(
            """
            I'm currently working in the IT industry as an Operations Engineer at Andorix Inc. \n
            At my job, I work in the Data Protection & IoT Team to: \n
            - Create and manage automated processes using Python
            - Provide Data Management as a Service utilizing CommVault and Acronis Cloud Backup
            - Offer technical support and server deployment for clients in collaboration with the Infrastructure, Operations, and Project Management Teams
            """
        )
    with right:
        st_lottie(animation, height=300, key="coding")

# Education
with st.container():
    st.write('---')
    st.header("Education")
    st.write(
        """
        #### University of Waterloo
        *Data Science Certificate* || Present \n
        - **Courses:** Foundations of Data Science, Statistics
        """)
    st.write(
        """
        #### McMaster University \n
        *Bachelor of Engineering, Mechanical Engineering Co-op* || 2022 \n
        - **Final Year GPA:** 3.4 out of 4.0
        - **Mechanical Engineering Courses:** Robotics, Control Systems, Mechanical Vibration, Finite Element Analysis, Computer-Aided Design, Fluid Mechanics, Product Development
        - **Mathematics Courses:** Mathematical Modelling, Differential Equations, Vector Calculus, Probability and Statistics for Engineers, Linear Algebra
        """)
    st.write("")
    st.write(
        """
        ##### Yonsei University
        *Summer Exchange Student* || 2021
        - **Courses:** Introduction to Computer Graphics
        """)

# Skills
with st.container():
    st.write("---")
    st.header("Skills")
    left, middle, right = st.columns(3)
    with left:
        st.write(
            """
            ##### Mechanical Engineering
            - ANSYS
            - SolidWorks
            - Siemens NX
            - Autodesk Inventor
            - Autodesk Fusion 360
            - AutoCAD
            """
        )
    with middle:
        st.write(
            """
            ##### Manufacturing Engineering
            - Fused Deposition Modeling (FDM) 3D Printing
            - Coordinate Measuring Machine
            - Drill Press
            - Milling
            - Lathe
            """
        )

    with right:
        st.write(
            """
            ##### Data Analytics
            - Python
            - MATLAB
            - SQL
            - Statistics
            - ETL & ELT
            - Machine Learning
            - Microsoft Excel
            - Spreedsheets
            - Minitab
            """
        )
