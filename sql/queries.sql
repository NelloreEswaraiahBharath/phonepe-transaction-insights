-- Top 10 States by Transaction Amount
SELECT State, SUM(Amount) as Total_Amount
FROM aggregated_transaction
GROUP BY State
ORDER BY Total_Amount DESC
LIMIT 10;

-- Payment Type Distribution
SELECT Payment_Type, SUM(Amount) as Total
FROM aggregated_transaction
GROUP BY Payment_Type;

-- Yearly Growth
SELECT Year, SUM(Amount) as Total
FROM aggregated_transaction
GROUP BY Year
ORDER BY Year;

-- Fraud Detection (Unusual high transactions)
SELECT *
FROM aggregated_transaction
WHERE Amount > (
    SELECT AVG(Amount) * 3 FROM aggregated_transaction
);

-- Customer Segmentation
SELECT State,
       CASE
           WHEN SUM(Amount) > 100000000 THEN 'High Value'
           WHEN SUM(Amount) > 50000000 THEN 'Medium Value'
           ELSE 'Low Value'
       END as Segment
FROM aggregated_transaction
GROUP BY State;
