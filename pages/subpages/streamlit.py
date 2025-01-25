import streamlit as st

def render():
    st.title("Streamlit Learning Material")
    st.markdown("""
    ### Topics Covered:
    1. **Introduction to Streamlit**
    2. **Installing and Setting Up Streamlit**
    3. **Creating Basic Streamlit Applications**
    4. **Streamlit Widgets**: Buttons, Sliders, Text Input
    5. **Page Layout and Styling**
    6. **Dynamic Data Visualization with Streamlit**
    7. **Handling Forms and User Input**
    8. **Integrating APIs with Streamlit**
    9. **Deploying Streamlit Applications**
    10. **Advanced Features: Theming, Caching, and Multipage Apps**
    """)


    # List of topics and their content
    content = {
        "Introduction to Streamlit": """
        Streamlit is an open-source app framework that enables you to quickly build and share interactive web applications. It is built for data scientists and machine learning engineers to create beautiful data apps without needing to know web development.

        **Key Points:**
        - **Pythonic Framework**: Everything is done in Python.
        - **Fast Development**: You can create apps with a few lines of code.
        - **Interactive UI**: Allows you to add widgets and interactive elements.

        **Example:**
        ```python
        import streamlit as st
        st.title("Hello, Streamlit!")
        ```
        """,

        "Installing and Setting Up Streamlit": """
        To install Streamlit, you can use the Python package manager `pip`. Here’s how to set it up:

        **Steps:**
        1. Install Streamlit using pip:
            ```bash
            pip install streamlit
            ```
        2. Verify the installation by running:
            ```bash
            streamlit --version
            ```
        3. To create a Streamlit app, create a Python file (`app.py`) and write your app logic.
        4. Run the app using:
            ```bash
            streamlit run app.py
            ```

        **Note**: Ensure Python 3.6 or higher is installed.
        """,

        "Creating Basic Streamlit Applications": """
        A basic Streamlit app displays a title, some text, or any other widget in a simple and interactive way.

        **Key Points:**
        - **Displaying Text**: Use `st.title`, `st.header`, `st.subheader`, `st.write`, etc.
        - **Displaying DataFrames**: Streamlit also supports DataFrame visualizations.

        **Example:**
        ```python
        import streamlit as st
        st.title("Welcome to Streamlit!")
        st.write("This is a basic Streamlit application.")
        ```
        """,

        "Streamlit Widgets: Buttons, Sliders, Text Input": """
        Streamlit provides several interactive widgets that let users interact with the application.

        **Widgets Available:**
        - **Button**: `st.button("Click Me")`
        - **Slider**: `st.slider()`
        - **Text Input**: `st.text_input()`

        **Example:**
        ```python
        import streamlit as st

        name = st.text_input("Enter your name")
        age = st.slider("Select your age", 0, 100)

        st.write(f"Hello {name}, you are {age} years old.")
        ```
        """,

        "Page Layout and Styling": """
        Streamlit provides tools for laying out elements on the page and applying simple styling.

        **Key Points:**
        - **Columns**: Use `st.columns` to create multiple columns in the layout.
        - **Sidebar**: Use `st.sidebar` to create side navigation.
        - **Styling**: Streamlit allows basic customization using Markdown and HTML.

        **Example:**
        ```python
        col1, col2 = st.columns(2)

        with col1:
            st.header("Left Column")
            st.write("This is the left column.")
        
        with col2:
            st.header("Right Column")
            st.write("This is the right column.")
        ```
        """,

        "Dynamic Data Visualization with Streamlit": """
        Streamlit makes it easy to visualize data dynamically.

        **Key Points:**
        - **Charts**: Use `st.line_chart()`, `st.bar_chart()`, and `st.pyplot()` for visualizations.
        - **Maps**: You can display interactive maps using `st.map()`.

        **Example:**
        ```python
        import pandas as pd
        import streamlit as st

        data = pd.DataFrame({
            'x': [1, 2, 3, 4, 5],
            'y': [10, 20, 30, 40, 50]
        })

        st.line_chart(data)
        ```
        """,

        "Handling Forms and User Input": """
        Streamlit allows handling forms and taking user input with various widgets.

        **Key Points:**
        - **Forms**: Group widgets into forms using `st.form`.
        - **Button Actions**: Trigger actions when a button is pressed.

        **Example:**
        ```python
        import streamlit as st

        with st.form(key='my_form'):
            name = st.text_input("Enter your name")
            age = st.slider("Select your age", 0, 100)
            submit_button = st.form_submit_button("Submit")

        if submit_button:
            st.write(f"Hello {name}, you are {age} years old.")
        ```
        """,

        "Integrating APIs with Streamlit": """
        Streamlit supports integration with APIs to fetch and display data dynamically.

        **Key Points:**
        - You can use libraries like `requests` to interact with APIs.
        - Use the data returned from an API in your Streamlit app.

        **Example:**
        ```python
        import requests
        import streamlit as st

        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()
        st.write(f"Current Bitcoin Price: {data['bpi']['USD']['rate']}")
        ```
        """,

        "Deploying Streamlit Applications": """
        After building your Streamlit application, you can deploy it online using platforms like Streamlit Cloud, Heroku, or AWS.

        **Steps to Deploy on Streamlit Cloud:**
        1. Push your app code to a GitHub repository.
        2. Go to [Streamlit Cloud](https://share.streamlit.io) and click on "New app".
        3. Link your GitHub repository and select the app file.
        4. Click "Deploy".

        **Note**: You may need to create a free Streamlit Cloud account.
        """,

        "Advanced Features: Theming, Caching, and Multipage Apps": """
        Streamlit offers advanced features like theming, caching, and multipage apps to improve performance and UI customization.

        **Key Features:**
        - **Theming**: Customize the appearance of your app using the `config.toml` file.
        - **Caching**: Cache expensive computations with `@st.cache`.
        - **Multipage Apps**: Use `st.sidebar` to create navigation and multiple pages.

        **Example:**
        ```python
        @st.cache
        def expensive_computation():
            # Some expensive function
            return 42

        st.write(expensive_computation())
        ```
        """
    }

    # Display content for each topic
    for topic, text in content.items():
        st.subheader(topic)
        st.markdown(text)
