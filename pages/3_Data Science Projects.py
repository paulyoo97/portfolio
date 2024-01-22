import streamlit as st
from PIL import Image
import pandas as pd
from pyproj import Proj, transform
import plotly.express as px


st.set_page_config(page_title="Data Science Projects", page_icon="", layout="wide")    # layout by default is center.
st.sidebar.success("Select a page above.")

# Title
st.title("Data Science & Analytics Projects \U0001F4CA")

with st.container():
    st.write("---")
    st.header("Data Science Projects")
    st.write("#### Predicting Automobile Casualty Severity in Calderdale, England")
    with st.expander("**2023-12**"):
        df = pd.read_excel('final_data.xlsx')
        # Define the coordinate systems
        bng = Proj(init='epsg:27700')  # British National Grid EPSG code
        wgs84 = Proj(init='epsg:4326')  # WGS84 EPSG code for latitude/longitude

        # Example northing (Y) and easting (X) coordinates in BNG
        northing = df['Northing']
        easting = df['Easting']

        # Convert BNG to latitude and longitude (WGS84)
        longitude, latitude = transform(bng, wgs84, easting, northing)
        dfplotting = pd.DataFrame(data = {'lat':latitude,'lon':longitude,'Severity':df['Casualty Severity']})   

        fig = px.scatter_mapbox(dfplotting, lat="lat", lon="lon", color="Severity", zoom=1)
        fig.update_layout(mapbox_style="open-street-map", mapbox_zoom=10,margin={"r":100,"t":0,"l":100,"b":0})

        st.plotly_chart(fig, use_container_width=True)
        ls,m,rs = st.columns(3)
        with m:
            st.write('*Geographical plot. Accidents in Calderdale 2014-2017.*')
        st.write(
            """
            #### Defining the Problem
            The focus of this project is to predict the casualty severity from automobile accidents using classification
            machine learning models.\n
            You can find the work done on a Jupyter Notebook [here.](https://github.com/paulyoo97/DataScience/blob/main/Traffic%20Accident%20Severity%20Analysis.ipynb)
            """)
        st.write(
            """
            #### Preparing the Data
            Firstly, data between 2014 to 2017 was extracted from multiple CSV files for road accidents that occured in Calderdale, England.
            The data can be found [here.](https://data.world/datagov-uk/053a6529-6c8c-42ac-ae1e-455b2708e535)
            
            Next, using Python, each file was loaded as a DataFrame on a Jupyter Notebook to preprocess and clean the data.
            Each DataFrame did not have any empty or missing entries; however, cleaning the data was still required.
            Here are the following preoprocessing steps that occurred:
            1) Checked for common features, created any missing features where possible, dropped unnecessary columns, renamed columns, and merged datasets.
            2) Made feature labels and data types consistent
            3) Created new features- month, day of the week, day of the month
            4) Utilized mapping to improve easier readability of categorical labels
            5) Used grouping to generalize certain column labels
            \n
            I noticed that since there were multiple features that could be used as inputs, I grouped features
            into characteristics to determine if using all or certain features would yield better results. Below are the characteristics
            based on who, what, when, and where: 
            """)
        f1,f2,f3,f4 = st.columns(4)
        with f1:
            st.write(
                """
                **Who was involved in the accident?**
                - Casualty Class
                - Sex of Casualty
                - Age Group
                """)
        with f2:
            st.write(
                """
                **What was involved in the accident?**
                - Number of Vehicles
                - Road Surface
                - Lighting Condition
                - Weather Conditions
                - Type of Vehicle
                """)
        with f3:
            st.write(
                """
                **When did the accident occur?**
                - Day of the Week
                - Day of the Month
                - Month
                - Hour
                """)
        with f4:
            st.write(
                """
                **Where did the accident occur?**
                - Easting
                - Northing
                - 1st Road Class
                """)
        st.write("")
        st.write(
            """
            #### Machine Learning Models
            The machine learning models that were utilized for classification were the
            k-nearest neighbours and random forest classifier. Classification models were used as
            the task was to predict casualty severity, which is a categorical feature. Below we can observe the accuarcy
            of each model in the form of a bar graph.
            \n
            """)
        st.image(Image.open('pages/casualty prediction.png').resize((600,400)),caption="Accuracy of each model based on who, what, when, where.",use_column_width='auto')
        st.write("")
        st.write(
            """
            #### Evaluate the Results
            Based on the average accuracy of each model using selected input characteristics (i.e., who, what, when, where),
            the KNN and random forest classifier models had accuracies of 83.1%
            and 82.3%, respectively. However, when using all features as input, we yielded better accuracy,
            where the accuracy of the KNN and random forest classifier models had accuracies of 84.1%
            and 84.3%, respectively.
            \n
            Therefore, for this application, we can conclude that casualty severity is most accurate when
            using all the features.
            """)
        st.image(Image.open('pages/casualty prediction final.png').resize((600,400)),caption="Accuracy of each model.",use_column_width='auto')


