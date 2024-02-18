import streamlit as st
import pandas as pd
import ydata_profiling
from streamlit_pandas_profiling import st_profile_report
tab1, tab2, tab3 = st.tabs(['Home', 'Profilling', 'Calculator'])
with tab1:
    st.subheader('Bringing together compiled project')
with tab2:
   st.markdown('Streamlit Pandas profiling')
   a = st.file_uploader('Upload a csv file')
   if a:
       df = pd.read_csv(a)
       st.write(df[1:5])
       pr = df.profile_report()
       st_profile_report(pr)
   else:
       st.write(':sunglasses: Upload a .csv file')
with tab3:
    import numpy as np 
    a = np.arange(10)
    st.write(a)
