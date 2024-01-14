import streamlit as st
st.experimental_connection('pets_db', type='sql')
conn = st.experimental_connection('sql')
conn = st.experimental_connection('snowpark')

class MyConnection(ExperimentalBaseConnection[myconn.MyConnection]):
   def _connect(self, **kwargs) -> MyConnection:
      return myconn.connect(**self._secrets, **kwargs)
    def query(self, query):
         return self._instance.query(query)