with st.container():
    st.write("---")
    st.header("Research Projects")
    st.write("#### Optimal Condition for Natural Ventilation")
    with st.expander("**2021-08**"):
        st.image(image=Image.open('pages/presentation.jpg').resize((600,400)),use_column_width="auto",caption="Presentation conducted at Yonsei University.")
        st.write(
            """
            ##### Context \n
            In the summer of 2021, I had the opportunity to visit Seoul, South Korea, to attend Yonsei University
            as a research intern. During my time, I worked with the Architectural Environment Lab where I participated on a project
            focused on identifying optimal conditions for natural ventilation in South Korean classrooms.\n
            There were two main objectives for optimal natural ventilation: \n
            - To reduce energy consumption required to regulate indoor temperature by allowing inside and outside air to mix. This was achieved using operable windows- opened or closed state.
            - To provide optimal air quality for an optimal studying environment. For example, if the carbon dioxide level is too high within a classroom, it can cause drowsiness which can result in poor concentration and academic performance.
            """)
        st.write("")
        st.write(
            """     
            ##### The Problem
            What makes this project complicated is that the outdoor air quality isn't always **ideal**. 
            In Korea, there are pollutants, particulate matter, called "fine dust" which, when exposed to a certain concentration, can negatively affect heart, lung, and developmental health. \n
            With this in mind, monitoring air quality and identifying the optimal condition to ventilate becomes crucial. Reducing energy consumption and improving performance are important, but health is not something to be compromised.
            """)
        st.write(
            """
            ##### My Research
            Part of my contribution to this project was to research and propose what other factor could influence the decision to naturally ventilate classrooms.
            What I proposed as an additional factor was pollen concentration as 20% of the population were allergic and (potentially) affected by the following:
            - Physical: nasal congestion, dry eyes
            - Exhaustion: daytime sleepiness, sleep disturbance, loss of appetite
            - Mood: irritable, miserable, depressed
            - Chronic Stress: increases risk of being allergic
            - Cognitive: slower decision making and verbal reasonings \n
            In summary, those with pollen allergy have lower energy, hindered performance, and reduced wellbeing.  
            """)
        st.write("##### Solution")
        st.write(
            """
            The lab created an Arduino Sensor and utilized ThingSpeak IoT platform to monitor live air quality data and aggregate the data to the **cloud**, respectively.
            With these tools, the following **ELT** process occured:
            - **Extracted** live air quality data from the Arduino sensor and webscraped live pollen concentation using MATLAB
            - **Loaded** the air quality data onto ThingSpeak cloud platform and then all the data to a spreadsheet
            - **Transformed** all the data using an algorithm I created to analyze the data and identify optimal conditions for natural ventilation
            """)
        st.write("")
        st.write("##### Results")
        st.write(
        """
        After building an alogorithm to analyze collected data and identify the optimal condition for natural ventilation, I created an application using MATLAB.
        The application was created to inform occupants about air quality and alert them whether a classroom should be naturally ventilated or not.
        """)
        st.image(Image.open('pages/matlab.jpg').resize((600,400)),caption="Application built using MATLAB.",use_column_width='auto')