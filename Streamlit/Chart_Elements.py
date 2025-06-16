import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Chart Elements")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.subheader("Area Chart")
st.area_chart(chart_data)

st.subheader("Line Chart")
st.line_chart(chart_data)

st.subheader("Bar Chart")
st.bar_chart(chart_data)

st.subheader("Matplotlib Chart")
fig, ax = plt.subplots()
ax.plot(chart_data["A"], label="A")
ax.plot(chart_data["B"], label="B")
ax.plot(chart_data["C"], label="C")
ax.set_title("Matplotlib Line Chart")
ax.set_xlabel("Index")
ax.set_ylabel("Values")
ax.legend()
st.pyplot(fig)


st.subheader("Matplotlib Bar Chart")
fig, ax = plt.subplots()
ax.bar(chart_data.index, chart_data["A"], label="A", alpha=0.6)
ax.bar(chart_data.index + 0.2, chart_data["B"], label="B", alpha=0.6)
ax.bar(chart_data.index + 0.4, chart_data["C"], label="C", alpha=0.6)
ax.set_title("Matplotlib Bar Chart")
ax.set_xlabel("Index")
ax.set_ylabel("Values")
ax.legend()
st.pyplot(fig)

st.subheader("Matplotlib Area Chart")
fig, ax = plt.subplots()
ax.fill_between(chart_data.index, chart_data["A"], label="A", alpha=0.3)
ax.fill_between(chart_data.index, chart_data["B"], label="B", alpha=0.3)
ax.fill_between(chart_data.index, chart_data["C"], label="C", alpha=0.3)
ax.set_title("Matplotlib Area Chart")
ax.set_xlabel("Index")
ax.set_ylabel("Values")
ax.legend()
st.pyplot(fig)


st.title("Scatter chart")
chart_data = pd.DataFrame(
    np.random.randn(100, 2),
    columns=["x", "y"]
)
st.subheader("Scatter Chart")
st.scatter_chart(chart_data)

st.title("Map")
st.subheader("Map Chart")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"]
)
st.map(map_data)
st.subheader("Map with Markers")
st.map(map_data, zoom=10)
