import streamlit as st
from PIL import Image

st.set_page_config(page_title="MechEng Projects", page_icon="", layout="wide")    # layout by default is center.
st.sidebar.success("Select a page above.")

# Title
st.title("MechEng Projects \U00002699")

with st.container():
    st.write("---")
    st.header("Undergraduate Studies")
    st.write("#### Final Year Capstone Design Project")
    with st.expander("**2022-04**"):
        task, how, results = st.columns(3)
        with task:
            st.write("#### Task")
            st.image(Image.open('pages/initial contour.png').resize((200,400)),caption="Contour plot of an initial design.",use_column_width='auto')
            st.write(
                """
                - Collaborated in a team of 4 to research, design, and create a specimen used for planar simple shear-stress test while observing stress-strain behaviour, deformation, and concentration
                """)
        with how:
            st.write("#### How")
            st.image(Image.open('pages/sample specimen.png').resize((200,355)),caption="Sample specimen before final design.",use_column_width='auto')
            st.write(
                """
                - Used **Autodesk Fusion 360** to create prototypes and final design
                - Analyzed stress-strain results by simulating a finite element anaylsis using **ANSYS Mechanical Workbench**
                """)
        with results:
            st.write("#### Results")
            st.image(Image.open('pages/contour.png').resize((200,400)),caption="Contour plot of final design.",use_column_width='auto')
            st.write(
                """
                - Tested and modified thickness, aspect ratio, and fillets in the gauge section while optimizing the number of TET10 elements and nodes
                - Contour plot displays high stress concentrations at the gauge section due to reduced gauge section thickness, increase in aspect ratio, and fillets that reduce stress concentration at corners
                - Thickness went from 1.8 mm to 0.75 mm
                - Aspect ratio went from 5 to 6.5
                """)

with st.container():
    st.write("#### CPU Heatsink Design")
    with st.expander("**2020-04**"):
        task, how, results = st.columns(3)
        with task:
            st.write("#### Task")
            st.image(Image.open('pages/prototype heatsink.png').resize((600,400)),caption="Sample prototype CPU heatsink.",use_column_width='auto')
            st.write(
                """
                - Worked in a team of 4 to research, design, and analyze the results of a 3D printed titanium CPU Heat Sink which diffused heat using a computer fan's airflow
                """)
        with how:
            st.write("#### How")
            st.image(Image.open('pages/CPU heatsink.png').resize((600,400)),caption="Final CPU heatsink design.",use_column_width='auto')
            st.write(
                """
                - Used **Autodesk Inventor** to create models and isometric drawings
                """)
        with results:
            st.write("#### Results")
            st.image(Image.open('pages/recirculation.png').resize((600,400)),caption="Recirculation simulation using ANSYS-CFX on prototype.",use_column_width='auto')
            st.write(
                """
                - Team used ANSYS-CFX to run test simulation on prototypes and then redesigned the product to improve recirculation which resulted in an increase of 10% heat dissipation
                """)

with st.container():
    st.write("#### Gear Train Assembly Finite Element Analysis")
    with st.expander("**2019-04**"):
        task, how, results = st.columns(3)
        with task:
            st.write("#### Task")
            st.image(Image.open('pages/wall-e.png').resize((600,450)),caption="3D CAD Model of WALL-E.",use_column_width='auto')
            st.write(
                """
                - Worked in a team of 3 to model Disney Pixar's WALL-E to creatively design the drivetrain system, head, and body subassemblies 
                - Conducted a stress analysis on the drivetrain gear using a load of 510 N
                """)
        with how:
            st.write("#### How")
            st.image(Image.open('pages/drivetrain.png').resize((600,450)),caption="WALL-E drivetrain subassembly.",use_column_width='auto')
            st.write(
                """
                - Utilized **SIEMENS NX10** CAD software to create parts for each subassembly
                - Evaluated a stress analysis on the drivetrain gear using **Autodesk Fusion** to conduct an FEA
                """)
        with results:
            st.write("#### Results")
            st.image(Image.open('pages/gear stress.png').resize((600,450)),caption="Drivetrain gear stress analysis.",use_column_width='auto')
            st.write(
                """
                - Analyzed findings from stress analysis and concluded that the gear teeths from the drivetrain required thicker surface area to manage stress distribution
                """)

with st.container():
    st.write("#### Autonomous Robot")
    with st.expander("**2018-04**"):
        task, how, results = st.columns(3)
        with task:
            st.write("#### Task")
            st.image(Image.open('pages/walker.png').resize((600,400)),caption="Concept drawing of walker robot.",use_column_width='auto')
            st.write(
                """
                - Colloborated in a group of 4 to design, manufacture, and assemble an autonomous robot that travelled on uneven terrian and arrived at a specified destination
                """)
        with how:
            st.write("#### How")
            st.image(Image.open('pages/elephant.png').resize((600,400)),caption="Concept drawing of elephant inspired robot.",use_column_width='auto')
            st.write(
                """
                - Generated initial concept designs - elephant, walker, and scorpion inspired robots
                - Group concluded to use a biologically inspired scorpion autonomous robot as it had less parts, simple design, and optimized for speed
                - Utilized **Autodesk Inventor** to design and measure 2D drafts and 3D printed parts
                """)
        with results:
            st.write("#### Results")
            st.image(Image.open('pages/scorpion.png').resize((600,400)),caption="Final design of scorpion robot.",use_column_width="auto")
            st.write(
                """
                - After initial testing, the power output and RPM were recalculated, which resulted in a a robot that was 78.6% more accurate than the course average
                - Class time was 48.3 seconds while group time was 10.32 seconds
                """)