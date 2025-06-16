import streamlit as st
import datetime as datetime

st.title("User Information Form")


min_date = datetime.date(1920, 1, 1)
max_date = datetime.datetime.now()

with st.form(key="user_info_form"):
    st.subheader("Personal Details")
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.date_input("Date of Birth", min_value=min_date, max_value=max_date)
    
    st.subheader("Preferences")
    favorite_color = st.color_picker("Favorite Color", "#00f900")
    hobbies = st.multiselect("Hobbies", ["Reading", "Traveling", "Cooking", "Gaming"])
    
    submit_button = st.form_submit_button("Submit")
    
    if submit_button:
        st.write(f"Name: {name}")
        st.write(f"Email: {email}")
        st.write(f"Age: {age}")
        st.write(f"Favorite Color: {favorite_color}")
        st.write(f"Hobbies: {', '.join(hobbies)}")
        st.success("Form submitted successfully!")