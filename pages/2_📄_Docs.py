import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Documentaion",
    page_icon="📄",
)

from PIL import Image
logo = Image.open("ignitelogoW.png")
st.image(logo, width=200)
st.sidebar.image(logo, width=100)

st.write("# Documentation 📄")

st.sidebar.success("Select a product above.☝️")
st.sidebar.write('#### Table of content:')
st.sidebar.write("👉 Getting Started", )
st.sidebar.write("⚙️ How it works!!")
st.sidebar.write("📊  Charts")

st.markdown(
    """
   ### *IgniteChase is a easy to use, data visualisation tool.* 
    Ignitechase is a powerful data visualization and analytics tool that is designed to help individuals and organizations gain insights and make data-driven decisions. This tool provides a user-friendly interface that allows users to easily create customized visualizations, explore data, and uncover patterns and trends.
   #### *Prerequisites:*
    - Python
    - Streamlit
    - Pandas
    - Pipenv
    - Ploty

    ### 👉 Getting started
    Getting started with Ignitechase is a straightforward process that requires a few key tools and packages. In this guide, we will walk you through the steps needed to install Streamlit, Plotly, Pandas, and Pipenv, and get you up and running with Ignitechase.

    ##### Step 1: Install Python
    Before you can start using Ignitechase, you will need to have Python installed on your system. You can download the latest version of Python from the [official website](https://www.python.org/downloads/). Follow the installation instructions provided on the website to install Python on your system.
   
    ##### Step 2: Install Pipenv
     Pipenv is a package manager that is used to manage Python packages and dependencies. To install Pipenv, open a terminal window and enter the following command:

     ```
     pip install pipenv
     ```
     This will install Pipenv on your system.
    ##### Step 3: Create a new virtual environment
     Next, you will need to create a new virtual environment. Virtual environments are isolated Python environments that let you manage and package your Python packages without worrying about conflicts.
     ```
     pipenv shell
     ```
     This will create a new virtual environment.

     ##### Step 4: Install required packages
     With your virtual environment activated, you can now install the required packages for Ignitechase. Enter the following commands in your terminal window:
     ```
    pipenv install streamlit plotly pandas
    ```
    This will install the Streamlit, Plotly, and Pandas packages.

    ##### Step 5: Install Ignitechase
    Finally, you can install Ignitechase by entering the following command in your terminal window:
    ```
    pipenv install ignitechase
    ```
    This will install Ignitechase and all its dependencies.

    ##### Step 6: Start using Ignitechase
    With Ignitechase installed, you can start using it by running the following command in your terminal window:
    ```
    streamlit run your_app.py

    ```
    Replace your_app.py with the name of your Ignitechase app. This will start a Streamlit server and launch your Ignitechase app in your web browser.

    Congratulations! You are now ready to start using Ignitechase to visualize and analyze your data.

    ### ⚙️ How it work!!
    The code is a data visualization web application created using the Streamlit library in Python. The application allows the user to upload a CSV or Excel file and choose from various chart types to visualize the data. The chart types include Scatterplots, Lineplots, Bar, Boxplot, Histogram, Violin, Density, Heatmap, Pie, and Scatter matrix.

    Let's go through the code line by line to understand what each part does:

    ```python
    import streamlit as st
    import plotly.express as px
    import pandas as pd 
    import numpy as np
    ```

    These lines import the necessary libraries that are used in the code. **streamlit** is a Python library used for building web applications, **plotly** is a graphing library, **pandas** is a data manipulation library, and **numpy** is a numerical computing library.

    ```python
    st.set_option('deprecation.showfileUploaderEncoding', False)
    ```
    This line disables a warning that is displayed when uploading files to the application.

    ```python
    from PIL import Image
    logo = Image.open("ignitelogoW.png")
    st.image(logo, width=200)
    st.sidebar.image(logo, width=100)
    ```

    These lines import the Image module from the Python Imaging Library (PIL) and display an image logo on the main page and the sidebar of the application.

    ```python
    st.title('Data Visualization')
    st.sidebar.subheader('Visualization setting')
    ```
    These lines display the title of the application and a subheader in the sidebar.

    ```python
    uploaded_file = st.sidebar.file_uploader(label="Upload your CSV or Excel file.", type=['csv','xlsx'])

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
    ```
    These lines allow the user to upload a CSV or Excel file, which is read using the pandas library. If the file is uploaded successfully, the dataframe is displayed on the main page and the columns with numeric values are saved for later use. If the file is not uploaded, a warning message is displayed.

    ```python
    chart_select = st.sidebar.selectbox(
    label='Select the chart type',
    options=['none','Lineplots', 'Bar', 'Scatterplots', 'Boxplot', 'Histogram', 'Violin', 'Density', 'Heatmap', 'Pie', 'Scatter_matrix' ]
    )
    ```
    These lines display the sidebar menu with the chart type option.

    ```python
    if chart_select == 'Scatterplots':
    st.sidebar.subheader('Scatterplots Settings')
    try:
        x_values = st.sidebar.selectbox('X-axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('Y-axis', options=numeric_columns)
        fig = px.scatter(df, x=x_values, y=y_values)
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Error plotting scatterplot: {e}")
    ```
    These lines display the scatterplot option. If the option is selected, the x-axis and y-axis are selected from the sidebar menu. The scatterplot is generated using the Plot.

    Similar code blocks exist for each of the chart types that the user can select.

"""
)

st.markdown("""

 ### 📊 Charts
 Ignitechase is a powerful data visualization tool that offers a wide range of chart types to help users present their data in an engaging and meaningful way. Here are some of the most commonly used chart types in Ignitechase, along with the code used to create them:

  ##### 1.Line
  A line chart is used to display trends over time. Here's an example code to create a line chart in Ignitechase:
  ```python
    import streamlit as st
    import pandas as pd
    import numpy as np

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)
    ```
    **Output:**

""")
# line chart 
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.markdown("""

  ##### 2.Bar Chart
  A bar chart is used to compare values across different categories. Here's an example code to create a bar chart in Ignitechase:
  ```python
    import streamlit as st
    import pandas as pd
    import numpy as np

    chart_bar = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.bar_chart(chart_bar)
    ```
    **Output:**

""")
            
# Bar Chart
chart_bar = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

st.bar_chart(chart_bar)

st.markdown("""

  For more charts, [click here](https://docs.streamlit.io/library/api-reference/charts)

""")
            
