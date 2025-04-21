import streamlit as st
import pandas as pd
import duckdb as db

st.write("""
#SQL SRS 
SPACE REPETITION system SQL PRACTICE
"""
         )

data = {"a": [1, 2, 3], "b": [4, 5, 6]}

st.write("""
SQL REVISION SITE
""")
with st.sidebar:
    option = st.selectbox(
        "what would like to revise ?",
        ("join", "GroupBy", "Windows function"),
        index=None,
        placeholder="select theme ..."
)

st.write('you selected : ', option)
df = pd.DataFrame(data)
tab1, tab2, tab3 = st.tabs(["cat", "dog", "owm"])


st.write('you selected : ', option)
with tab1:
    input_text = st.text_area(label="entrer votre input:")
    result = db.sql(input_text)
    st.write(result)

    st.write(input_text)
