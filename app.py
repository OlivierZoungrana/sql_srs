import io
from os import supports_fd

import streamlit as st
import pandas as pd
import duckdb as db

st.write("""
#SQL SRS 
SPACE REPETITION system SQL PRACTICE
"""
         )

with st.sidebar:
    option = st.selectbox(
        "what would like to revise ?",
        ("join", "GroupBy", "Windows function"),
        index=None,
        placeholder="select theme ..."
)

csv ="""
beverage, price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages=pd.read_csv(io.StringIO(csv))

csv2 ="""
food_item, food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""

food_items= pd.read_csv(io.StringIO(csv2))

answer="""
SELECT * FROM beverages CROSS JOIN food_items
"""

solution = db.sql(answer).df()


st.header("Enter code")

query = st.text_area(label= "votre code SQL ici", key="user_input")

if query:
    result = db.sql(query).df()
    st.dataframe(result)


tab2,tab3=st.tabs(["Tables", "Solution"])

with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected")
    st.dataframe(solution)

with tab3:
    st.write(answer)
