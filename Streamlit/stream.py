import streamlit as st
import os 

st.title("Streamlit Crash Course")
st.header("Welcome to Streamlit")
st.subheader("This is a subheader")
st.text("This is a simple text message.")
st.markdown("This is **bold** text and *italic* text.")
st.caption("This is a caption for the text above.")
st.latex(r"E = mc^2")
st.code("print('Hello, World!')", language='python')
st.divider()

st.write("Hello, Streamlit!")
st.write("Current working directory:", os.getcwd())

if 1 + 3 == 4:
    st.write("1 + 3 equals 4")
else:
    st.write("1 + 3 does not equal 4")


pressed = st.button("Press me")
print("first:",pressed)

pressed2 = st.button("Sec me")
print("Second:",pressed2)

st.divider()

st.image(os.path.join(os.getcwd(), "static", '1.jpg'), caption='Sample Image', use_container_width=True)