import streamlit as st
import os, time
# Stop execution immediately:
#st.stop()
# Rerun script immediately:
#st.experimental_rerun()

# Group multiple widgets:
with st.form(key='my_form'):
     username = st.text_input('Username')
     os.system('clear')
     password = st.text_input('Password')
     st.form_submit_button('Login')
if st.form_submit_button:
     st.write('Your username: ', username)
     st.write('Your password: ', password)
