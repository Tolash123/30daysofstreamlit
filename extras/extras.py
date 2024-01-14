from streamlit_extras.add_vertical_space import add_vertical_space
import streamlit as st
def example():
    add = st.slider('Add n vertical lines below this', 1,20,5)
    add_vertical_space(add)
    st.write('Here is text after the nth line')

example()