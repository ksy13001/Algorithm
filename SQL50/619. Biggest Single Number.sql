SELECT MAX(Single_number.num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1 
    ) AS Single_number
