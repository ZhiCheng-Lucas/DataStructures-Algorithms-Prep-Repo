-- Write your PostgreSQL query statement below
SELECT p.product_id, 
COALESCE(
        ROUND(SUM(p.price * 1.0 * u.units) / NULLIF(SUM(u.units),0) ,2)
        ,0) 
    AS average_price
FROM Prices p 
LEFT JOIN UnitsSold u
ON 
    p.product_id = u.product_id 
    AND 
    u.purchase_date BETWEEN p.start_date and p.end_date
GROUP BY 
    p.product_id
