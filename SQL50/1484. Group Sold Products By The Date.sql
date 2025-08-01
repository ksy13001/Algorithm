SELECT
    sell_date,
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(DISTINCT product separator ',') AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date
