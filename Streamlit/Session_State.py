import streamlit as st

counter = 0
st.write("Counter:", counter)
if st.button("Increment Counter"):
    counter += 1
    st.write("Counter:", counter)
else:
    st.write("Counter remains:", counter)