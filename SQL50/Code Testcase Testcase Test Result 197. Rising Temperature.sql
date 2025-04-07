SELECT w.id AS Id FROM Weather w 
JOIN Weather p 
    ON w.recordDate = p.recordDate + INTERVAL 1 DAY
where w.temperature > p.temperature

-- 날짜 계산: INTERVAL n S/M/H/D/M/Y
