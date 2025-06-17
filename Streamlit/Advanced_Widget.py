import streamlit as st

st.title("Advanced Widgets Example")

st.button("Ok", key="1")
st.button("Ok", key="2")

# if "slider" not in st.session_state:
#     st.session_state.slider = 25

min_value = st.slider(
    "Select a value",0, 100, 25)

st.session_state.slider = st.slider(
    "Select a value", min_value, 100, st.session_state.slider)