import streamlit as st
import widgets as wd
import pandas as pd


st.title("Widgets in Streamlit")
name= st.text_input("Enter your name")

age = st.slider("Select your age", 0, 100, 25)
st.write(f"Your age is {age}")


if name:
    st.write(f"Hello, {name}!")
    
options=["python","java","c++","javascript"]
choice=st.selectbox("Select your favorite programming language",options)
st.write(f"you selected {choice}")   


data= {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 30, 22, 35],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df=pd.DataFrame(data)
st.write(df)
df.to_csv("data.csv")

upload_file= st.file_uploader("Upload a CSV file", type=["csv"])
if upload_file is not None:
    uploaded_df=pd.read_csv(upload_file)
    st.write(uploaded_df)