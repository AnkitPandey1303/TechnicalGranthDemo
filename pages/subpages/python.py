import streamlit as st

def render():
    st.title("Python Learning Material")
    st.write("Here are the topics covered in Python Learning Material:")
    st.markdown("""
    ### Topics Covered:
    1. **Introduction to Python**
    2. **Python Basics**: Variables, Data Types, Operators
    3. **Control Flow**: if-else, loops (for, while)
    4. **Functions and Modules**
    5. **File Handling**
    6. **Exception Handling**
    7. **Object-Oriented Programming in Python**
    8. **Python Libraries Overview**: NumPy, Pandas, Matplotlib
    9. **Python for Web Development**: Flask, Django Basics
    10. **Working with APIs in Python**
    """)
    
    # List of topics and their content
    content = {
        "Introduction to Python": """
        Python is a high-level, interpreted programming language known for its simplicity and versatility.
        It is widely used for web development, data analysis, artificial intelligence, and more.

        **Key Points:**
        - Easy-to-read syntax
        - Interpreted and dynamically typed
        - Extensive standard library and third-party modules
        """,

        "Python Basics: Variables, Data Types, Operators": """
        Variables store data, and Python supports multiple data types like integers, floats, strings, and more.
        Operators perform operations on variables and values.

        **Key Points:**
        - **Variables**: Dynamic typing (e.g., `x = 10`)
        - **Data Types**: int, float, str, list, tuple, dict, set
        - **Operators**: Arithmetic (`+`, `-`), Logical (`and`, `or`), Comparison (`==`, `!=`)

        **Example:**
        ```python
        x = 10  # Integer
        y = 3.14  # Float
        name = "Python"  # String
        result = x + y
        print(result)  # Output: 13.14
        ```
        """,

        "Control Flow: if-else, loops (for, while)": """
        Control flow structures allow decision-making and repetitive tasks.

        **Key Points:**
        - **if-else**: Conditional execution
        - **for loop**: Iterate over sequences
        - **while loop**: Repeated execution until a condition is met

        **Example:**
        ```python
        x = 10
        if x > 5:
            print("x is greater than 5")
        else:
            print("x is 5 or less")

        # Loop Example
        for i in range(3):
            print(i)  # Output: 0, 1, 2
        ```
        """,

        "Functions and Modules": """
        Functions encapsulate reusable code, and modules organize related functions and variables.

        **Key Points:**
        - **Functions**: Defined with `def` keyword
        - **Modules**: Import with `import` keyword

        **Example:**
        ```python
        def greet(name):
            return f"Hello, {name}!"

        import math
        print(math.sqrt(16))  # Output: 4.0
        ```
        """,

        "File Handling": """
        Python allows reading and writing files easily with built-in functions.

        **Key Points:**
        - **Modes**: `'r'` (read), `'w'` (write), `'a'` (append)
        - **File Handling Functions**: `open()`, `read()`, `write()`, `close()`

        **Example:**
        ```python
        # Write to a file
        with open("example.txt", "w") as file:
            file.write("Hello, Python!")

        # Read from a file
        with open("example.txt", "r") as file:
            print(file.read())
        ```
        """,

        "Exception Handling": """
        Exceptions handle errors gracefully without crashing the program.

        **Key Points:**
        - **try-except**: Catch errors
        - **finally**: Execute cleanup code

        **Example:**
        ```python
        try:
            x = 10 / 0
        except ZeroDivisionError:
            print("Cannot divide by zero")
        finally:
            print("Execution completed")
        ```
        """,

        "Object-Oriented Programming in Python": """
        OOP organizes code using objects, classes, and methods.

        **Key Points:**
        - **Class**: Blueprint for objects
        - **Object**: Instance of a class
        - **Inheritance**: Reusing code in derived classes

        **Example:**
        ```python
        class Animal:
            def __init__(self, name):
                self.name = name

            def speak(self):
                return f"{self.name} makes a sound"

        dog = Animal("Dog")
        print(dog.speak())  # Output: Dog makes a sound
        ```
        """,

        "Python Libraries Overview: NumPy, Pandas, Matplotlib": """
        These libraries are essential for data analysis and visualization.

        **Key Points:**
        - **NumPy**: Numerical operations (arrays, linear algebra)
        - **Pandas**: Data manipulation (DataFrames)
        - **Matplotlib**: Visualization (plots, charts)

        **Example:**
        ```python
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt

        # NumPy
        arr = np.array([1, 2, 3, 4])
        print(arr.mean())  # Output: 2.5

        # Pandas
        data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
        df = pd.DataFrame(data)
        print(df)

        # Matplotlib
        plt.plot([1, 2, 3], [4, 5, 6])
        plt.show()
        ```
        """,

        "Python for Web Development: Flask, Django Basics": """
        Python frameworks simplify web development.

        **Key Points:**
        - **Flask**: Lightweight and minimal
        - **Django**: Full-stack framework with built-in admin panel

        **Flask Example:**
        ```python
        from flask import Flask
        app = Flask(__name__)

        @app.route("/")
        def home():
            return "Hello, Flask!"

        if __name__ == "__main__":
            app.run(debug=True)
        ```
        """,

        "Working with APIs in Python": """
        APIs enable interaction with external services.

        **Key Points:**
        - Use libraries like `requests` to send HTTP requests
        - Parse JSON responses for structured data

        **Example:**
        ```python
        import requests

        response = requests.get("https://api.github.com")
        if response.status_code == 200:
            print(response.json())
        ```
        """
    }

    # Display content for each topic
    for topic, text in content.items():
        st.subheader(topic)
        st.markdown(text)

