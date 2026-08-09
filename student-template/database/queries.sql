SELECT 
    customer_id, 
    SUM(total_amount) AS total_order_value
FROM 
    orders
WHERE 
    EXTRACT(YEAR FROM order_date) = 2025
GROUP BY 
    customer_id
ORDER BY 
    total_order_value DESC
LIMIT 5;
-- QUESTION 2.1: SQL Query
-- Task: Find top 5 customers by total order value for the year 2025.
-- Tables: orders(order_id, customer_id, total_amount, order_date)

-- Write your SQL query below
