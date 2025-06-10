SELECT id-1 AS id, student
FROM Seat
WHERE id % 2 = 0

UNION ALL

SELECT 
    CASE
        WHEN 
        id = ( SELECT COUNT(*) FROM Seat ) THEN id
        ELSE id+1 
    END 
    AS id, 
    student
FROM Seat
WHERE id % 2 = 1

ORDER BY id
