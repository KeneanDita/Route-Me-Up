import streamlit as st
import os
import pandas as pd

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

st.divider()



st.title("Streamlit Elements Demo")
# Dataframe Section
st.subheader("Dataframe")

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 32, 37, 45],
    'Occupation': ['Engineer', 'Doctor', 'Artist', 'Chef']
}) 

st.dataframe(df)
# Data Editor Section (Editable dataframe)
st.subheader("Data Editor")
editable_df = st.data_editor(df)
print(editable_df)

# Static Table Section
st.subheader("Static Table") 
st.table(df)

#Metrics Section
st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average Age", value=df['Age'].mean())


#Json and dictionary Section
st.subheader("JSON and Dictionary")
sample_dict = {
    "name": "Alice",
    "age": 30,
    "city": "Wonderland"
}
st.json(sample_dict)

# also display a dictionary
st.write("Dictionary view:", sample_dict)