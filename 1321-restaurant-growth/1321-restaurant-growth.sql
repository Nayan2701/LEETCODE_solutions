
WITH DailySum AS (
    SELECT visited_on, SUM(amount) AS day_total
    FROM Customer
    GROUP BY visited_on
)
SELECT 
    visited_on,
   
    (
        SELECT SUM(day_total)
        FROM DailySum
        WHERE visited_on BETWEEN DATE_SUB(ds.visited_on, INTERVAL 6 DAY) AND ds.visited_on
    ) AS amount,

    ROUND(
        (
            SELECT SUM(day_total) / 7
            FROM DailySum
            WHERE visited_on BETWEEN DATE_SUB(ds.visited_on, INTERVAL 6 DAY) AND ds.visited_on
        ), 2
    ) AS average_amount
FROM DailySum ds

WHERE visited_on >= (
    SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY)
    FROM Customer
)
ORDER BY visited_on;