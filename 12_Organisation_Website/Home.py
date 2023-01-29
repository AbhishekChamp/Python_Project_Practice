import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.title("Fictional Company")
content = """
This is a simple organisation information based website and all the details present here are fictional. There are two pages present in this website and there is a Home page with employee details and in Contact Us page there is a form which can be filled and the entire application is developed using streamlit framework in python.
"""
st.info(content)

st.subheader('Our Team')

col1, col2, col3 = st.columns(3)

df = pd.read_csv('./data.csv')

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('images/'+row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('images/'+row['image'])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('images/'+row['image'])