import streamlit as st
# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Home", "Content"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")

# You can also use "with" notation:
with tab1:
    st.radio('Select one:', [1, 2])
with tab2:
    st.write('Which is your favorite')
    st.radio('select one', ['bread','snacks'])
