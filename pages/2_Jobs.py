import streamlit as st

st.title("Latest Job Vacancies")
st.write("Stay updated with the latest job openings and opportunities.")

# Example Job Vacancy
jobs = [
    {
        "name_of_post": "Software Engineer - AI Specialist",
        "post_date": "2025-01-19",
        "short_information": "An exciting opportunity to work on cutting-edge AI projects with a leading tech company.",
        "important_dates": {
            "Application Start": "2025-01-20",
            "Last Date to Apply": "2025-02-10",
            "Exam Date": "2025-03-15"
        },
        "application_fee": {
            "General/OBC": "₹500",
            "SC/ST/PWD": "₹250"
        },
        "age_limit": "Minimum: 21 Years | Maximum: 35 Years",
        "vacancy_details": [
            {"post_name": "AI Specialist", "total_post": "10", "eligibility": "B.Tech/BE in CS or equivalent with AI expertise"},
            {"post_name": "ML Engineer", "total_post": "5", "eligibility": "M.Tech/PhD in Machine Learning or relevant field"}
        ],
        "category_wise_vacancy": [
            {"category": "General", "total_post": "8"},
            {"category": "OBC", "total_post": "4"},
            {"category": "SC", "total_post": "2"},
            {"category": "ST", "total_post": "1"}
        ],
        "how_to_fill": """
        - Visit the official website and click on the 'Apply Online' link.
        - Fill out the application form carefully.
        - Upload required documents, including your resume and photo.
        - Submit the form and take a printout for future reference.
        """,
        "important_links": {
            "Apply Online": "https://example.com/apply",
            "How to Fill": "https://example.com/how-to-fill",
            "Download Notification": "https://example.com/notification",
            "Resume Making": "https://example.com/resume-making"
        }
    }
]

# Render each job
for job in jobs:
    st.subheader(job["name_of_post"])
    st.write(f"**Post Date/Update:** {job['post_date']}")
    st.write(f"**Short Information:** {job['short_information']}")
    
    # Important Dates Table
    st.write("### Important Dates")
    st.table(job["important_dates"].items())
    
    # Application Fee
    st.write("### Application Fee")
    for category, fee in job["application_fee"].items():
        st.write(f"**{category}:** {fee}")
    
    # Age Limit
    st.write("### Age Limit")
    st.write(job["age_limit"])
    
    # Vacancy Details Table
    st.write("### Vacancy Details")
    st.table(job["vacancy_details"])
    
    # Category-wise Vacancy
    st.write("### Category-wise Vacancy")
    st.table(job["category_wise_vacancy"])
    
    # How to Fill
    st.write("### How to Fill the Form")
    st.markdown(job["how_to_fill"])
    
    # Important Links
    st.write("### Important Links")
    for link_name, link_url in job["important_links"].items():
        st.markdown(f"[{link_name}]({link_url})")
    
    st.write("---")

# Footer
st.write("""
---
Thank you for visiting our job portal! Stay updated with the latest job opportunities daily.
Visit our official website: [Example.com](https://example.com)
""")
