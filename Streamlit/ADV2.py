import streamlit as st

# Initialize checkbox state
if "checkbox" not in st.session_state:
    st.session_state.checkbox = False

def toggle_checkbox():
    st.session_state.checkbox = not st.session_state.checkbox

# Display checkbox and toggle state
st.checkbox("Show Input field", value=st.session_state.checkbox, on_change=toggle_checkbox)

# Conditionally show text input
if st.session_state.checkbox:
    user_input = st.text_input("Enter some text", key="user_input")
else:
    user_input = st.session_state.get("user_input", "")

# Display result
st.write("You entered:", user_input)
