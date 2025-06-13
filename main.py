import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.image("images/photo.png")


with col2:
    st.title("Ardit Sulce")
    content = """
    Hi i am Ardit!i am a Python programmer,teacher and founder of PythonHow.i graduated in 2013 with a master of science in geospatial technologies from the university of Muenster in Germany with a focus on using Python for remote sensing.i have worked with  companies from various countries,such as the Center of Conservation Geography,
    to map and understand Australian ecosystems,
    image processing with the Swiss in-Terra,
    and performing data mining to gain business insights
    with the Australian rapid intelligence
    """
    st.info(content)

content2 = """Below you can find some of the apps i have build in Python.Feel free to contact me!"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


