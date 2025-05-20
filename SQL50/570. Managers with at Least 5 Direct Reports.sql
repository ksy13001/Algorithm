SELECT e1.name
FROM Employee e1
JOIN Employee e2
    on e1.id = e2.managerId
GROUP BY e1.id
    HAVING count(e1.id) >= 5
    
