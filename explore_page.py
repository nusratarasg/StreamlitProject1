import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
@st.cache
def load_data():
    df = pd.read_csv("penguins.csv")
    return df

df = load_data()

def show_explore_page():
    df = pd.read_csv("penguins.csv")
    df = df.rename(columns={'island': 'Island','bill_length_mm': 'Bill Length', 'bill_depth_mm': 'Bill Depth','flipper_length_mm': 'Flipper Length','body_mass_g': 'Body Mass','year':'Year'})
    df = df.dropna()
    data = "penguins.csv"
    st.write(f"##    Dataset Name:  {data} ")
    st.write('Shape of dataset:', df.shape)
    c = df['species'].nunique()
    st.write('number of classes:', c)
    s = df['species'].unique()
    st.write(
        """
     Name of Classes : 
    """
    )
    #st.write('number of classes:', s)

    st.write(f"{s} ")

    d=df.describe()
    st.write(' ### Description of data:', d)
    r = df.head()
    st.write(' ### First five rows of data:')
    st.write(r)
    #st.write(f"{d} ")
    #st.title("Explore penguins Species")




