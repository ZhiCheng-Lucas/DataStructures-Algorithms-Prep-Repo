-- Write your PostgreSQL query statement below
WITH 
    TotalUsers AS (
        SELECT COUNT(*) AS total_count  
        FROM Users
    ),
    ContestCounts AS (
        SELECT 
            contest_id, 
            COUNT(DISTINCT user_id) AS unique_users  
        FROM Register
        GROUP BY contest_id
    )

SELECT 
    cc.contest_id, 
    ROUND(unique_users * 100.0 / total_count, 2) AS percentage
FROM 
    ContestCounts cc
CROSS JOIN 
    TotalUsers tu
ORDER BY 
    percentage DESC, 
    cc.contest_id ASC;