# Write your MySQL query statement below
SELECT DISTINCT id,
MAX(CASE WHEN Month = "Jan" THEN revenue END) AS Jan_Revenue,
MAX(CASE WHEN Month = "Feb" THEN revenue END) AS Feb_Revenue,
MAX(CASE WHEN Month = "Mar" THEN revenue END) AS Mar_Revenue,
MAX(CASE WHEN Month = "Apr" THEN revenue END) AS Apr_Revenue,
MAX(CASE WHEN Month = "May" THEN revenue END) AS May_Revenue,
MAX(CASE WHEN Month = "Jun" THEN revenue END) AS Jun_Revenue,
MAX(CASE WHEN Month = "Jul" THEN revenue END) AS Jul_Revenue,
MAX(CASE WHEN Month = "Aug" THEN revenue END) AS Aug_Revenue,
MAX(CASE WHEN Month = "Sep" THEN revenue END) AS Sep_Revenue,
MAX(CASE WHEN Month = "Oct" THEN revenue END) AS Oct_Revenue,
MAX(CASE WHEN Month = "Nov" THEN revenue END) AS Nov_Revenue,
MAX(CASE WHEN Month = "Dec" THEN revenue END) AS Dec_Revenue
FROM Department
Group by id