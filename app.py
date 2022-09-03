import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# SET PAGE CONFIG
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

df = pd.read_excel('supermarkt_sales.xlsx')

# st.dataframe(df)

# SIDEBAR
st.sidebar.header("Filter Here:")

## City filter
city = st.sidebar.multiselect(
    "Select the City:",
    options=df["City"].unique(),
    default=df["City"].unique()
)

## Customer type filter
customer_type = st.sidebar.multiselect(
    "Select Customer Type:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique()
)

## Gender
gender = st.sidebar.multiselect(
    "Select the Gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

# filtering the selection
# df_selection = df.query(
#     "City==@city & Customer_type==@customer_type & Gender==@gender"
# )

# st.dataframe(df_selection)




