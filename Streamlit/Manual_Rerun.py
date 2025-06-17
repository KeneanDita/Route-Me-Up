import streamlit as st

st.title("Counter Example with Immediate Rerun")

if "counter" not in st.session_state:
    st.session_state.counter = 0
    
def increment_counter():
    st.session_state.counter += 1
    st.rerun()  # Immediately rerun the app to reflect the updated counter

st.write(f"Counter: {st.session_state.counter}")
if st.button("Increment and Update Immediately"):
    increment_counter()# Immediately rerun the app to reflect the updated counter