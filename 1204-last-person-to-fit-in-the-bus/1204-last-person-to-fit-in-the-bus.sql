# Write your MySQL query statement below
WITH CumulativeWeights AS (
    SELECT 
        person_name,
        turn,
        -- Calculate the running total of weight ordered by turn
        SUM(weight) OVER (ORDER BY turn) AS total_weight
    FROM Queue
)
SELECT person_name
FROM CumulativeWeights
-- Keep only the people who fit within the weight limit
WHERE total_weight <= 1000
-- Order by turn descending so the last person to fit is at the top
ORDER BY turn DESC
-- Limit the output to just that one person
LIMIT 1;