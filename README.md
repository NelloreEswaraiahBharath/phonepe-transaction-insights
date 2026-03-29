# PhonePe Transaction Insights

## Project Overview

This project focuses on analyzing PhonePe digital transaction data to extract meaningful insights about transaction patterns, user behavior, and geographical performance.

The data is processed using SQL for structured querying and Python for analysis. An interactive dashboard is built using Streamlit to visualize the results and enable real-time exploration.

---

## Objectives

- Analyze transaction data across states and districts
- Identify top-performing regions and payment categories
- Understand user engagement trends
- Generate actionable business insights
- Build an interactive dashboard for data visualization

---

## Technologies Used

- Python (Pandas)
- SQL (MySQL/PostgreSQL)
- Streamlit
- Data Visualization

---

## Project Structure

- dashboard.py : Main Streamlit dashboard application
- csv/ : Contains dataset files
- sql/ : SQL schema and query files
- analysis/ : Python scripts for insights generation
- utils/ : Helper functions for data loading and processing
- requirements.txt : Project dependencies
- README.md : Project documentation

---

## Data Processing Workflow

1. Data Extraction:
   Dataset is collected from PhonePe public repository and converted into CSV format.

2. Data Storage:
   Data is stored in SQL tables for structured querying.

3. Data Analysis:
   SQL queries are used to extract insights such as:
   - Top states by transaction volume
   - Payment category distribution
   - Yearly growth trends
   - Fraud detection patterns

4. Data Visualization:
   Streamlit dashboard is used to display:
   - Transaction trends
   - State-wise performance
   - Payment analysis
   - Key performance indicators

---

## Key Insights

- Top performing states contribute the majority of total transaction volume.
- UPI is the most dominant payment method in the ecosystem.
- There is a steady increase in yearly transaction growth, indicating rising adoption.
- Certain regions show lower engagement, representing growth opportunities.
- High-value transaction spikes may indicate potential anomalies or fraud patterns.

---

## Business Recommendations

- Focus marketing strategies on high-growth states to maximize returns.
- Introduce promotional offers in low-performing regions to improve adoption.
- Strengthen fraud detection mechanisms for abnormal transaction patterns.
- Promote widely used payment methods such as UPI for better engagement.
- Develop region-specific strategies based on transaction behavior.

---

## Results

- Improved understanding of digital payment trends
- Strong SQL query development skills
- Hands-on experience in data analysis using Python
- Ability to create interactive dashboards using Streamlit
- Practical exposure to real-world business problem solving

---

## How to Run the Project

1. Install dependencies:
   pip install -r requirements.txt

2. Run the Streamlit app:
   streamlit run dashboard.py

---

## Conclusion

This project demonstrates the ability to extract, analyze, and visualize transaction data to generate meaningful business insights. It highlights the practical application of SQL, Python, and data visualization tools in solving real-world problems in the digital payment domain.
