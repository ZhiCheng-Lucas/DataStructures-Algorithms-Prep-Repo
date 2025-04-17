-- Write your PostgreSQL query statement below
WITH single_number AS
    (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
    )

SELECT MAX(num) AS num FROM single_number
