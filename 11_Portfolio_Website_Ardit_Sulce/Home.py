import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('./images/ardit_photo.png')

with col2:
    st.title("Ardit Sulce")
    content = """
    About Ardit : He is a Python programmer, teacher and founder of PythonHow. He graduated in 2013 with a Master of Science in Geospatial Technologies from University og Muenster in Germany wit a focus on using Python for remote sensing, He had worked with companies from various countries, such as the Center for Conservation Geography, to map and understand Australian ecosystems, image processing with Swiss in-Terra, and performing data mining to gain business insights with the Australian Rapid Intelligence.
    """
    st.info(content)

content2 = """
Below you can find some of the apps he had built in Python. Feel free to contact him!
"""
st.write(content2)

col3, empty_col , col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv('./data.csv', sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image("./images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image("./images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")