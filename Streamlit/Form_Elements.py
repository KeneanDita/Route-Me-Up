import streamlit as st
import pandas as pd

st.title("Form Elements")


with st.form(key="my_form"):
    st.subheader("Text Input")
    name = st.text_input("Enter your name")
    feedback = st.text_area("Enter your feedback")
    
    st.subheader("Date and Time Input")
    dob = st.date_input("Select your date of birth")
    time = st.time_input("Select a time")
    
    st.subheader("Selectors")
    choice = st.radio("Choose an option", ["Bugatti", "Ferrari", "Lamborghini"])
    options = st.selectbox("Select a car", ["Bugatti", "Ferrari", "Lamborghini"])
    multi_select = st.multiselect("Select multiple cars", ["Bugatti", "Ferrari", "Lamborghini"])
    checkbox = st.checkbox("I agree to the terms and conditions")
    slider = st.slider("Select a range", 0, 100, (20, 80))
    number_input = st.number_input("Enter a number", min_value=0, max_value=100, value=50)
    file_uploader = st.file_uploader("Upload a file", type=["csv", "txt"])
    color_picker = st.color_picker("Pick a color", "#00f900")
    button = st.form_submit_button("Submit")
    if button:
        st.write(f"Name: {name}")
        st.write(f"Feedback: {feedback}")
        st.write(f"Date of Birth: {dob}")
        st.write(f"Time: {time}")
        st.write(f"Choice: {choice}")
        st.write(f"Selected Car: {options}")
        st.write(f"Multiple Cars Selected: {multi_select}")
        st.write(f"Checkbox: {checkbox}")
        st.write(f"Slider Range: {slider}")
        st.write(f"Number Input: {number_input}")
        
        if file_uploader is not None:
            df = pd.read_csv(file_uploader)
            st.write("Uploaded File:")
            st.dataframe(df)
        
        st.write(f"Color Picked: {color_picker}")