SELECT e.machine_id, ROUND((sum(e.timestamp)-sum(s.timestamp))/count(*),3) AS processing_time
FROM Activity s
JOIN Activity e
    ON s.activity_type = "start" 
    and e.activity_type = "end" 
    and e.process_id = s.process_id
    and e.machine_id = s.machine_id
group by machine_id
order by e.machine_id
-- 

-- (sum(e.timestamp)-sum(s.timestamp))/count(*) -> AVG(e.timestamp - s.timestamp)
