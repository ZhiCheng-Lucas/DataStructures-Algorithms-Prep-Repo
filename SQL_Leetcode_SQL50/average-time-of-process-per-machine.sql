-- Write your PostgreSQL query statement below
WITH ProcessTime AS (
    SELECT s.machine_id, s.process_id,
    e.timestamp - s.timestamp AS processing_time
    FROM Activity s
    JOIN Activity e
    ON s.machine_id = e.machine_id
    AND s.process_id = e.process_id
    AND s.activity_type = 'start'
    AND e.activity_type = 'end'
)

SELECT machine_id, round(avg(processing_time)::numeric,3) AS processing_time 
FROM ProcessTime 
group by machine_id
