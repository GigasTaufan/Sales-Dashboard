from tkinter import E
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# SET PAGE CONFIG
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

# READ DATASET
## Caching dataset
@st.cache
def get_data_from_excel():
    df = pd.read_excel('supermarkt_sales.xlsx')

    ## Add "hour" column to dataframe 
    df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour

    return df

## Calling the function to get the dataset into dataframe
df = get_data_from_excel()

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
df_selection = df.query(
    "City==@city & Customer_type==@customer_type & Gender==@gender"
)

# st.dataframe(df_selection)

#====MAINPAGE====
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

## TOP KPI
total_sales = int(df_selection["Total"].sum())
average_rating = round(df_selection["Rating"].mean(),1)
star_rating = ":star:" * int(round(average_rating,0))
average_sale_by_transaction = round(df_selection["Total"].mean(),2)

## COLUMN FOR DISPLAY THE KPI
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US ${total_sales:,}")
with middle_column:
    st.subheader("Average Rating")
    st.subheader(f"{average_rating} {star_rating}")
with right_column:
    st.subheader("Average Sales Per Transaction")
    st.subheader(f"US ${average_sale_by_transaction}")

st.markdown("---")


# SALES BY PRODUCT LINE

## Group the product line by Product Line column
sales_by_product_line = (
    df_selection.groupby(by=["Product line"]).sum()[["Total"]].sort_values(by="Total")
)

## Make the figure 
fig_product_sales = px.bar(
    sales_by_product_line,
    x="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sales by Product Line</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)

## Configure the layout
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False)),
)

## Show the figure
st.plotly_chart(fig_product_sales)


# SALES BY HOUR (BAR CHART)

## Group the sales by Hour column
sales_by_hour = df_selection.groupby(by=["hour"]).sum()[["Total"]]

## Make the figure
fig_hourly_sales = px.bar(
    sales_by_hour,
    x=sales_by_hour.index,
    y="Total",
    title="<b>Sales by Hour</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
    template="plotly_white",
)

## Configure the layout
fig_hourly_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

## Show the figure
st.plotly_chart(fig_hourly_sales)




