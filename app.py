import streamlit as st
import pandas as pd
from db_con import run_query
import query as q 

st.set_page_config(page_title="OLA Ride Insights", layout="wide")

st.title("🚕 OLA Ride Insights Dashboard")
st.subheader("Data Analytics & Business Intelligence")

df = pd.read_csv("ola_dataset_cleaned.csv")

st.write("### Sample Data")
st.dataframe(df.head())

col1, col2, col3 = st.columns(3)

col1.metric("Total Rides", df.shape[0])
col2.metric("Total Revenue", f"₹ {df['Booking_Value'].sum():,.0f}")
col3.metric("Cancelled Rides", df['Booking_Status'].value_counts().get('Canceled by Customer', 0))

vehicle = st.selectbox(
    "Select Vehicle Type",
    options=df['Vehicle_Type'].unique()
)

filtered_df = df[df['Vehicle_Type'] == vehicle]

st.dataframe(filtered_df)

# =======================
# SQL INSIGHTS SECTION
# =======================

st.divider()
st.header("📊 SQL-Based Insights")

# Total rides from SQL
sql_total_rides = run_query(q.TOTAL_RIDES)
st.metric("Total Rides (SQL)", int(sql_total_rides['total_rides'][0]))

# Top 5 customers
st.subheader("Top 5 Customers by Booking Value")
top5_df = run_query(q.TOP_5_CUSTOMERS)
st.dataframe(top5_df)
                                                                                                        
  

st.subheader("Revenue by Vehicle Type")

revenue_by_vehicle = (
    df.groupby("Vehicle_Type")["Booking_Value"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(revenue_by_vehicle)
