-- Write your PostgreSQL query statement below
SELECT
    p.product_name, 
    s.year,
    s.price
FROM 
    Product p
INNER JOIN 
    Sales s
ON 
    s.product_id = p.product_id
ORDER BY
    p.product_name, 
    s.year