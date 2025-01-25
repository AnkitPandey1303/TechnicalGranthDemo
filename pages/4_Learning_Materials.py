import streamlit as st

# Sidebar Navigation for Subpages
st.sidebar.title("Learning Material Topics")
selected_topic = st.sidebar.radio(
    "Select a topic:",
    ["Overview", "Python", "Java", "C++", "Streamlit", "Selenium", "Data Science", "Machine Learning", "AI Development"]
)

# Navigation Logic
if selected_topic == "Overview":
    st.title("Welcome to Learning Materials")
    st.write("Explore topics in-depth using the sidebar navigation.")
elif selected_topic == "Python":
    from pages.subpages import python
    python.render()  # Ensure the subpage file has a `render()` function
elif selected_topic == "Java":
    from pages.subpages import java
    java.render()
elif selected_topic == "C++":
    from pages.subpages import cpp
    cpp.render()
elif selected_topic == "Streamlit":
    from pages.subpages import streamlit
    streamlit.render()
elif selected_topic == "Selenium":
    from pages.subpages import selenium
    selenium.render()
elif selected_topic == "Data Science":
    from pages.subpages import datascience
    datascience.render()
elif selected_topic == "Machine Learning":
    from pages.subpages import machine_learning
    machine_learning.render()
elif selected_topic == "AI Development":
    from pages.subpages import ai_development
    ai_development.render()
