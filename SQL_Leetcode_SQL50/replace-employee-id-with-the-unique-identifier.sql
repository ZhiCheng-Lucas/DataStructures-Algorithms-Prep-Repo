-- Write your PostgreSQL query statement below
SELECT 
    ui.unique_id,
    e.name
FROM
    Employees e
LEFT JOIN 
    EmployeeUNI ui
ON 
    ui.id = e.id
ORDER BY 
    name