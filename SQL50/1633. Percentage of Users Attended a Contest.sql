SELECT
    contest_id, 
    ROUND(count(*) / (SELECT COUNT(*) FROM Users) * 100, 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage desc, contest_id
