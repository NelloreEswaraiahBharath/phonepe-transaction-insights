import streamlit as st
import pandas as pd

# Load CSV
df = pd.read_csv("csv/aggregated_transaction.csv")

st.title("PhonePe Transaction Insights")

# ---- STATE FILTER ----
state = st.selectbox("Select State", df['State'].unique())
filtered = df[df['State'] == state]

st.subheader(f"Data for {state}")
st.write(filtered)

# ---- BAR CHART ----
st.subheader("Transaction Type Analysis")
chart = filtered.groupby('Payment_Type')['Amount'].sum()
st.bar_chart(chart)

# ---- YEARLY TREND ----
st.subheader("Yearly Trend")
year_chart = filtered.groupby('Year')['Amount'].sum()
st.line_chart(year_chart)

# ---- KPI ----
st.subheader("Overall Metrics")
st.metric("Total Transactions", int(filtered["Transaction_Count"].sum()))
st.metric("Total Amount", int(filtered["Amount"].sum()))
