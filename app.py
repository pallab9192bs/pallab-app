#Imports 

import streamlit as st
import seaborn as sns
import pandas as pd
#Make Title & Sub Header of My Streamlit app

st.title(":blue[Exploratory Data Analysis App]")
st.markdown("By  **:green[Pallab Sarkar , JUEE]**")
st.divider()

st.markdown(":red[EDA Analyis through Application of Python,Pandas,Seaborn,Streamlit]")
st.divider()

#upload datasheet by user


upload=st.file_uploader("Upload CSV Files")
if upload is not None:
    data=pd.read_csv(upload)

#show dataset to user

if upload is not None:
  
    if st.button("Head"):
        st.write(data.head())
    if st.button("Tail"):
        st.write(data.tail())
    if st.button("Entire DataSet"):
        st.write(data)

    
    
#User Check data type of each column
if upload is not None:
    if st.checkbox("Data Type of Each Column in DataFrame"):
        st.text("DataTypes")
        st.write(data.dtypes)
        
#Find Shape of the Uploaded Data Shape
if upload is not None:
    data_shape=st.radio("What Dimension Need?",("Rows","Columns"))
    
    if data_shape=="Rows":
        rw=st.write(data.shape[0])
        
        
        
    if data_shape=="Columns":
        st.write(data.shape[1])
        

#User Find the Null Values in Dataset
if upload is not None:
    test=data.isnull().values.any()
    
    if test==True: 
        if st.button("NULL VALUES Detected! Want to Visualize?"):
            sns.heatmap(data.isnull())
            st.pyplot()
            
    if test==False: 
        st.success("Congo! No Null Values Detected")
            
# Get Duplicate Value in the dataset
if upload is not None:
    test=data.duplicated().any()
    
    if test==True:
        st.warning("Duplicate Values Detected!")
        dup=st.selectbox("Remove Duplicate ??",("Choose","Yes","No"))
        
        if dup=="Yes":
            data=data.drop_duplicates()
            st.success("Removed Duplicates")
            st.text("New Refined Data is :")
            st.write(data)
            
            
        if dup=="No":
            st.text("Ok.")
        
    
#Overall Statistics :
      
if upload is not None:
    if st.button("Statistical Analyis"):
        st.write(data.describe())
