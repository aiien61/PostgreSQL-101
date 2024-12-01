SELECT COUNT(*)
FROM orders
WHERE employeeid=3;

SELECT COUNT(*)
FROM order_details
WHERE quantity > 20;

-- How many order had a freight cost equal to or greater than $250
SELECT COUNT(*)
FROM orders
WHERE freight >= 250;

