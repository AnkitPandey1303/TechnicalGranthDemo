import streamlit as st
import os

st.title("Latest News")
st.write("Stay updated with the latest happenings.")

# Path to the folder containing news images
news_image_folder = "news_images"

# Example News
news = [
    {
        "headline": "AI Revolution in 2025",
        "description": "Artificial Intelligence is transforming industries worldwide. Discover how AI advancements are shaping our future.",
        "image": "ai_revolution.jpg",  # Name of the image in the 'news_images' folder
        "youtube_link": "https://www.youtube.com/watch?v=example1"
    },
    {
        "headline": "Top Programming Languages of the Year",
        "description": "Find out which programming languages are leading the tech industry in 2025 and why they matter.",
        "image": "top_languages.jpg",
        "youtube_link": "https://www.youtube.com/watch?v=example2"
    },
    {
        "headline": "Breakthrough in Renewable Energy",
        "description": "Scientists have made a significant breakthrough in renewable energy technology, paving the way for a greener future.",
        "image": "renewable_energy.jpg",
        "youtube_link": "https://www.youtube.com/watch?v=example3"
    },
]

# Display the news items
for item in news:
    image_path = os.path.join(news_image_folder, item["image"])
    if os.path.exists(image_path):  # Check if the image file exists
        st.image(image_path, use_column_width=True)
    else:
        st.warning(f"Image not found: {image_path}")
    st.subheader(item["headline"])
    st.write(item["description"])  # Display the description
    st.markdown(f"[Watch on YouTube]({item['youtube_link']})")
    st.write("---")  # Divider between news items
