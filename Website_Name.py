import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Resource to Help Indians",  # Title displayed in the browser tab
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar for navigation
st.sidebar.title("Resource to Help Indians")
st.sidebar.info("Select a section from the sidebar to get started.")

# Main content
st.title("Welcome to Resource to Help Indians 🎉")
st.markdown(" # <span style='color:red;'>Dear Viewers!</span>", unsafe_allow_html=True)
st.write("""
We provide a wide range of resources for government and private job seekers. 
Explore various sections to find valuable information and tools tailored to your needs.

### Why You Should Visit Our Website:
- **Comprehensive Job Listings**: Access the latest job openings from both government and private sectors. Our website is regularly updated to ensure you don't miss any opportunities.
- **Free Educational Resources**: We offer a variety of learning materials to help you improve your skills, including coding, general knowledge, and professional development courses.
- **Practice Test and Quizzes**: Prepare for competitive exams, interviews, or just test your knowledge with quizzes available in various domains.
- **Stay Updated**: Get the latest news and notifications about job openings, government schemes, and educational opportunities.
- **Contact and Support**: Have questions or need assistance? Our website includes a dedicated Contact Us page where you can reach out for support.

Use the sidebar to navigate through the sections and explore all the features of our website. We're here to help you in your journey to success!

""")

