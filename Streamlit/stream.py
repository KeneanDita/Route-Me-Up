import streamlit as st
import os 

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