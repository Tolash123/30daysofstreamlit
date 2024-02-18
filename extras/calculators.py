import streamlit as st
import numpy as np 

def cal():
    tab1,tab2 = st.tabs(['Calculator', '2Dimension'])
    with tab1:
       st.subheader('Numpy Calculator')
       st.write('Complex Maths')
       a = st.number_input('Enter a number! ')
       st.write('The sin of the number: ', np.sin(a))
       st.write('The cos of the number: ', np.cos(a))
       st.write('The tan of the number: ', np.tan(a))
       st.write('The sinh of the number: ', np.sinh(a))
       st.write('The cosh of the number: ', np.cosh(a))
       st.write('The tanh of the number: ', np.tanh(a))
       
    with tab2:
        st.header('Printing Dimension')
        
cal()