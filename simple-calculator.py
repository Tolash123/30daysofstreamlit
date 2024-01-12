import streamlit as st
st.header('Simple Calculator by: Dristol')
col1,col2 =st.columns(2)
col3,col4 =st.columns(2)

with col1:
  st.header(""" Addition  """)
  a = st.number_input('Enter a number')
  b = st.number_input('Add to ')
  c = st.number_input('plus')
  st.write(a+b+c)

with col2:
  st.header(""" Subtraction  """)
  a = st.number_input('Enter number')
  b = st.number_input('To subtract')
  c = st.number_input('To minus')
  st.write(a-b-c)

with col3:
  st.header(""" Division  """)
  a = st.number_input('What are you dividing')
  b = st.number_input('From')
  c = st.number_input('From ')
  d = (a / b)
  st.write(d)
  st.write(d/c)

with col4:
  st.header(""" Multiplication  """)
  a = st.number_input('What are you multiplying')
  b = st.number_input('by')
  d = a*b
  c = st.number_input('by ')
  st.write(d)
  st.write(d*c)

from math import *
st.header('Complex Maths')
g = st.number_input('check for sin,cosine, tangent of numbers and so on.')
st.write('sin',sin(g))
st.write('cos',cos(g))
st.write('tan',tan(g))
st.write('sinh',sinh(g))
st.write('cosh',cosh(g))
st.write('tanh',tanh(g))