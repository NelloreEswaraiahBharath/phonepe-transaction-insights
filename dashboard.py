import streamlit as st
import pandas as pd
import plotly.express as px

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
chart = filtered.groupby('Payment_Type')['Amount'].sum().reset_index()

fig = px.bar(chart, x='Payment_Type', y='Amount', color='Payment_Type')
st.plotly_chart(fig)

# ---- YEARLY TREND ----
st.subheader("Yearly Trend")
year_chart = filtered.groupby('Year')['Amount'].sum().reset_index()

fig2 = px.line(year_chart, x='Year', y='Amount')
st.plotly_chart(fig2)

# ---- KPI ----
st.subheader("Overall Metrics")
st.metric("Total Transactions", int(filtered["Transaction_Count"].sum()))
st.metric("Total Amount", int(filtered["Amount"].sum()))