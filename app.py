import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="Bharath",   # NOT root
    password="Bharath@1234",
    database="phonepe"
)

query = "SELECT * FROM transactions"
df = pd.read_sql(query, conn)

print(df.head())

import matplotlib.pyplot as plt

# State-wise total amount
state_data = df.groupby('state')['amount'].sum().sort_values(ascending=False)

plt.figure(figsize=(12,6))
state_data.head(10).plot(kind='bar')
plt.title("Top 10 States by Transaction Amount")
plt.xlabel("State")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.show()