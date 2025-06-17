import streamlit as st

st.sidebar.title("This is a sidebar")
st.sidebar.write("You can add text, widgets, and more here.")
sidebar_input = st.sidebar.text_input("Enter something in the sidebar")

#Tabs layout
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
    st.write("This is the content of Tab 1")
    st.button("Click me in Tab 1")
    
with tab2:
    st.write("This is the content of Tab 2")
    st.button("Click me in Tab 2")
    
with tab3:
    st.write("This is the content of Tab 3")
    st.button("Click me in Tab 3")
    
col1, col2 = st.columns(2)

with col1:
    st.write("This is the first column")
    st.button("Button in Column 1")
with col2:
    st.write("This is the second column")
    st.button("Button in Column 2")
    
#containers example
with st.container(border=True):
    st.write("This is a container with a border")
    st.button("Button in Container")
    
#Empty placeholder
placeholder = st.empty()
placeholder.write("This is a placeholder that can be updated later.")


if st.button("Update Placeholder"):
    placeholder.write("The placeholder has been updated!")


expander = st.expander("Click to expand")
expander.write("This is the content inside the expander.")

#popover example
st.write("Hover over the button to see the popover.")
with st.popover("This is a popover"):
    st.write("This content appears when you hover over the button.")
    st.button("Click me in the popover")
    
#sidebar  input handling
if sidebar_input:
    st.sidebar.write(f"You entered: {sidebar_input}")