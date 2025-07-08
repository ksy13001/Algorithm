WITH md AS (SELECT MIN(visited_on) AS min_date FROM Customer)

SELECT 
    c1.visited_on,
    SUM(c2.amount)/COUNT(DISTINCT c1.customer_id) AS amount,
    ROUND((SUM(c2.amount)/COUNT(DISTINCT c1.customer_id))/7.0, 2) AS average_amount
FROM Customer c1
JOIN Customer c2
    ON DATEDIFF(c1.visited_on, c2.visited_on) BETWEEN 0 AND 6 
GROUP BY c1.visited_on 
    HAVING DATEDIFF(c1.visited_on, (SELECT min_date from md)) >= 6
ORDER BY c1.visited_on
