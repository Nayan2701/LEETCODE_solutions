WITH FirstOrders AS (
    -- Step 1: Find the earliest order date for each customer
    SELECT customer_id, MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
)
SELECT 
    -- Step 3: Calculate the percentage of immediate orders
    ROUND(
        AVG(CASE WHEN d.order_date = d.customer_pref_delivery_date THEN 1 ELSE 0 END) * 100, 
        2
    ) AS immediate_percentage
FROM Delivery d
-- Step 2: Inner join to keep ONLY the first orders
JOIN FirstOrders f 
    ON d.customer_id = f.customer_id 
    AND d.order_date = f.first_order_date;