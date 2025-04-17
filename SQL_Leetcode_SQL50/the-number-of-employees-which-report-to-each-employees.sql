-- Write your PostgreSQL query statement below
WITH report_list AS
    (
    SELECT reports_to as manager_id , COUNT(*) AS reports_count, ROUND(AVG(age),0) AS average_age
    FROM Employees
    WHERE reports_to is not NULL
    GROUP BY reports_to
    )

SELECT e.employee_id, name, r.reports_count, r.average_age
FROM Employees e
INNER JOIN report_list r ON e.employee_id = r.manager_id
ORDER BY employee_id ASC

