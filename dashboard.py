import streamlit as st
import pandas as pd
from utils.data_loader import load_data
from analysis.insights import generate_insights

df = load_data()

st.set_page_config(page_title="PhonePe Insights", layout="wide")

st.title(" PhonePe Transaction Insights Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")
state = st.sidebar.selectbox("Select State", df['State'].unique())

filtered = df[df['State'] == state]

# KPI Section
col1, col2 = st.columns(2)
col1.metric("Total Transactions", int(filtered["Transaction_Count"].sum()))
col2.metric("Total Amount", int(filtered["Amount"].sum()))

# Charts
st.subheader("Payment Type Distribution")
st.bar_chart(filtered.groupby('Payment_Type')['Amount'].sum())

st.subheader("Yearly Trend")
st.line_chart(filtered.groupby('Year')['Amount'].sum())

st.subheader("Top States")
top_states = df.groupby('State')['Amount'].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_states)

# Pie Chart
st.subheader("Payment Share")
payment_share = filtered.groupby('Payment_Type')['Amount'].sum()
st.write(payment_share)

# Insights
st.subheader("📌 Key Insights")
insights = generate_insights(df)
for i in insights:
    st.success(i)
