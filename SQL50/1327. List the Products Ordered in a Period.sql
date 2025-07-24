SELECT 
    p.product_name,
    SUM(o.unit) AS unit
FROM Products p
JOIN Orders o
    ON p.product_id = o.product_id 
    AND YEAR(o.order_date) = 2020 
    AND MONTH(o.order_date) = 2
GROUP BY p.product_name
    HAVING sum(o.unit) >= 100
