SELECT
    employee_id,
    IF(
        COUNT(employee_id) > 1,
        SUM(CASE WHEN primary_flag="Y" THEN department_id END),
        SUM(department_id)
    )    AS department_id
FROM Employee 
GROUP BY employee_id

