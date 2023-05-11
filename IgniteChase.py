import streamlit as st

st.set_page_config(
    page_title="IgniteChase",
    page_icon="🔥",
)

from PIL import Image
logo = Image.open("ignitelogoW.png")
st.image(logo, width=200)
st.sidebar.image(logo, width=100)

st.write("# Welcome to IgniteChase! 🔥")

st.sidebar.success("Select a product above.☝️")

st.markdown(
    """
   ## *IgniteChase is a easy to use, data visualisation tool.*
    “We are surrounded by data, but starved for insights.”
    ### Everything you get with IgniteChase
    -  It allows users to easily and intutively create graphical repsentation of their data. 
    - Its user-friendly interface and easy to use
    ### Keep track with all Forecasts
    IgniteChase offers a range of features that makes it a powerful and flexible tool for data visualisation. 
    - Quickly understand and analyze large datasets 
    - Identify trends and patterns
    - Make data-driven decisions
"""
)

st.image('public/mockup1.png',width=350)


st.markdown(
    """
    ### Features
     With IgniteChase, users can quickly and easily create wide range of visualisations, including  
    - Bar chart
    - Line chart
    - Scatter chart
    - Pie chart
    - Histogram
    - Boxplot
    - Heatmap
   
"""
)