# Write your MySQL query statement below
WITH Poor_query AS (
    SELECT query_name AS query_name, COUNT(*) AS poor_query_cnt
    FROM Queries
    WHERE rating < 3
    GROUP BY query_name
)

SELECT 
    q1.query_name, 
    ROUND(AVG(q1.rating/q1.position),2) AS quality,
    IFNULL(ROUND(pq.poor_query_cnt / COUNT(*) * 100,2),0) AS poor_query_percentage
FROM Queries q1
LEFT JOIN Poor_query pq
    ON pq.query_name = q1.query_name
GROUP BY q1.query_name
