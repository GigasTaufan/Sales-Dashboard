import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# SET PAGE CONFIG
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

df = pd.read_excel('supermarkt_sales.xlsx')

st.dataframe(df)

