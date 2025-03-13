-- Write your PostgreSQL query statement below
WITH student_subject_pairs AS (
    SELECT 
        s.student_id, 
        s.student_name, 
        su.subject_name
    FROM Students s 
    CROSS JOIN Subjects su
) 

SELECT 
    ssp.student_id, 
    ssp.student_name, 
    ssp.subject_name, 
    COUNT(e.student_id) AS attended_exams
FROM student_subject_pairs ssp
LEFT JOIN Examinations e ON ssp.student_id = e.student_id 
                        AND ssp.subject_name = e.subject_name
GROUP BY 
    ssp.student_id, 
    ssp.student_name, 
    ssp.subject_name
ORDER BY 
    ssp.student_id, 
    ssp.subject_name;