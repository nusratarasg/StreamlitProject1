import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
@st.cache
def load_data():
    df = pd.read_csv("penguins.csv")
    return df

df = load_data()

def show_visualize_page():
    df = pd.read_csv("penguins.csv")
    st.title("Data Visualization")
    #st.write(""" #### Data Visualization """)

# pie chart
    st.write(""" #### Pie Plot """)
    data = df["species"].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    #st.write(""" #### Pie Plot """)
    st.pyplot(fig1)
# Bar Chart
    st.write(""" #### Bar Chart """)
    st.write(
        """
    #### Mean Body Mass Based On Flipper Length
    """
    )
    data = df.groupby(["flipper_length_mm"])["body_mass_g"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(""" #### Line Graph""")
    st.write(
        """
    #### Mean Body Mass Based On Flipper Length
    """
    )

    data = df.groupby(["flipper_length_mm"])["body_mass_g"].mean().sort_values(ascending=True)
    st.line_chart(data)

    # Bar and line Charts using bill_length and body_mass

    st.write(""" #### Bar Chart bill_length and body_mass""")
    st.write(
        """
    #### Mean Body Mass Based On Bill Length
    """
    )
    data = df.groupby(["bill_length_mm"])["body_mass_g"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(""" #### Line Graph""")
    st.write(
        """
    #### Mean Body Mass Based On Bill Length
    """
    )

    data = df.groupby(["bill_length_mm"])["body_mass_g"].mean().sort_values(ascending=True)
    st.line_chart(data)

