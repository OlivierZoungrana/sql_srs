import streamlit as st
import pandas as pd
import duckdb as db

data= {"a": [1, 2, 3], "b": [4, 5, 6]}

df= pd.DataFrame(data)
tab1,tab2,tab3 = st.tabs(["cat", "dog", "owm"])

with tab1:
    input_text=st.text_area(label="entrer votre input:")
    result =db.sql(input_text)
    st.write(result)

    st.write(input_text)
    st.dataframe(df)