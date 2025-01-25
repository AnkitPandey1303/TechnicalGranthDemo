import streamlit as st

st.title("Contact Us")
st.write("Get in touch with us using the form below.")

with st.form(key="contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.success("Thank you for your message. We will get back to you shortly!")
