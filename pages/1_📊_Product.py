import streamlit as st
import plotly.express as px
import pandas as pd 
import numpy as np

# configuration 
st.set_option('deprecation.showfileUploaderEncoding', False)

#  add logo
from PIL import Image
logo = Image.open("ignitelogoW.png")
st.image(logo, width=200)
st.sidebar.image(logo, width=100)

st.title('Data Visualization')
st.sidebar.subheader('Visualization setting')


uploaded_file = st.sidebar.file_uploader(label="Upload your CSV or Excel file.",
                         type=['csv','xlsx'])


if uploaded_file is not None:
    global df
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(uploaded_file)
        else:
            st.error("File type not supported. Please upload a CSV or Excel file.")
    except Exception as e:
        st.error(f"Error reading file: {e}")

    st.write(df)
    numeric_columns = list(df.select_dtypes(['float','int']).columns)

else:
    st.warning("Please upload a file.")



chart_select = st.sidebar.selectbox(
    label='Select the chart type',
    options=['none','Lineplots', 'Bar', 'Scatterplots', 'Boxplot', 'Histogram', 'Violin', 'Density', 'Heatmap', 'Pie', 'Scatter_matrix' ]
)


if chart_select == 'Scatterplots':
    st.sidebar.subheader('Scatterplots Settings')
    try:
        x_values = st.sidebar.selectbox('X-axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('Y-axis', options=numeric_columns)
        fig = px.scatter(df, x=x_values, y=y_values)
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Error plotting scatterplot: {e}")

if chart_select == 'Histogram':
    st.sidebar.subheader('Histogram Settings')
    try:
        x_values = st.sidebar.selectbox('Select a column for the x-axis', options=numeric_columns)
        fig = px.histogram(df, x=x_values)
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Error plotting histogram: {e}")
        
if chart_select == 'Lineplots':
    st.sidebar.subheader('Line Chart')
    try:
        x_values = st.sidebar.selectbox('Select a column for the x-axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('Select a column for the y-axis', options=numeric_columns)
        fig = px.line(df, x=x_values, y=y_values)
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Error plotting Line Plot: {e}")

if chart_select == 'Bar':
    st.sidebar.subheader('Bar Chart')
    try:
        x_values = st.sidebar.selectbox('X-axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('Y-axis', options=numeric_columns)
        fig = px.bar(df, x=x_values, y=y_values)
        st.plotly_chart(fig)
    except Exception as e:
         st.error(f"Error plotting Bar: {e}")

if chart_select == 'Violin':
    st.sidebar.subheader('Violin plot')
    try:
        x = st.sidebar.selectbox('X-axis', options=numeric_columns)
        y = st.sidebar.selectbox('Y-axis', options=numeric_columns)
        fig = px.violin(df, x=x, y=y, box=True, points="all")
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Error plotting Violin Plot: {e}")

if chart_select == 'Pie':
    st.sidebar.subheader('Pie Chart')
    try:
        column_to_plot = st.sidebar.selectbox('Select column for pie chart', options=df.columns)
        fig = px.pie(df, values=column_to_plot, names=df[column_to_plot], title=f'Pie chart of {column_to_plot}')
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Error plotting Pie Chart: {e}")

if chart_select == 'Boxplot':
    st.sidebar.subheader('Boxplot')
    try:
        x_value = st.sidebar.selectbox('Select X-axis column', options=numeric_columns)
        y_value = st.sidebar.selectbox('Select Y-axis column', options=numeric_columns)
        fig = px.box(df, x=x_value, y=y_value)
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Error plotting Boxplot: {e}")

if chart_select == 'Density':
    st.sidebar.subheader('Density Plot')
    x_values = st.sidebar.selectbox('Select the column', options=numeric_columns)
    color_values = st.sidebar.selectbox('Select the color column (optional)', ['None'] + numeric_columns)
    if color_values == 'None':
        fig = px.density_contour(df, x=x_values, marginal_x='histogram')
    else:
        fig = px.density_contour(df, x=x_values, color=color_values, marginal_x='histogram')
    st.plotly_chart(fig)



if chart_select == 'Scatter_matrix':
            st.sidebar.subheader('Scatter matrix')
            fig = px.scatter_matrix(df, dimensions=numeric_columns)
            st.plotly_chart(fig)

if chart_select == 'Heatmap':
            st.sidebar.subheader('Heatmap')
            x_values = st.sidebar.selectbox('X-axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('Y-axis', options=numeric_columns)
            fig = px.density_heatmap(df, x=x_values, y=y_values)
            st.plotly_chart(fig)


    



