SELECT 
    ROUND(COUNT(DISTINCT a1.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity) 
    ,2) AS fraction
FROM Activity a1
JOIN (SELECT player_id, min(event_date) AS first_date FROM Activity GROUP BY player_id) a2
    ON a1.player_id = a2.player_id AND DATEDIFF(a1.event_date, a2.first_date) = 1
