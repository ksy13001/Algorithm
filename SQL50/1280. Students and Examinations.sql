SELECT st.student_id, st.student_name, sb.subject_name, count(ex.subject_name) AS attended_exams 
FROM Students st
CROSS JOIN Subjects sb
LEFT JOIN Examinations ex
    ON ex.student_id = st.student_id
    AND ex.subject_name = sb.subject_name
GROUP BY 1, 2, 3
ORDER BY 1
