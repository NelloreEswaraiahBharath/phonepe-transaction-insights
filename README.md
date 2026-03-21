# phonepe-transaction-insights
Data analysis and visualization of PhonePe transaction data using Python, SQL, and Streamlit
# PhonePe Transaction Insights

## Project Overview

This project focuses on analyzing PhonePe transaction data to extract meaningful insights using Python, SQL, and Streamlit. The data is processed from raw JSON format into structured form for analysis and visualization.

## Objectives

* Analyze transaction trends across states and years
* Identify top-performing states and payment categories
* Understand user behavior and transaction patterns

## Tech Stack

* Python (Pandas, Matplotlib)
* MySQL
* Streamlit
* SQL

## Project Structure

* app.py – Data extraction and analysis
* dashboard.py – Streamlit dashboard
* requirements.txt – Required libraries

## Data Processing Workflow

1. Extract data from JSON files
2. Convert JSON data into CSV format
3. Load CSV data into MySQL database
4. Perform SQL queries for analysis
5. Visualize data using Python and Streamlit

## How to Run the Project

1. Install required libraries:
   pip install -r requirements.txt

2. Run the Streamlit dashboard:
   streamlit run dashboard.py

## Key Insights

* Identification of top states by transaction volume
* Analysis of year-wise transaction growth
* Understanding of most used payment types

## Conclusion

This project demonstrates end-to-end data analysis, starting from raw data extraction to building an interactive dashboard for insights.
