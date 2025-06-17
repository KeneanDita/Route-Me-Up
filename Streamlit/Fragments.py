import streamlit as st

st.title("App")

@st.fragment()
def toggle_and_text():
    st.toggle("Toggle")
    st.text_area("Enter Text")

@st.fragment()
def filter_and_text():
    st.checkbox("Filter")
    st.file_uploader("Upload File")
    st.selectbox("Select Option", ["Option 1", "Option 2", "Option 3"])
    st.slider("Slider", 0, 100, 50)
    st.text_input("Enter Text")

# Call fragments
toggle_and_text()

# Additional controls, also shown vertically
st.selectbox("Select Option", [1, 2, 3], index=None)
st.button("Update")

filter_and_text()
