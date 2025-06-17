import streamlit as st

file_path = "static/ff.txt"

@st.cache_resource
def get_file_handler():
    flie = open(file_path, "a+")
    return flie

file_handler = get_file_handler()

if st.button("Write to File"):
    file_handler.write("Hello, Streamlit!\n")
    file_handler.flush()
    st.success("Data written to file successfully!")
    
if st.button("Read from File"):
    file_handler.seek(0)  # Move the cursor to the beginning of the file
    content = file_handler.read()
    st.text_area("File Content", content, height=300)
    
st.button("Close File", on_click=file_handler.close)
st.write("File handler is cached and will not be closed until the app stops.")