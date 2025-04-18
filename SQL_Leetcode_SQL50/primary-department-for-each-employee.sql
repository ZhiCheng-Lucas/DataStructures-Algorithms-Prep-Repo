-- Write your PostgreSQL query statement below

WITH employee_count AS 
(
    SELECT employee_id, COUNT(*) AS department_count
    FROM Employee
    GROUP BY employee_id
)

SELECT e.employee_id, department_id
FROM Employee e
INNER JOIN employee_count c ON c.employee_id = e.employee_id
WHERE department_count = 1 OR primary_flag = 'Y'