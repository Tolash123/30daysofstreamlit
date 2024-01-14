import streamlit as st 
import pandas as pd
df =pd.read_csv('occupation.csv')

st.dataframe(df)
st.table(df.iloc[0:10])
st.json({'foo':'bar','fu':'ba'})
st.metric(label="Temp", value="273 K", delta="1.2 K")