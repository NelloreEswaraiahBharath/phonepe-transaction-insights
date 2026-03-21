import streamlit as st
import pandas as pd
import mysql.connector

# Connect DB
conn = mysql.connector.connect(
    host="localhost",
    user="Bharath",
    password="Bharath@1234",
    database="phonepe"
)

df = pd.read_sql("SELECT * FROM transactions", conn)

st.title("📊 PhonePe Transaction Insights")

# ---- STATE FILTER ----
state = st.selectbox("Select State", df['state'].unique())

filtered = df[df['state'] == state]

st.subheader(f"Data for {state}")
st.write(filtered)

# ---- BAR CHART ----
st.subheader("Transaction Type Analysis")
chart = filtered.groupby('type')['amount'].sum()
st.bar_chart(chart)

# ---- YEARLY TREND ----
st.subheader("Yearly Trend")
year_chart = filtered.groupby('year')['amount'].sum()
st.line_chart(year_chart)