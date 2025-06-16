import streamlit as st

if "step" not in st.session_state:
    st.session_state.step = 1
    
if "info" not in st.session_state:
    st.session_state.info = {}
    
if st.session_state.step == 1:
    st.header("Part 1: Personal Information")
    name = st.text_input("Name", value=st.session_state.info.get("name", ""))
    if st.button("Next"):
        st.session_state.info["name"] = name
        st.session_state.step = 2
elif st.session_state.step == 2:
    st.header("Review Information")
    
    st.subheader("Please review your information:")
    st.write(f"Name: {st.session_state.info.get('name', '')}")
    
    if st.button("Submit"):
        st.session_state.info["name"] = st.session_state.name
        st.success("Information submitted successfully!")
        st.session_state.step = 1