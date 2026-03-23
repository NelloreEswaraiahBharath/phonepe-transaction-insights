-- View all data
SELECT * FROM aggregated_transaction;

-- Top 10 states by transaction amount
SELECT State, SUM(Amount) AS Total_Amount
FROM aggregated_transaction
GROUP BY State
ORDER BY Total_Amount DESC
LIMIT 10;

-- Year-wise growth
SELECT Year, SUM(Amount) AS Total_Amount
FROM aggregated_transaction
GROUP BY Year
ORDER BY Year;

-- Payment type analysis
SELECT Payment_Type, SUM(Transaction_Count) AS Total_Transactions
FROM aggregated_transaction
GROUP BY Payment_Type
ORDER BY Total_Transactions DESC;
