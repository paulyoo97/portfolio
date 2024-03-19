import streamlit as st
st.set_page_config(page_title="Experience", page_icon="", layout="wide")    # layout by default is center.
st.sidebar.success("Select a page above.")

# Title
st.title("Work Experience \U0001F558")
st.write("---")

# List of Experiences
with st.container():
    st.write(
        """
        ##### Andorix Inc.
        *Operations Engineer, Full Time, March 2023 - Present*
        - Utilized Python scripting to automate and manage server network connectivity to reduce vulnerability windows and potential security threats during monthly data protection jobs
        - Created a Python Jupyter Notebook to autogenerate SLA Excel Reports, presented to clients and key 
          stakeholders during monthly meetings, which reduced report creation time by 75% and eliminated manual data entry errors
        - Tested and validated Optical Network Terminal fibre light levels and internet connectivity, ensuring quality and reliability before deployment.
        - Provided Data Management as a Service utilizing CommVault and Acronis Cloud Backup
        - Offered technical support and server deployment for clients in collaboration with the Infrastructure, Operations, and Project Management Teams\n
        """)
    st.write("")
    st.write(
        """
        ##### Yonsei University
        *Research Assistant, Internship, June 2021 - August 2021*
        - Collaborated with Architectural Environment Lab manager on a project focused on optimizing indoor air quality and energy in South Korean classrooms
        - Extracted live air quality data from Arduino sensor through an API, transformed collected data into tabular form utilizing MATLAB, and loaded data into Excel Spreadsheet for analysis
        - Designed an algorithm and user interface with MATLAB App Designer to display current air quality, automate data analysis, and suggest decisions to improve indoor air quality
        """)
    st.write("")
    st.write(
        """
        ##### Linamar Corporation
        *Quality Assurance and Mechanical Engineer, Internship, September 2020 - April 2021*
        - Designed CAD models and drafted 2D drawings of fixtures, drive shafts, robotic gripper parts and assemblies utilizing SolidWorks
        - Conducted quality control testing and validation of production parts using a coordinate measuring machine.
        - Measured, drafted, and revised production line layout using AutoCAD
        """)
