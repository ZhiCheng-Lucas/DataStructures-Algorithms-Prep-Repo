-- Write your PostgreSQL query statement below
SELECT curr.id
FROM Weather curr
JOIN Weather prev
ON curr.recordDate = prev.recordDate + INTERVAL '1 Day'
WHERE curr.temperature > prev.temperature