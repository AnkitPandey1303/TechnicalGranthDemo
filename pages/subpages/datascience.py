import streamlit as st

def render():
    st.title("Data Science Learning Material")
    st.markdown("""
    ### Topics Covered:
    1. **Introduction to Data Science**
    2. **Data Manipulation with Pandas**
    3. **Data Visualization with Matplotlib and Seaborn**
    4. **Exploratory Data Analysis (EDA)**
    5. **Working with NumPy for Numerical Computations**
    6. **Handling Missing Data**
    7. **Feature Engineering Basics**
    8. **Introduction to Machine Learning Models**
    9. **Model Evaluation Techniques**
    10. **Deploying Data Science Projects**
    """)

    # List of topics and their content
    content = {
        "Introduction to Data Science": """
        Data Science is an interdisciplinary field that combines techniques from computer science, statistics, and domain knowledge to extract insights and knowledge from data.

        **Key Points:**
        - Involves data collection, data cleaning, data analysis, and data visualization.
        - Uses statistical methods and machine learning algorithms for predictive modeling and decision-making.
        - Applies to various fields like business, healthcare, finance, and more.

        **Example:**
        Data Science involves steps like:
        1. Collecting data from various sources.
        2. Cleaning and preparing data for analysis.
        3. Analyzing data with algorithms.
        4. Visualizing results to make decisions.
        """,

        "Data Manipulation with Pandas": """
        Pandas is a powerful library for data manipulation in Python. It provides data structures like DataFrames and Series to handle structured data.

        **Key Points:**
        - Allows for data cleaning, merging, reshaping, and aggregating.
        - Provides functionalities to handle missing data, filter, and sort data.
        - Works seamlessly with other libraries like NumPy and Matplotlib.

        **Example:**
        ```python
        import pandas as pd
        df = pd.read_csv('data.csv')
        df['new_column'] = df['old_column'] * 2
        df.dropna(inplace=True)
        ```        
        """,

        "Data Visualization with Matplotlib and Seaborn": """
        Matplotlib and Seaborn are two popular libraries for data visualization in Python.

        **Matplotlib** is used for creating static, animated, and interactive plots.
        **Seaborn** is built on top of Matplotlib and provides a high-level interface for attractive and informative statistical graphics.

        **Example:**
        ```python
        import matplotlib.pyplot as plt
        import seaborn as sns
        df = pd.read_csv('data.csv')

        sns.heatmap(df.corr(), annot=True)
        plt.show()
        ```        
        """,

        "Exploratory Data Analysis (EDA)": """
        EDA is the process of analyzing data sets to summarize their main characteristics, often with visual methods.

        **Key Points:**
        - Involves data cleaning, feature selection, and data visualization.
        - Helps in understanding the distribution, trends, and relationships in the data.
        - Identifies potential issues with data such as missing values or outliers.

        **Example:**
        ```python
        sns.pairplot(df)
        plt.show()
        ```        
        """,

        "Working with NumPy for Numerical Computations": """
        NumPy is a library for numerical computations in Python. It provides support for arrays, matrices, and a wide range of mathematical functions.

        **Key Points:**
        - Efficiently handles large data sets using arrays.
        - Supports mathematical operations like linear algebra, statistics, and random number generation.

        **Example:**
        ```python
        import numpy as np
        array = np.array([1, 2, 3, 4])
        mean_value = np.mean(array)
        ```        
        """,

        "Handling Missing Data": """
        Handling missing data is an important part of data preprocessing. Common strategies include removing or filling missing values.

        **Key Points:**
        - **Drop missing values**: `df.dropna()`
        - **Fill missing values**: `df.fillna(value)`
        - **Forward or backward filling**: `df.ffill()` or `df.bfill()`

        **Example:**
        ```python
        df.fillna(df.mean(), inplace=True)
        ```        
        """,

        "Feature Engineering Basics": """
        Feature engineering is the process of using domain knowledge to select, modify, or create features that help machine learning models perform better.

        **Key Points:**
        - It includes transformations such as scaling, encoding, and creating new features.
        - Feature selection can be used to identify the most important features for a model.

        **Example:**
        ```python
        df['new_feature'] = df['column1'] * df['column2']
        ```        
        """,

        "Introduction to Machine Learning Models": """
        Machine Learning involves training algorithms to learn patterns from data and make predictions or decisions.

        **Key Points:**
        - **Supervised Learning**: Involves labeled data and algorithms like linear regression, decision trees, etc.
        - **Unsupervised Learning**: Involves unlabeled data and algorithms like clustering and dimensionality reduction.
        - **Reinforcement Learning**: Involves learning through interactions with an environment.

        **Example:**
        ```python
        from sklearn.linear_model import LinearRegression
        model = LinearRegression()
        model.fit(X_train, y_train)
        ```        
        """,

        "Model Evaluation Techniques": """
        Evaluating the performance of machine learning models is crucial to ensure they generalize well on new data.

        **Key Metrics:**
        - **Accuracy**: Proportion of correct predictions.
        - **Precision, Recall, F1-Score**: Metrics used for classification problems.
        - **Mean Squared Error (MSE)**: Used for regression models.

        **Example:**
        ```python
        from sklearn.metrics import mean_squared_error
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f'Mean Squared Error: {mse}')
        ```        
        """,

        "Deploying Data Science Projects": """
        Deploying a data science model involves making the model available for use in a production environment.

        **Key Points:**
        - **Model Serialization**: Use libraries like `joblib` or `pickle` to save models.
        - **Web Deployment**: Use frameworks like Flask or FastAPI to create a REST API for the model.
        - **Model Monitoring**: Track the model's performance over time.

        **Example:**
        ```python
        import joblib
        joblib.dump(model, 'model.pkl')
        ```        
        """
    }

    # Display content for each topic
    for topic, text in content.items():
        st.subheader(topic)
        st.markdown(text)
